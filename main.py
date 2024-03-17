# Lexer
def lexer(code):
    return code.replace("\n", " ").split()

# Parser
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        else:
            raise SyntaxError("Invalid token: " + tokens[i])
    return parsed

# Interpreter
def interpreter(parsed_code):
    variables = {}
    for instruction in parsed_code:
        if instruction[0] == "PRINT":
            print(instruction[1])
        elif instruction[0] == "SET":
            variables[instruction[1]] = instruction[2]

# Example code
code = """
SET x 10
PRINT x
"""

# Main
if __name__ == "__main__":
    tokens = lexer(code)
    parsed = parser(tokens)
    interpreter(parsed)
# Writing code to a file
with open("test.z--", "w") as file:
    file.write(code)
# Define your custom language code
code = """
SET x 10
PRINT x
"""

# Writing code to a file
filename = "test.z--"
with open(filename, "w") as file:
    file.write(code)

print(f"File '{filename}' has been created with the following code:")
print(code)
# Define lexer function
def lexer(code):
    return code.replace("\n", " ").split()

# Define parser function
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        else:
            raise SyntaxError("Invalid token: " + tokens[i])
    return parsed

# Define interpreter function
def interpreter(parsed_code):
    variables = {}
    for instruction in parsed_code:
        if instruction[0] == "PRINT":
            print(instruction[1])
        elif instruction[0] == "SET":
            variables[instruction[1]] = instruction[2]

# Read code from file
filename = "test.Z"
with open(filename, "r") as file:
    code = file.read()

# Tokenize, parse, and execute the code
tokens = lexer(code)
parsed = parser(tokens)
interpreter(parsed)
# Updated parser function
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        else:
            raise SyntaxError("Invalid token: " + tokens[i])
        i += 1  # Move to the next token
    return parsed

# Updated interpreter function
def interpreter(parsed_code):
    variables = {}
    for instruction in parsed_code:
        if instruction[0] == "PRINT":
            # Check if it's a variable or a string
            value = variables.get(instruction[1], instruction[1])
            print(value)
        elif instruction[0] == "SET":
            variables[instruction[1]] = instruction[2]
# Updated lexer function to recognize strings
def lexer(code):
    tokens = []
    current_token = ''
    in_string = False

    for char in code:
        if char == '"':
            if in_string:
                tokens.append(('STRING', current_token))
                current_token = ''
                in_string = False
            else:
                in_string = True
        elif char.isspace() and not in_string:
            continue
        else:
            current_token += char

    return tokens

# Updated parser function to handle strings
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i][0] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        elif tokens[i][0] == "STRING":
            parsed.append(("STRING", tokens[i][1]))  # New: handle strings
            i += 1
        else:
            raise SyntaxError("Invalid token: " + tokens[i][0])
        i += 1  # Move to the next token
    return parsed

# Updated lexer function to recognize strings
def lexer(code):
    tokens = []
    current_token = ''
    in_string = False

    for char in code:
        if char == '"':
            if in_string:
                tokens.append(('STRING', current_token))
                current_token = ''
                in_string = False
            else:
                in_string = True
        elif char.isspace() and not in_string:
            continue
        else:
            current_token += char

    return tokens

# Updated parser function to handle strings
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i][0] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        elif tokens[i][0] == "STRING":
            parsed.append(("STRING", tokens[i][1]))  # New: handle strings
            i += 1
        else:
            raise SyntaxError("Invalid token: " + tokens[i][0])
        i += 1  # Move to the next token
    return parsed

# Updated interpreter function to handle strings
def interpreter(parsed_code):
    variables = {}
    for instruction in parsed_code:
        if instruction[0] == "PRINT":
            value = variables.get(instruction[1], instruction[1])
            print(value)
        elif instruction[0] == "SET":
            variables[instruction[1]] = instruction[2]
        elif instruction[0] == "STRING":
            print(instruction[1])  # New: print the string
# Updated lexer function to recognize "good bye"
def lexer(code):
    tokens = []
    current_token = ''
    in_string = False

    for char in code:
        if char == '"':
            if in_string:
                tokens.append(('STRING', current_token))
                current_token = ''
                in_string = False
            else:
                in_string = True
        elif char.isspace() and not in_string:
            continue
        else:
            current_token += char

    # Check for "good bye" string
    if "good bye" in code:
        tokens.append(("GOODBYE", "good bye"))

    return tokens

# Updated parser function to handle "good bye"
def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == "PRINT":
            parsed.append(("PRINT", tokens[i+1]))
            i += 2
        elif tokens[i][0] == "SET":
            parsed.append(("SET", tokens[i+1], tokens[i+2]))
            i += 3
        elif tokens[i][0] == "STRING":
            parsed.append(("STRING", tokens[i][1]))
            i += 1
        elif tokens[i][0] == "GOODBYE":
            parsed.append(("GOODBYE", tokens[i][1]))  # New: handle "good bye"
            i += 1
        else:
            raise SyntaxError("Invalid token: " + tokens[i][0])
        i += 1  # Move to the next token
    return parsed

# Updated interpreter function to handle "good bye"
def interpreter(parsed_code):
    variables = {}
    for instruction in parsed_code:
        if instruction[0] == "PRINT":
            value = variables.get(instruction[1], instruction[1])
            print(value)
        elif instruction[0] == "SET":
            variables[instruction[1]] = instruction[2]
        elif instruction[0] == "STRING":
            print(instruction[1])
        elif instruction[0] == "GOODBYE":
            print("Good bye!")  # New: print "good bye" message

