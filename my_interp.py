import copy
import re
from dataclasses import dataclass

# Config
VARIABLE_MAX_LENGTH = 4
NUM_OF_MAX_VARIABLES = 6


@dataclass
class Variable:
    name: str
    value: int

    def __post_init__(self):
        if len(self.name) > VARIABLE_MAX_LENGTH:
            raise ValueError(f'The variable name "{self.name}" are to long ({len(self.name)}), '
                             f'Max allowed length is {VARIABLE_MAX_LENGTH}')
        elif not self.name.isalpha():
            raise ValueError(f'The variable name {self.name} not valid, must be alphabetic only')
        elif not isinstance(self.value, int):
            raise ValueError(f'The value {self.value} not valid, must be an integer')


class InterpreterProgram:
    def __init__(self, program_file: str):
        self.program_file = program_file

        self.line_count = 0
        self.variables = {}

        self.if_skip = False
        self.if_start = False

        self.while_loop_commands = []
        self.while_start = False

    def __str__(self):
        summary = f'summary:\n' \
                  f'Number of lines: {self.line_count}\n' \
                  f'Number of variables: {len(self.variables)}\n'
        for var, val in self.variables.items():
            summary += f'{var} = {val.value}\n'
        return summary

    def run(self) -> None:
        # read all lines into local variables to avoid multiple file access
        with open(self.program_file, 'r') as file:
            program_lines = file.readlines()

        # Interpret the program line by line
        for line in program_lines:
            if self.handle_line(line):
                self.line_count += 1

    def handle_line(self, line: str) -> bool:
        """
        Handle a programs line

        :param line: line to handle
        :return: True if line is handled false if empty line or comment
        """
        line = line.strip()

        # Ignore comment lines
        if line.startswith('#') or line == '':
            return False

        # skip to the end of the skip command
        if self.if_skip:
            if line.startswith('end if'):
                self.handle_end_if_command(line)
            else:
                # skip the line
                return False
        elif self.while_start:
            # collect the commands until the 'end while' line
            if line.startswith('end while'):
                self.handle_end_while_command(line)
            else:
                self.while_loop_commands.append(line)
        # check for 'new' command
        elif line.startswith('new'):
            self.handle_new_command(line)
        # Handle output command
        elif line.startswith('>>'):
            self.handle_output_command(line)
        # Check for an 'if'
        elif line.startswith('if'):
            self.handle_if_command(line)
        # Check for 'end if'
        elif line.startswith('end if'):
            self.handle_end_if_command(line)
        # Check for assignment to existing variable - line starts with existing variable
        elif self.is_assignment(line):
            self.handle_assignment_command(line)
        # check for while command
        elif line.startswith('while'):
            self.handle_while_command(line)
        elif line.startswith('end while'):
            self.handle_end_while_command(line)
        else:
            raise ValueError(f'The line:\n'
                             f'{line}\n'
                             f'not valid')

        return True

    def handle_if_command(self, line: str) -> None:
        """
        We assume that If condition is in the following format
        if (condition):
            expression
            ...
        end if

        if condition is true - raise an if_start and continue
        if condition is false - raise an if_skip and skip the lines till 'end if' command

        :param line: line to interpret
        :return:
        """
        new_pattern = re.compile(r"if\s*\((.*)\)\s*:")
        condition = new_pattern.findall(line)[0]

        res = self.check_condition(condition)

        self.if_start = True
        if not res:
            self.if_skip = True

    def handle_end_if_command(self, line: str) -> None:
        """
        We assume that If condition is in the following format
        if (condition):
            expression
            ...
        end if

        If we reached this command and if_skip or if_start is True we need to reset it to False
        If we reached this command and both if_skip and if_start is False this is invalid syntax

        :param line: line to interpret
        :return:
        """
        if not line == 'end if':
            raise SyntaxError('"end if" syntax error')

        if self.if_start:
            self.if_start = False
            self.if_skip = False
        else:
            raise SyntaxError('"end if" command before if command')

    def handle_while_command(self, line: str) -> None:
        """
        We assume that while condition is in the following format
        while (condition):
            expression
            ...
        end while

        :param line: line to interpret
        :return:
        """
        self.while_start = True
        self.while_loop_commands.append(line)

    def handle_end_while_command(self, line: str) -> None:
        """
        We assume that while condition is in the following format
        while (condition):
            expression
            expression
            ...
        end while

        If we reached this command and while_start True we need to reset it to False
        If we reached this command and while_start is False this is invalid syntax

        :param line: line to interpret
        :return:
        """
        if not line == 'end while':
            raise SyntaxError('"end while" syntax error')

        if self.while_start:
            self.while_start = False
        else:
            raise SyntaxError('"end while" command before "while" command')

        self.while_run()

    def while_run(self) -> None:
        """
        Run the while loop
        all the while commands are in the while_loop_commands variable
        run it in loop till while condition is false
        :return: None
        """
        new_pattern = re.compile(r"while\s*\((.*)\)\s*:")
        condition = new_pattern.findall(self.while_loop_commands.pop(0))[0]

        while self.check_condition(condition):
            # copy the while loop to local variable
            temp_loop = copy.deepcopy(self.while_loop_commands)
            for line in temp_loop:
                self.handle_line(line)

    def check_condition(self, condition: str) -> bool:
        """
        Condition is in the following format:
        A <cond> B
        Cond = >,<,==

        :param condition: Condition to evaluate
        :return: True if condition is true, False otherwise
        """
        comparison_ops = ['>', '<', '==']

        exp_left, exp_right, opr = self.split_on_first(expression=condition, operators=comparison_ops)
        value_left = self.get_value_from_single_expression(expression=exp_left.strip())
        value_right = self.get_value_from_single_expression(expression=exp_right.strip())

        match opr:
            case '>':
                res = value_left > value_right
            case '<':
                res = value_left < value_right
            case '==':
                res = value_left == value_right
            case _:
                raise SyntaxError(f'Invalid condition: {condition}')
        return res

    def is_assignment(self, line: str) -> bool:
        """
        We assume that assignment command is in the following format
        existing_var = expression

        :param line: line to interpret
        :return: True is this line is assignment command false otherwise
        """
        expressions = line.split('=')
        if len(expressions) != 2:
            return False
        return expressions[0].strip() in self.variables

    def handle_assignment_command(self, line: str) -> None:
        """
        We assume that assignment command is in the following format
        existing_var = expression

        :param line: line to interpret
        :return:
        """
        expressions = line.split('=')
        if len(expressions) != 2:
            return

        var = self.variables[expressions[0].strip()]
        var.value = self.handle_expression(expressions[1])

    def handle_new_command(self, line: str):
        """
        Handle the new command:
        Define new variable in the program and initiate it with a value
        The format of the new command is:
        new "identifier" = expression

        :param line: line to interpret
        :return:
        """
        new_pattern = re.compile(r"new\s+(\w+)\s*=\s*(.+)")
        variable, value = new_pattern.findall(line)[0]
        self.variables[variable] = Variable(variable, self.handle_expression(value))

    def handle_expression(self, expression: str) -> int:
        """
        We assume expression is one of the following:
        int
        var
        var operator var
        var operator int
        int operator var
        int operator int

        :param expression: expression to evaluate
        :return: The value of the evaluated expression
        """
        expression = expression.strip()

        operators = ['+', '-', 'X', 'x', '/', '^']

        # Check if there are an operator in the string
        if not any(op in expression for op in operators):
            result = self.get_value_from_single_expression(expression=expression.strip())
        else:
            # Separate the string by the first operator
            exp_left, exp_right, opr = self.split_on_first(expression, operators)

            match opr:
                case '+':
                    result = self.handle_expression(exp_left) + self.handle_expression(exp_right)
                case '-':
                    result = self.handle_expression(exp_left) - self.handle_expression(exp_right)
                case 'X' | 'x':
                    result = self.handle_expression(exp_left) * self.handle_expression(exp_right)
                case '/':
                    result = self.handle_expression(exp_left) // self.handle_expression(exp_right)
                case '^':
                    result = self.handle_expression(exp_left) ** self.handle_expression(exp_right)
                case _:
                    raise SyntaxError(f'Invalid expression: {expression}')
        return result

    def get_value_from_single_expression(self, expression: str) -> int:
        if expression.isdigit():
            # The expression is integer
            return int(expression)

        # The expression is variable
        # check if variable defined:
        if expression not in self.variables:
            raise ValueError(f'Not defined variable {expression}')
        return self.variables[expression].value

    @staticmethod
    def split_on_first(expression: str, operators: list) -> list:
        active_opr = None
        for operator in operators:
            if operator in expression:
                active_opr = operator
                break
        vals = expression.split(active_opr, 1)
        vals.append(active_opr)
        return vals

    def handle_output_command(self, line: str):
        """
        print the provided variable:
        syntax:
        print empty line:
        >>
        print text:
        >> 'My text'
        print variable:
        >> var

        :param line: line to interpret
        :return:
        """
        new_pattern = re.compile(r">>\s*(.*)")
        variable = new_pattern.findall(line)[0]

        if variable in self.variables:
            print(self.variables[variable].value)
        else:
            print(variable)
