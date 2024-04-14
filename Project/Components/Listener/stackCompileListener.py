import sys
from antlr4 import *
from GrammarComponents.GrammarParser import GrammarParser
from GrammarComponents.GrammarListener import GrammarListener

class stackCompileListener(GrammarListener):
    def __init__(self, output_file):
        self.output_file = output_file
        self.stack = []
        self.blocks = [{}]
        self.__clear_file()
        self.needConvertIntToFloat = False
        self.index = 0

    def write_to_file(self, text):
        with open(self.output_file, 'a') as file:
            file.write(f"{text}\n")

    def __clear_file(self):
        with open(self.output_file, 'w') as file:
            file.write("")
    
    def getAllBlocks(self):
        blocks = {}
        for block in self.blocks:
            for key in block:
                blocks[key] = block[key]
        return blocks
    
    def enterBlock(self, ctx: GrammarParser.BlockContext):
        self.blocks.append({})

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        self.blocks.pop()

    def getRuleType(self, ctx):
        rule = type(ctx).__name__.replace("Context", "").lower()
        match type(ctx):
            case GrammarParser.IdContext:
                rule = self.getAllBlocks()[ctx.getText()]
            case GrammarParser.AddSubContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                rule = "int" if leftType == "int" and rightType == "int" else "float"
            case GrammarParser.MulDivContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                rule = "int" if leftType == "int" and rightType == "int" else "float"
            case GrammarParser.ModContext:
                rule = "int"
            case GrammarParser.NegContext:
                valueType = self.getRuleType(ctx.expr())
                rule = valueType
            case GrammarParser.NotContext:
                valueType = self.getRuleType(ctx.expr())
                rule = valueType
            case GrammarParser.AndContext:
                rule = "bool"
            case GrammarParser.OrContext:
                rule = "bool"
            case GrammarParser.RelationalContext:
                rule = "bool"
            case GrammarParser.ParensContext:
                rule = self.getRuleType(ctx.expr())
        return rule

    def exitString(self, ctx: GrammarParser.StringContext):
        self.write_to_file(f"push S {ctx.getText()}")
        
    def exitInt(self, ctx:GrammarParser.IntContext):
        self.write_to_file(f"push I {ctx.getText()}")
        if self.needConvertIntToFloat:
            self.write_to_file(f"itof")
            self.needConvertIntToFloat = False

    def exitFloat(self, ctx:GrammarParser.FloatContext):
        self.write_to_file(f"push F {ctx.getText()}")
    
    def exitBool(self, ctx:GrammarParser.BoolContext):
        self.write_to_file(f"push B {ctx.getText()}")

    def exitWriteStmt(self, ctx: GrammarParser.WriteStmtContext):
        self.write_to_file(f"print {len(ctx.expr())}")
    
    def exitReadStmt(self, ctx: GrammarParser.ReadStmtContext):
            for i in range(len(ctx.expr())):
                expr = ctx.expr(i)
                expr_t = self.getRuleType(expr)
                match expr_t:
                    case "int":
                        self.write_to_file(f"read I")
                        self.write_to_file(f"save {expr.IDENTIFIER()}")
                    case "float":
                        self.write_to_file(f"read F")
                        self.write_to_file(f"save {expr.IDENTIFIER()}")
                    case "string":
                        self.write_to_file(f"read S")
                        self.write_to_file(f"save {expr.IDENTIFIER()}")
                    case "bool":
                        self.write_to_file(f"read B")
                        self.write_to_file(f"save {expr.IDENTIFIER()}")
                    case _:
                        self.write_to_file(f"read I")
                        self.write_to_file(f"save {expr.IDENTIFIER()}")


    def exitId (self, ctx: GrammarParser.IdContext):
        if (type(ctx.parentCtx) is not GrammarParser.ReadStmtContext):
            self.write_to_file(f"load {str(ctx.IDENTIFIER())}")

    def exitNeg(self, ctx: GrammarParser.NegContext):
        self.write_to_file(f"uminus")

    def exitNot(self, ctx: GrammarParser.NotContext):
        self.write_to_file(f"not")
    
    def enterMulDiv(self, ctx: GrammarParser.MulDivContext):
        left = self.getRuleType(ctx.expr(0))
        right = self.getRuleType(ctx.expr(1))

        if(left == "int" and right == "float") or (left == "float" and right == "int"):
           self.needConvertIntToFloat = True

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        if(ctx.op.text == "*"):
            self.write_to_file(f"mul")
        else:
            self.write_to_file(f"div")

    def enterAddSub(self, ctx: GrammarParser.AddSubContext):
        left = self.getRuleType(ctx.expr(0))
        right = self.getRuleType(ctx.expr(1))

        if(left == "int" and right == "float") or (left == "float" and right == "int"):
            self.needConvertIntToFloat = True

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        if(ctx.op.text == "+"):
            self.write_to_file(f"add")
        else:
            self.write_to_file(f"sub")

    def exitMod(self, ctx: GrammarParser.ModContext):
        self.write_to_file(f"mod")

    def exitStringConcat(self, ctx: GrammarParser.StringConcatContext):
        self.write_to_file(f"concat")
    
    def exitAnd(self, ctx: GrammarParser.AndContext):
        self.write_to_file(f"and")

    def exitOr(self, ctx: GrammarParser.OrContext):
        self.write_to_file(f"or")

    def enterIf(self, ctx: GrammarParser.IfContext):
        pass

    def enterRelational(self, ctx: GrammarParser.RelationalContext):
        left = self.getRuleType(ctx.expr(0))
        right = self.getRuleType(ctx.expr(1))

        if(left == "int" and right == "float") or (left == "float" and right == "int"):
            self.needConvertIntToFloat = True
    
    def exitBasicRPar(self, ctx: GrammarParser.BasicRParContext):
        match type(ctx.parentCtx):
            case GrammarParser.IfContext:
                self.write_to_file(f"fjmp {self.index}")
                self.index += 1
            case GrammarParser.WhileContext:
                self.index += 1
                self.write_to_file(f"fjmp {self.index}")

    def exitIf(self, ctx: GrammarParser.IfContext):
        if ctx.else_() is None:
            self.write_to_file(f"jmp {self.index}")
            self.write_to_file(f"label {self.index - 1}")
            self.write_to_file(f"label {self.index}")
            self.index += 1


    def enterElse(self, ctx: GrammarParser.ElseContext):
        self.write_to_file(f"jmp {self.index}")
        self.write_to_file(f"label {self.index -1}")
        self.index += 1

    def exitElse(self, ctx: GrammarParser.ElseContext):
        self.write_to_file(f"label {self.index -1}")
    
    def enterWhile(self, ctx: GrammarParser.WhileContext):
        self.write_to_file(f"label {self.index}")

    def exitWhile(self, ctx: GrammarParser.WhileContext):
        self.write_to_file(f"jmp {self.index - 1}")
        self.write_to_file(f"label {self.index}")
        self.index += 1
    


    def exitRelational(self, ctx: GrammarParser.RelationalContext):
        if(ctx.op.getText() == "<"):
            self.write_to_file(f"lt")
        elif(ctx.op.getText() == "<="):
            self.write_to_file(f"le")
        elif(ctx.op.getText() == ">"):
            self.write_to_file(f"gt")
        elif(ctx.op.getText() == ">="):
            self.write_to_file(f"ge")
        elif(ctx.op.getText() == "=="):
            self.write_to_file(f"eq")
        elif(ctx.op.getText() == "!="):
            self.write_to_file(f"eq")
            self.write_to_file(f"not")

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        for i in range(len(ctx.IDENTIFIER())):
            name = ctx.IDENTIFIER(i)
            type = ctx.primitiveType()         
            match type.getText():
                case "int":
                    self.write_to_file(f"push I 0")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "float":
                    self.write_to_file(f"push F 0.0")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "string":
                    self.write_to_file(f"push S \"\"")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "bool":
                    self.write_to_file(f"push B false")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())

            self.write_to_file(f"save {name.getText()}")  

    def enterAssignment(self, ctx: GrammarParser.AssignmentContext):
        name = ctx.IDENTIFIER()
        dec_t = self.getAllBlocks()[name.getText()]
        expr_t = self.getRuleType(ctx.expr())

        if dec_t == "float" and expr_t == "int":
            self.needConvertIntToFloat = True
    
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        name = ctx.IDENTIFIER()

        self.write_to_file(f"save {name.getText()}")

        self.write_to_file(f"load {name.getText()}")

        if ctx.parentCtx.getChild(0) == ctx: 
            self.write_to_file(f"pop")