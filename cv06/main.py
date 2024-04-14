import re

class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        try:
            result = self.E()
            if self.index == len(self.expression):
                return result
            else:
                return "ERROR"
        except Exception as e:
            return "ERROR"

    def E(self):
        result = self.T()
        return self.E1(result)

    def E1(self, acc):
        if self.index < len(self.expression):
            op = self.expression[self.index]
            if op in ['+', '-']:
                self.index += 1
                operand = self.T()
                if op == '+':
                    return self.E1(acc + operand)
                else:
                    return self.E1(acc - operand)
        return acc

    def T(self):
        result = self.F()
        return self.T1(result)

    def T1(self, acc):
        if self.index < len(self.expression):
            op = self.expression[self.index]
            if op in ['*', '/']:
                self.index += 1
                operand = self.F()
                if op == '*':
                    return self.T1(acc * operand)
                else:
                    if operand != 0:
                        return self.T1(acc / operand)
                    else:
                        raise ValueError("Division by zero")
        return acc

    def F(self):
        if self.index < len(self.expression):
            token = self.expression[self.index]
            self.index += 1
            if token == '(':
                result = self.E()
                if self.expression[self.index] == ')':
                    self.index += 1
                    return result
                else:
                    raise ValueError("Mismatched parentheses")
            elif re.match(r'\d+', token):
                return int(token)
            else:
                raise ValueError("Invalid token: {}".format(token))
        else:
            raise ValueError("Unexpected end of expression")


N = int(input())
for _ in range(N):
    expression = input().strip()
    parser = Parser(expression)
    result = parser.parse()
    print(result)
