import sys


def lex_file():
    if len(sys.argv) > 1:
        print("Lexing file " + sys.argv[1])
        source = get_source_lines(sys.argv[1])
        parsed_source = parse_source(source)
        print(parsed_source)
        return parsed_source
    else:
        print("No input file. Terminating.")


def get_source_lines(filename: str):
    with open(filename) as f:
        content = f.readlines()
        print(content)
        content = [x.replace("\t", "indent ") for x in content]
        print(content)
        content = [x.strip() for x in content]
        print(content)
    return content


def parse_source(source: list):
    parsed_source = []
    for source_line in source:
        content = str.split(source_line, " ")
        parsed_source.append(content)
    return parsed_source


if __name__ == "__main__":
    lex_file()
