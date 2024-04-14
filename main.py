import argparse
from my_interp import InterpreterProgram


def main(arguments):
    prog = InterpreterProgram(arguments.file)
    prog.run()

    print()
    print(prog)


def parse_arguments():
    """
    Parse Input arguments
    :return: Namespace of input arguments
    """
    parser = argparse.ArgumentParser(description='My Custom Interpreter')
    parser.add_argument('-f', '--file', help='File to interpret')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
