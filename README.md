# calculatorInterpeter
A simple calculator interpreter based on custom BNF rules

# Calculator Interpreter Rules
## General Rules:
Max Program Size: 32 lines. Programs exceeding this will only execute the first 40 lines.
Max Calculation Length:  64 characters. Any calculation exceeding this limit will result in an error message displayed on the screen.
Max Variables Allowed: 6 variables are allowed per program. Exceeding this limit will result in an error message displayed on the screen
Max Variable Name Size: 4 characters. Variable names exceeding this limit will result in an error message displayed on the screen.
Variable Restrictions: Variable names must be alphabetic only. No numbers or special symbols are permitted.

## Overflow Handling:
Calculation Overflow: If a calculation exceeds the maximum length allowed, an error message will be shown on the screen.
Program Overflow: If the program code exceeds the maximum length allowed, only the first 64 lines of code will be executed.

## Error Handling:
The calculator will display an error message for any rule violations, such as exceeding length limits or using invalid variable names.
In the case of program overflow, the calculator will execute only the first 64 lines of code and ignore the rest.

# Calculator Syntax (EBNF)
## Constructs:

`<numeric_sequence>` ::= `<unit_number>` | `<numeric_sequence>` `<unit_number>`
`<unit_number>` ::= `<integer>` | `+<integer>` | `-<integer>`
`<integer>` ::= `<nonzero_digit>` | `<integer>` `<zero_digit>` | `<integer>` `<nonzero_digit>`
`<nonzero_digit>` ::= [1-9]
`<zero_digit>` ::= 0

# Boolean Operators Syntax
`<comparison_ops>` ::= `<equals>` | `<greater_than>` | `<less_than>`
`<equals>` ::= `==`
`<less_than>` ::= `<`
`<greater_than>` ::= `>`


# Math Operators Syntax

- `<math_operation>` ::= `<add_op>` | `<subtract_op>` | `<multiply_op>` | `<divide_op>` | `<exponent_op>`
- `<add_op>` ::= `+`
- `<subtract_op>` ::= `-`
- `<multiply_op>` ::= `X` | `x`
- `<divide_op>` ::= `/`
- `<exponent_op>` ::= `^`

# Program Syntax Definition

`<code_structure>` ::= `<operations_list>`
`<operations_list>` ::= `<single_operation>` | `<operations_list>` `<single_operation>`
`<single_operation>` ::= `<assignment>` | `<math_calculation>` | `<if_condition>` | `<output_operation>` | `<while_loop>` | `<new_command>`
`<assignment>` ::= `<identifier>` "=" `<expression>`
`<math_calculation>` ::= `<identifier>` "=" `<expression>` `<arithmetic_operator>`
`<if_condition>` ::= "if" `<boolean_condition>` ":" `<operations_list>` `<else_condition>`
`<else_condition>` ::= "elif" `<boolean_condition>` ":" `<operations_list>`
`<while_loop>` ::= "while" `<boolean_condition>` ":" `<operations_list>`
`<output_operation>` ::= ">>" "(" `<expression>` ")"
`<expression>` ::= `<term>` | `<expression>` `<term>`
`<term>` ::= `<identifier>` | `<number>`
`<identifier>` ::= `<number_sequence>`
`<new_command>` ::= "new" `<identifier>` "=" `<expression>`

## Note:
`<arithmetic_operator>` is defined in the Arithmetic Operations Syntax section.
`<boolean_condition>` is defined in the Comparison Operators Syntax section.
`<number>` and `<number_sequence>` are defined in the Numeric Expressions section.


