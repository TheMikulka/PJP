# Lexical analyzer
# Write a program, that reads an input and converts it into a sequence of lexical symbols – tokens. Each token is a pair, it composes from a type and possibly a value.

# The tokens definition depends on you, and it is considered a part of the solution.

# Input specification
# The input may be containing the following symbols:

# identifiers - consisting of a sequence of letters and numbers starting with a letter
# numbers - formed by a sequence of decimal digits
# operators - symbols '+', '-', '*' and '/',
# delimiters - symbols '(', ')' and ';',
# keywords - div and mod.
# Symbols can be separated by a sequence of spaces, tabs, and line breaks.

# There can be notes in the input. Notes are preceded by a sequence // and continue to the end of the line.

# White spaces and notes does not produce any lexical symbols.

# Output specification
# Converts the given input into a sequence of tokens and write them on output. Write each token on a separated line.


# Example
# Input
#     -2 + (245 div 3);  // note
# 2 mod 3 * hello
# Output
# Your output can be different, it depends on your definition of tokens.

# OP:-
# NUM:2
# OP:+
# LPAR
# NUM:245
# DIV
# NUM:3
# RPAR
# SEMICOLON
# NUM:2
# MOD
# NUM:3
# OP:*
# ID:hello


import re

def tokenize_input(input_text):
    tokens = []
    patterns = [
        (r'\b(div)\b', "DIV"),              
        (r'\b(mod)\b', "MOD"),              
        (r'[a-zA-Z][a-zA-Z0-9]*', 'ID'),       
        (r'\d+', 'NUM'),                          
        (r'[+\-*/]', 'OP'),                       
        (r'\(', 'LPAR'),                          
        (r'\)', 'RPAR'),                         
        (r';', 'SEMICOLON'),                    
    ]

    for line in input_text.split('\n'):
        line = re.sub(r'//.*', '', line)
        while line:
            matched = False
            for pattern, token_type in patterns:
                match = re.match(pattern, line)
                if match:
                    value = match.group(0)
                    tokens.append((token_type, value))
                    line = line[len(value):].lstrip()
                    matched = True
            if not matched:
                print("Invalid token:", line[0])
                line = line[1:]

    return tokens

def main():
    with open('test.txt', 'r') as file:
        input_text = file.read()

    tokens = tokenize_input(input_text)
    for token_type, value in tokens:
        if token_type in ['DIV', 'LPAR', 'RPAR', 'SEMICOLON', 'MOD']:
            print(token_type)
        else:
            print(f"{token_type}: {value}")

if __name__ == "__main__":
    main()
