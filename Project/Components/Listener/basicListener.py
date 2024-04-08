import sys
from antlr4 import *
from GrammarComponents.GrammarLexer import GrammarLexer
from GrammarComponents.GrammarParser import GrammarParser
from GrammarComponents.GrammarListener import GrammarListener

class basicListener(GrammarListener):
    def __init__(self):
        self.values = {}
        self.blocks = [{}]
        self.errors = []

    def getAllBlocks(self):
        blocks = {}
        for block in self.blocks:
            for key in block:
                blocks[key] = block[key]
        return blocks
    
    def getBlockWithKey(self, key):
        for block in self.blocks:
            if key in block:
                return block
        return None
    
    
    def getRuleType(self, ctx:ParserRuleContext):
        rule = type(ctx).__name__.replace("Context", "").lower()
        match type(ctx):
            case GrammarParser.IdContext:
                rule = self.getAllBlocks()[ctx.getText()][0]
            case GrammarParser.AddSubContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                    self.errors.append(f"\n\033[1;31mError: Add/Sub requires int, float types, but got {leftType} Add/Sub {rightType}\033[0m")
                rule = "int" if leftType == "int" and rightType == "int" else "float"
            case GrammarParser.MulDivContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                    self.errors.append(f"\n\033[1;31mError: Mul/Div requires int, float types, but got {leftType} Mul/Div {rightType}\033[0m")
                rule = "int" if leftType == "int" and rightType == "int" else "float"
            case GrammarParser.ModContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                if leftType != "int" or rightType != "int":
                    self.errors.append(f"\n\033[1;31mError: Mod requires int types, but got {leftType} Mod {rightType}\033[0m")
                rule = "int"
            case GrammarParser.NegContext:
                valueType = self.getRuleType(ctx.expr())
                if valueType != "int" and valueType != "float":
                   self.errors.append(f"\n\033[1;31mError: Neg requires int and float types, but got {valueType}\033[0m")
                rule = valueType
            case GrammarParser.NotContext:
                valueType = self.getRuleType(ctx.expr())
                if valueType != "bool":
                    self.errors.append(f"\n\033[1;31mError: Not requires bool types, but got {valueType}\033[0m")
                rule = valueType
            case GrammarParser.AndContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                if leftType != "bool" or rightType != "bool":
                    self.errors.append(f"\n\033[1;31mError: And requires bool types, but got {leftType} And {rightType}\033[0m")
                rule = "bool"
            case GrammarParser.OrContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                if leftType != "bool" or rightType != "bool":
                    self.errors.append(f"\n\033[1;31mError: Or requires bool types, but got {leftType} Or {rightType}\033[0m")
                rule = "bool"
            case GrammarParser.RelationalContext:
                leftType = self.getRuleType(ctx.expr(0))
                rightType = self.getRuleType(ctx.expr(1))
                operator = ctx.op.getText()
                match operator:
                    case "==":
                        if leftType not in ["int", "float", "string"] or rightType not in ["int", "float", "string"]:
                            self.errors.append(f"\n\033[1;31mError: == requires int,float,string types, but got {leftType} == {rightType}\033[0m")
                        if leftType != rightType:
                            self.errors.append(f"\n\033[1;31mError: == requires int,float,string types, but got {leftType} == {rightType}\033[0m")
                    case "!=":
                        if leftType not in ["int", "float", "string"] or rightType not in ["int", "float", "string"]:
                            self.errors.append(f"\n\033[1;31mError: != requires int,float,string types, but got {leftType} != {rightType}\033[0m")
                    case ">":
                        if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                            self.errors.append(f"\n\033[1;31mError: > requires int,float type, but got {leftType} > {rightType}\033[0m")
                    case "<":
                        if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                            self.errors.append(f"\n\033[1;31mError: < requires int,float type, but got {leftType} < {rightType}\033[0m")
                    case ">=":
                        if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                            self.errors.append(f"\n\033[1;31mError: >= requires int,float type, but got {leftType} >= {rightType}\033[0m")
                    case "<=":
                        if leftType not in ["int", "float"] or rightType not in ["int", "float"]:
                            self.errors.append(f"\n\033[1;31mError: <= requires int,float type, but got {leftType} <= {rightType}\033[0m")
                rule = "bool"
            case GrammarParser.ParensContext:
                rule = self.getRuleType(ctx.expr())
            
        return rule
    
    def enterBlock(self, ctx: GrammarParser.BlockContext):
        self.blocks.append({})

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        self.blocks.pop()

    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        name = ctx.IDENTIFIER()

        expr = None
        while True:
            if expr is None:
                expr = ctx.expr()
            else:
                expr = expr.expr()

            if type(expr).__name__.replace("Context", "").lower() != "assignment":
                break

        value = expr
        valueType = self.getRuleType(value)
        block = self.getBlockWithKey(str(name))
        # self.values[str(name)] = value.getText()
        
        if block is None:
            self.errors.append(f"\n\033[1;31mError: \"{name}\" is not declared\033[0m")
            return
        
        declaration_type = block[str(name)][0]

        wasFloat = False
        if valueType != declaration_type:
            if valueType == "int" and declaration_type == "float":
                valueType = "float"
                wasFloat = True
            else:
                self.errors.append(f"\n\033[1;31mError: \"{name}\" is type {declaration_type}, but got {valueType}\033[0m")
                return
        
        if str(value.getText()).isdecimal() and declaration_type == "float":
            block[str(name)] = (str(declaration_type),float(value.getText()))
        else:
            block[str(name)] = (str(declaration_type),value.getText())
    
    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        for i in range(len(ctx.IDENTIFIER())):
            name = ctx.IDENTIFIER(i)
            type = ctx.primitiveType()

            if str(name) in self.getAllBlocks():
                self.errors.append(f"\n\033[1;31mError: \"{name}\" already declared\033[0m")
            else:
                match type.getText():
                    case "int":
                        self.blocks[len(self.blocks) - 1][str(name)] = (type.getText(),0)
                    case "float":
                        self.blocks[len(self.blocks) - 1][str(name)] = (type.getText(),0.0)
                    case "string":
                        self.blocks[len(self.blocks) - 1][str(name)] = (type.getText(),"")
                    case "bool":
                        self.blocks[len(self.blocks) - 1][str(name)] = (type.getText(),False)
    
    def exitStringConcat(self, ctx: GrammarParser.StringConcatContext):
        value_left = ctx.expr(0)
        value_right = ctx.expr(1)
        valueType_left = type(value_left).__name__.replace("Context", "").lower()
        valueType_right = type(value_right).__name__.replace("Context", "").lower()

        if valueType_left != "string" or valueType_right != "string":
            self.errors.append(f"\n\033[1;31mError: String concatenation requires strings type, but got {valueType_left} Dot {valueType_right}\033[0m")

    def exitWhile(self, ctx: GrammarParser.WhileContext):
        value = ctx.expr()
        valueType = self.getRuleType(value)
        if valueType != "bool":
            self.errors.append(f"\n\033[1;31mError: While requires bool type, but got {valueType}\033[0m")
    
    def exitIf(self, ctx: GrammarParser.IfContext):
        value = ctx.expr()
        valueType = self.getRuleType(value)
        if valueType != "bool":
            self.errors.append(f"\n\033[1;31mError: If requires bool type, but got {valueType}\033[0m")
    
    def exitFor(self, ctx: GrammarParser.ForContext):
        valueType = self.getRuleType(ctx.expr(0))
        valueType1 = self.getRuleType(ctx.expr(1))
        valueType2 = self.getRuleType(ctx.expr(2))
        print(valueType, valueType1, valueType2)
        if valueType1 != "bool":
            self.errors.append(f"\n\033[1;31mError: For requires bool type, but got {valueType2}\033[0m")

    def exitEveryRule(self, ctx):
        self.getRuleType(ctx)

    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        for error in self.errors:
            print(error)

        if len(self.errors) > 0:
            exit(1)

