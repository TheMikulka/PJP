class Interpreter:
    def __init__(self, path: str):
        self.__instruction_pointer = 0
        self.__stack = []
        self.__variables = {}
        
        self.__instructions = []
        with open(path, 'r') as file:
            self.__instructions = file.readlines()

        for i in range(len(self.__instructions)):
            self.__instructions[i] = self.__instructions[i].strip()
        
    def _run(self):
        while self.__instruction_pointer < len(self.__instructions):
            self.__interpret()
            self.__instruction_pointer += 1
    
    def __interpret(self):
        line = self.__instructions[self.__instruction_pointer].split(' ', 1)
        match line[0]:
            case "push":
                var_type, var_value = line[1].split(' ',1)
                self.__stack.append(self.__get_variable_type(var_type, var_value))
            case "pop":
                self.__stack.pop()
            case "save":
                self.__variables[line[1]] = self.__stack.pop()
            case "print":
                out = []
                for i in range(int(line[1])):
                    value = self.__stack.pop()
                    if isinstance(value, bool):
                        out.append(str(value).lower())
                    else:
                        out.append(str(value))
                out.reverse()
                print(f"\033[1;32m:>> \033[0m{"".join(out)}")
            case "load":
                self.__stack.append(self.__variables[line[1]])
            case "itof":
                self.__stack.append(float(self.__stack.pop()))
            case "uminus":
                self.__stack.append(-self.__stack.pop())
            case "not":
                self.__stack.append(not self.__stack.pop())
            case "mul":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 * var1)
            case "div":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                if isinstance(var1, float) or isinstance(var2, float):
                    self.__stack.append(var2 / var1)
                elif isinstance(var1, int) and isinstance(var2, int):
                    self.__stack.append(var2 // var1)
            case "mod":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 % var1)
            case "add":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 + var1)
            case "sub":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 - var1)
            case "concat":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 + var1)
            case "lt":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 < var1)
            case "gt":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 > var1)
            case "eq":
                self.__stack.append(self.__stack.pop() == self.__stack.pop())
            case "and":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 and var1)
            case "or":
                var1 = self.__stack.pop()
                var2 = self.__stack.pop()
                self.__stack.append(var2 or var1)
            case "jmp":
                self.__instruction_pointer = self.__instructions.index(f"label {line[1]}")
            case "fjmp":
                if not self.__stack.pop():
                    self.__instruction_pointer = self.__instructions.index(f"label {line[1]}")
            case "read":
                correct = False
                while not correct:
                    try:
                        t_imput =input(f"\033[0;33m:<< ({line[1]}): \033[0m")
                        if line[1] == "B":
                            t_imput = t_imput.lower()
                            if t_imput in ["true", "false"]:
                                self.__stack.append(self.__get_variable_type(line[1], t_imput == "true"))
                            else:
                                raise ValueError()
                        else:
                            self.__stack.append(self.__get_variable_type(line[1], t_imput))
                        correct = True
                    except ValueError:
                        print("\033[1;31m:>>\033[0;31m Invalid input\033[0m")
                    except KeyboardInterrupt:
                        print("\n\033[1;31m:>>\033[0;31m Keyboard interrupt\033[0m")
                        exit(1)
            

    def __get_variable_type(self, var_type, var_value):
        match var_type:
            case "I":
                return int(var_value)
            case "F":
                return float(var_value)
            case "S":
                if var_value[0] and var_value[-1] in ['"']:
                    return var_value[1: len(var_value) - 1].strip()
                else:
                    return var_value
            case "B":
                return var_value == "true"