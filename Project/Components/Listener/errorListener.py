from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        message = f"\033[1;31mRule stack: {stack}\033[0m"
        message += f"\n\033[1;31mSyntax error at line {line}:{column} - {msg}\033[0m"
        print(message)
