import sys

from postbol import pylex, pyparse


def compile_file():
    if len(sys.argv) > 1:
        print("Compiling file " + sys.argv[1])
        lexed_program = pylex.lex_file()
        parsed_program = pyparse.parse_source(lexed_program)
        print(parsed_program)
    else:
        print("No input file. Terminating.")


if __name__ == "__main__":
    compile_file()
