IDENTIFICATION = 1
PROCEDURE = 3
WHITESPACE = "    "


def parse_source(source: list):
    program = {}
    program["identification"] = []
    program["procedure"] = []
    current_section = None
    line_number = 0
    for line in source:
        line_number += 1
        print("Line " + str(line_number))
        if line[0] != "indent":
            current_section = None
            print("Starting new section")
            current_section = get_section(line[0])
        elif current_section == IDENTIFICATION:
            pass
        elif current_section == PROCEDURE:
            program["procedure"].extend(tokenise(line))
    program["procedure"].append("END")
    return program


def get_section(token):
    if token == "Identification:":
        print("Entering identification section")
        return IDENTIFICATION
    if token == "Procedure:":
        print("Entering procedure section")
        return PROCEDURE


def tokenise(line):
    output = []
    if line[1] == "display":
        output.append("DISPLAY")
        tail = " ".join(line[2:])
        string_start = str.find(tail, '"')
        string_end = str.find(tail, '"', string_start+1)
        output.append(tail[string_start+1:string_end])
    return output
