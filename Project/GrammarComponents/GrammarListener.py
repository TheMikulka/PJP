# Generated from ./GrammarComponents/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#statementList.
    def enterStatementList(self, ctx:GrammarParser.StatementListContext):
        pass

    # Exit a parse tree produced by GrammarParser#statementList.
    def exitStatementList(self, ctx:GrammarParser.StatementListContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#declaration.
    def exitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#printExpr.
    def enterPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#printExpr.
    def exitPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#readStmt.
    def enterReadStmt(self, ctx:GrammarParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#readStmt.
    def exitReadStmt(self, ctx:GrammarParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#writeStmt.
    def enterWriteStmt(self, ctx:GrammarParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#writeStmt.
    def exitWriteStmt(self, ctx:GrammarParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#if.
    def enterIf(self, ctx:GrammarParser.IfContext):
        pass

    # Exit a parse tree produced by GrammarParser#if.
    def exitIf(self, ctx:GrammarParser.IfContext):
        pass


    # Enter a parse tree produced by GrammarParser#else.
    def enterElse(self, ctx:GrammarParser.ElseContext):
        pass

    # Exit a parse tree produced by GrammarParser#else.
    def exitElse(self, ctx:GrammarParser.ElseContext):
        pass


    # Enter a parse tree produced by GrammarParser#while.
    def enterWhile(self, ctx:GrammarParser.WhileContext):
        pass

    # Exit a parse tree produced by GrammarParser#while.
    def exitWhile(self, ctx:GrammarParser.WhileContext):
        pass


    # Enter a parse tree produced by GrammarParser#basicRPar.
    def enterBasicRPar(self, ctx:GrammarParser.BasicRParContext):
        pass

    # Exit a parse tree produced by GrammarParser#basicRPar.
    def exitBasicRPar(self, ctx:GrammarParser.BasicRParContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#for.
    def enterFor(self, ctx:GrammarParser.ForContext):
        pass

    # Exit a parse tree produced by GrammarParser#for.
    def exitFor(self, ctx:GrammarParser.ForContext):
        pass


    # Enter a parse tree produced by GrammarParser#parens.
    def enterParens(self, ctx:GrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by GrammarParser#parens.
    def exitParens(self, ctx:GrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by GrammarParser#mod.
    def enterMod(self, ctx:GrammarParser.ModContext):
        pass

    # Exit a parse tree produced by GrammarParser#mod.
    def exitMod(self, ctx:GrammarParser.ModContext):
        pass


    # Enter a parse tree produced by GrammarParser#or.
    def enterOr(self, ctx:GrammarParser.OrContext):
        pass

    # Exit a parse tree produced by GrammarParser#or.
    def exitOr(self, ctx:GrammarParser.OrContext):
        pass


    # Enter a parse tree produced by GrammarParser#bool.
    def enterBool(self, ctx:GrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by GrammarParser#bool.
    def exitBool(self, ctx:GrammarParser.BoolContext):
        pass


    # Enter a parse tree produced by GrammarParser#string.
    def enterString(self, ctx:GrammarParser.StringContext):
        pass

    # Exit a parse tree produced by GrammarParser#string.
    def exitString(self, ctx:GrammarParser.StringContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment.
    def exitAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#addSub.
    def enterAddSub(self, ctx:GrammarParser.AddSubContext):
        pass

    # Exit a parse tree produced by GrammarParser#addSub.
    def exitAddSub(self, ctx:GrammarParser.AddSubContext):
        pass


    # Enter a parse tree produced by GrammarParser#float.
    def enterFloat(self, ctx:GrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by GrammarParser#float.
    def exitFloat(self, ctx:GrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by GrammarParser#int.
    def enterInt(self, ctx:GrammarParser.IntContext):
        pass

    # Exit a parse tree produced by GrammarParser#int.
    def exitInt(self, ctx:GrammarParser.IntContext):
        pass


    # Enter a parse tree produced by GrammarParser#mulDiv.
    def enterMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass

    # Exit a parse tree produced by GrammarParser#mulDiv.
    def exitMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass


    # Enter a parse tree produced by GrammarParser#neg.
    def enterNeg(self, ctx:GrammarParser.NegContext):
        pass

    # Exit a parse tree produced by GrammarParser#neg.
    def exitNeg(self, ctx:GrammarParser.NegContext):
        pass


    # Enter a parse tree produced by GrammarParser#not.
    def enterNot(self, ctx:GrammarParser.NotContext):
        pass

    # Exit a parse tree produced by GrammarParser#not.
    def exitNot(self, ctx:GrammarParser.NotContext):
        pass


    # Enter a parse tree produced by GrammarParser#and.
    def enterAnd(self, ctx:GrammarParser.AndContext):
        pass

    # Exit a parse tree produced by GrammarParser#and.
    def exitAnd(self, ctx:GrammarParser.AndContext):
        pass


    # Enter a parse tree produced by GrammarParser#relational.
    def enterRelational(self, ctx:GrammarParser.RelationalContext):
        pass

    # Exit a parse tree produced by GrammarParser#relational.
    def exitRelational(self, ctx:GrammarParser.RelationalContext):
        pass


    # Enter a parse tree produced by GrammarParser#id.
    def enterId(self, ctx:GrammarParser.IdContext):
        pass

    # Exit a parse tree produced by GrammarParser#id.
    def exitId(self, ctx:GrammarParser.IdContext):
        pass


    # Enter a parse tree produced by GrammarParser#stringConcat.
    def enterStringConcat(self, ctx:GrammarParser.StringConcatContext):
        pass

    # Exit a parse tree produced by GrammarParser#stringConcat.
    def exitStringConcat(self, ctx:GrammarParser.StringConcatContext):
        pass


    # Enter a parse tree produced by GrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:GrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:GrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#relationalOp.
    def enterRelationalOp(self, ctx:GrammarParser.RelationalOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#relationalOp.
    def exitRelationalOp(self, ctx:GrammarParser.RelationalOpContext):
        pass



del GrammarParser