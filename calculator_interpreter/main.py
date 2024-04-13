# File: main.py
import sys
from interpreter.lexer import lexer
from interpreter.parser import parser

def main():
    if len(sys.argv) > 1:
        # If a file path is provided as a command-line argument
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            data = file.read()
            # Parsing the data from the file using the lexer and parser
            result = parser.parse(data, lexer=lexer)
            print("Result of Parsing:", result)
    else:
        # If no command-line argument, take input interactively
        while True:
            try:
                s = input('calculator > ')
                if s.strip() == "exit":  # Type "exit" to quit the calculator
                    break
                result = parser.parse(s, lexer=lexer)
                print("Result:", result)
            except EOFError:
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
