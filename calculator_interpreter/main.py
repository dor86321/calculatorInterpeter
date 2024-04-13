import sys
from interpreter.lexer import lexer
from interpreter.parser import parser
from utils import constants as consts

MAX_RESULT_LENGTH = consts.MAX_RESULT_LENGTH
MAX_PROGRAM_LENGTH = consts.MAX_RESULT_LENGTH
MAX_VARIABLES = consts.MAX_VARIABLES

def main():
    if len(sys.argv) > 1:
        # If a file path is provided as a command-line argument
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            data = file.read()

            # Limit program size
            lines = data.split('\n')[:MAX_PROGRAM_LENGTH]
            data = '\n'.join(lines)

            if len(lines) >= MAX_PROGRAM_LENGTH:
                print("Warning: Maximum program size exceeded. Only the first 32 lines will be executed.")

            try:
                result = parser.parse(data, lexer=lexer)
                # Convert the result to a string if it's an integer
                if isinstance(result, int):
                    result = str(result)
                # Truncate the result if it exceeds MAX_RESULT_LENGTH
                result = result[:MAX_RESULT_LENGTH]
                print("Result of Parsing:", result)
            except SyntaxError as e:
                print(f"SyntaxError: {e}")
    else:
        # If no command-line argument, take input interactively
        lines = []  # List to store lines of input
        while len(lines) < MAX_PROGRAM_LENGTH:  # Limit number of lines
            try:
                s = input('calculator > ')
                if s.strip() == "exit":  # Type "exit" to quit the calculator
                    break
                if len(s) > MAX_PROGRAM_LENGTH:
                    print(f"Error: Maximum program length exceeded. Maximum allowed length is {MAX_PROGRAM_LENGTH}.")
                    continue  # Skip parsing this line

                # Count variables in the input
                lexer.input(s)
                num_variables = sum(1 for token in lexer if token.type == 'IDENTIFIER')

                if num_variables > MAX_VARIABLES:
                    print(f"Error: Maximum number of variables exceeded. Maximum allowed is {MAX_VARIABLES}.")
                    continue  # Skip parsing this line

                lines.append(s)  # Add the line to the list of lines
            except EOFError:
                break

        if len(lines) >= MAX_PROGRAM_LENGTH:
            print("Warning: Maximum program size exceeded. Only the first 50 lines will be executed.")

        # Join all the lines into a single string separated by newline characters
        input_data = '\n'.join(lines)

        # Parse the input data
        try:
            result = parser.parse(input_data, lexer=lexer)
            # Convert the result to a string if it's an integer
            if isinstance(result, int):
                result = str(result)
            # Truncate the result if it exceeds MAX_RESULT_LENGTH
            result = result[:MAX_RESULT_LENGTH]
            print("Result:", result)
        except SyntaxError as e:
            print(f"SyntaxError: {e}")

if __name__ == "__main__":
    main()