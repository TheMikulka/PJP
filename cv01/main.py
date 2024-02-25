def parser(expression): 
    expression = expression.replace(" ", "")
    for char in expression:
        if char not in "0123456789+-*/()":
            return "ERROR2" 

    if expression[0] in "+-*/" or expression[-1] in "+-*/":
        return "ERROR"

    try:
        return evaluate(expression)
    except ZeroDivisionError:
        return "ERROR"
    except:
        return "ERROR"

def evaluate(expression):
    operators = []
    operands = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ""
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            operands.append(int(num))
            continue
        elif expression[i] in "+-*/":
            while operators and priority(operators[-1]) >= priority(expression[i]):
                apply_operation(operators.pop(), operands)
            operators.append(expression[i])
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operation(operators.pop(), operands)
            operators.pop()
        i += 1

    while operators:
        apply_operation(operators.pop(), operands)

    return operands[0]

def priority(operator):
    if operator in '+-':
        return 1
    elif operator in '*/':
        return 2
    return 0

def apply_operation(operator, operands):
    right_operand = operands.pop()
    left_operand = operands.pop()
    if operator == '+':
        operands.append(left_operand + right_operand)
    elif operator == '-':
        operands.append(left_operand - right_operand)
    elif operator == '*':
        operands.append(left_operand * right_operand)
    elif operator == '/':
        operands.append(left_operand / right_operand)

def main():
    n = int(input())

    for i in range(n):
        expression = input()
        print(parser(expression))
    
if __name__ == "__main__":
    main()


