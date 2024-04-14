import sys
from antlr4 import *
from GrammarComponents.GrammarLexer import GrammarLexer
from GrammarComponents.GrammarParser import GrammarParser
from GrammarComponents.GrammarListener import GrammarListener
from Components.Listener.evalListener import evalListener
from Components.Listener.errorListener import MyErrorListener
from Components.Listener.stackCompileListener import stackCompileListener


def main(argv):
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = input("Filename: ").strip()

    input_stream = FileStream(filename)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() == 0:
        listener = evalListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        print(f"\n\033[1;32mSuccessfully parsed\033[0m")
    else:
        exit(1)
    
    listener2 = stackCompileListener("./Outputs/output3.txt")
    walker2 = ParseTreeWalker()
    walker2.walk(listener2, tree)

if __name__ == '__main__':
    main(sys.argv)
