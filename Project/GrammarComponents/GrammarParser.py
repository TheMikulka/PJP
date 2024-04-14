# Generated from ./GrammarComponents/Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        5,1,42,8,1,10,1,12,1,45,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,56,8,2,1,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,1,
        6,1,6,1,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,100,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,144,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,5,13,168,8,13,10,13,12,13,171,9,13,1,14,1,
        14,1,14,1,14,3,14,177,8,14,1,15,1,15,1,15,0,1,26,16,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,0,3,1,0,19,20,1,0,22,23,1,0,24,29,
        196,0,33,1,0,0,0,2,39,1,0,0,0,4,55,1,0,0,0,6,57,1,0,0,0,8,68,1,0,
        0,0,10,71,1,0,0,0,12,82,1,0,0,0,14,93,1,0,0,0,16,101,1,0,0,0,18,
        104,1,0,0,0,20,110,1,0,0,0,22,112,1,0,0,0,24,116,1,0,0,0,26,143,
        1,0,0,0,28,176,1,0,0,0,30,178,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,
        0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,
        5,0,0,1,38,1,1,0,0,0,39,43,3,4,2,0,40,42,3,4,2,0,41,40,1,0,0,0,42,
        45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,
        0,46,56,3,10,5,0,47,56,3,12,6,0,48,56,3,8,4,0,49,56,3,6,3,0,50,56,
        3,14,7,0,51,56,3,18,9,0,52,56,3,22,11,0,53,56,3,24,12,0,54,56,5,
        16,0,0,55,46,1,0,0,0,55,47,1,0,0,0,55,48,1,0,0,0,55,49,1,0,0,0,55,
        50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,
        0,56,5,1,0,0,0,57,58,3,28,14,0,58,63,5,37,0,0,59,60,5,17,0,0,60,
        62,5,37,0,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,16,0,0,67,7,1,0,0,0,68,69,
        3,26,13,0,69,70,5,16,0,0,70,9,1,0,0,0,71,72,5,1,0,0,72,77,3,26,13,
        0,73,74,5,17,0,0,74,76,3,26,13,0,75,73,1,0,0,0,76,79,1,0,0,0,77,
        75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,16,
        0,0,81,11,1,0,0,0,82,83,5,2,0,0,83,88,3,26,13,0,84,85,5,17,0,0,85,
        87,3,26,13,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,
        0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,5,16,0,0,92,13,1,0,0,0,93,
        94,5,3,0,0,94,95,5,4,0,0,95,96,3,26,13,0,96,97,3,20,10,0,97,99,3,
        4,2,0,98,100,3,16,8,0,99,98,1,0,0,0,99,100,1,0,0,0,100,15,1,0,0,
        0,101,102,5,5,0,0,102,103,3,4,2,0,103,17,1,0,0,0,104,105,5,6,0,0,
        105,106,5,4,0,0,106,107,3,26,13,0,107,108,3,20,10,0,108,109,3,4,
        2,0,109,19,1,0,0,0,110,111,5,7,0,0,111,21,1,0,0,0,112,113,5,8,0,
        0,113,114,3,2,1,0,114,115,5,9,0,0,115,23,1,0,0,0,116,117,5,10,0,
        0,117,118,5,4,0,0,118,119,3,26,13,0,119,120,5,16,0,0,120,121,3,26,
        13,0,121,122,5,16,0,0,122,123,3,26,13,0,123,124,5,7,0,0,124,125,
        3,4,2,0,125,25,1,0,0,0,126,127,6,13,-1,0,127,128,5,30,0,0,128,144,
        3,26,13,12,129,130,5,23,0,0,130,144,3,26,13,9,131,144,5,34,0,0,132,
        144,5,33,0,0,133,144,5,35,0,0,134,144,5,36,0,0,135,144,5,37,0,0,
        136,137,5,4,0,0,137,138,3,26,13,0,138,139,5,7,0,0,139,144,1,0,0,
        0,140,141,5,37,0,0,141,142,5,11,0,0,142,144,3,26,13,1,143,126,1,
        0,0,0,143,129,1,0,0,0,143,131,1,0,0,0,143,132,1,0,0,0,143,133,1,
        0,0,0,143,134,1,0,0,0,143,135,1,0,0,0,143,136,1,0,0,0,143,140,1,
        0,0,0,144,169,1,0,0,0,145,146,10,16,0,0,146,147,7,0,0,0,147,168,
        3,26,13,17,148,149,10,15,0,0,149,150,7,1,0,0,150,168,3,26,13,16,
        151,152,10,14,0,0,152,153,5,21,0,0,153,168,3,26,13,15,154,155,10,
        13,0,0,155,156,3,30,15,0,156,157,3,26,13,14,157,168,1,0,0,0,158,
        159,10,11,0,0,159,160,5,31,0,0,160,168,3,26,13,12,161,162,10,10,
        0,0,162,163,5,32,0,0,163,168,3,26,13,11,164,165,10,8,0,0,165,166,
        5,18,0,0,166,168,3,26,13,9,167,145,1,0,0,0,167,148,1,0,0,0,167,151,
        1,0,0,0,167,154,1,0,0,0,167,158,1,0,0,0,167,161,1,0,0,0,167,164,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,27,1,
        0,0,0,171,169,1,0,0,0,172,177,5,12,0,0,173,177,5,13,0,0,174,177,
        5,14,0,0,175,177,5,15,0,0,176,172,1,0,0,0,176,173,1,0,0,0,176,174,
        1,0,0,0,176,175,1,0,0,0,177,29,1,0,0,0,178,179,7,2,0,0,179,31,1,
        0,0,0,11,35,43,55,63,77,88,99,143,167,169,176
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'write'", "'if'", "'('", "'else'", 
                     "'while'", "')'", "'{'", "'}'", "'for'", "'='", "'int'", 
                     "'float'", "'bool'", "'string'", "';'", "','", "'.'", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", 
                      "SEMI", "COMMA", "DOT", "MUL", "DIV", "MOD", "ADD", 
                      "SUB", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", 
                      "GREATER_EQUAL", "NOT", "AND", "OR", "FLOAT", "INT", 
                      "BOOL", "STRING", "IDENTIFIER", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_declaration = 3
    RULE_printExpr = 4
    RULE_readStmt = 5
    RULE_writeStmt = 6
    RULE_if = 7
    RULE_else = 8
    RULE_while = 9
    RULE_basicRPar = 10
    RULE_block = 11
    RULE_for = 12
    RULE_expr = 13
    RULE_primitiveType = 14
    RULE_relationalOp = 15

    ruleNames =  [ "program", "statementList", "statement", "declaration", 
                   "printExpr", "readStmt", "writeStmt", "if", "else", "while", 
                   "basicRPar", "block", "for", "expr", "primitiveType", 
                   "relationalOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    INT_KEYWORD=12
    FLOAT_KEYWORD=13
    BOOL_KEYWORD=14
    STRING_KEYWORD=15
    SEMI=16
    COMMA=17
    DOT=18
    MUL=19
    DIV=20
    MOD=21
    ADD=22
    SUB=23
    EQUAL=24
    NOT_EQUAL=25
    LESS=26
    GREATER=27
    LESS_EQUAL=28
    GREATER_EQUAL=29
    NOT=30
    AND=31
    OR=32
    FLOAT=33
    INT=34
    BOOL=35
    STRING=36
    IDENTIFIER=37
    COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementListContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementListContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statementList()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 267370231134) != 0)):
                    break

            self.state = 37
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = GrammarParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.statement()
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.statement() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readStmt(self):
            return self.getTypedRuleContext(GrammarParser.ReadStmtContext,0)


        def writeStmt(self):
            return self.getTypedRuleContext(GrammarParser.WriteStmtContext,0)


        def printExpr(self):
            return self.getTypedRuleContext(GrammarParser.PrintExprContext,0)


        def declaration(self):
            return self.getTypedRuleContext(GrammarParser.DeclarationContext,0)


        def if_(self):
            return self.getTypedRuleContext(GrammarParser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(GrammarParser.WhileContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def for_(self):
            return self.getTypedRuleContext(GrammarParser.ForContext,0)


        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.readStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.writeStmt()
                pass
            elif token in [4, 23, 30, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.printExpr()
                pass
            elif token in [12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.declaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.if_()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.while_()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.block()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.for_()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.match(GrammarParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(GrammarParser.PrimitiveTypeContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = GrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.primitiveType()
            self.state = 58
            self.match(GrammarParser.IDENTIFIER)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 59
                self.match(GrammarParser.COMMA)
                self.state = 60
                self.match(GrammarParser.IDENTIFIER)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(GrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_printExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)




    def printExpr(self):

        localctx = GrammarParser.PrintExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(GrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)




    def readStmt(self):

        localctx = GrammarParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GrammarParser.T__0)
            self.state = 72
            self.expr(0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 73
                self.match(GrammarParser.COMMA)
                self.state = 74
                self.expr(0)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(GrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_writeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)




    def writeStmt(self):

        localctx = GrammarParser.WriteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_writeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GrammarParser.T__1)
            self.state = 83
            self.expr(0)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 84
                self.match(GrammarParser.COMMA)
                self.state = 85
                self.expr(0)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(GrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def basicRPar(self):
            return self.getTypedRuleContext(GrammarParser.BasicRParContext,0)


        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def else_(self):
            return self.getTypedRuleContext(GrammarParser.ElseContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = GrammarParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GrammarParser.T__2)
            self.state = 94
            self.match(GrammarParser.T__3)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.basicRPar()
            self.state = 97
            self.statement()
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 98
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = GrammarParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(GrammarParser.T__4)
            self.state = 102
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def basicRPar(self):
            return self.getTypedRuleContext(GrammarParser.BasicRParContext,0)


        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = GrammarParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GrammarParser.T__5)
            self.state = 105
            self.match(GrammarParser.T__3)
            self.state = 106
            self.expr(0)
            self.state = 107
            self.basicRPar()
            self.state = 108
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicRParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_basicRPar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicRPar" ):
                listener.enterBasicRPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicRPar" ):
                listener.exitBasicRPar(self)




    def basicRPar(self):

        localctx = GrammarParser.BasicRParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basicRPar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(GrammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(GrammarParser.T__7)
            self.state = 113
            self.statementList()
            self.state = 114
            self.match(GrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMI)
            else:
                return self.getToken(GrammarParser.SEMI, i)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)




    def for_(self):

        localctx = GrammarParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GrammarParser.T__9)
            self.state = 117
            self.match(GrammarParser.T__3)
            self.state = 118
            self.expr(0)
            self.state = 119
            self.match(GrammarParser.SEMI)
            self.state = 120
            self.expr(0)
            self.state = 121
            self.match(GrammarParser.SEMI)
            self.state = 122
            self.expr(0)
            self.state = 123
            self.match(GrammarParser.T__6)
            self.state = 124
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def OR(self):
            return self.getToken(GrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(GrammarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(GrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class NegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(GrammarParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def AND(self):
            return self.getToken(GrammarParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # RelationalOpContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def relationalOp(self):
            return self.getTypedRuleContext(GrammarParser.RelationalOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class StringConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def DOT(self):
            return self.getToken(GrammarParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringConcat" ):
                listener.enterStringConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringConcat" ):
                listener.exitStringConcat(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 127
                self.match(GrammarParser.NOT)
                self.state = 128
                self.expr(12)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(GrammarParser.SUB)
                self.state = 130
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(GrammarParser.INT)
                pass

            elif la_ == 4:
                localctx = GrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = GrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(GrammarParser.BOOL)
                pass

            elif la_ == 6:
                localctx = GrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(GrammarParser.STRING)
                pass

            elif la_ == 7:
                localctx = GrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(GrammarParser.IDENTIFIER)
                pass

            elif la_ == 8:
                localctx = GrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(GrammarParser.T__3)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(GrammarParser.T__6)
                pass

            elif la_ == 9:
                localctx = GrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(GrammarParser.IDENTIFIER)
                self.state = 141
                self.match(GrammarParser.T__10)
                self.state = 142
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 167
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.MulDivContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 145
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 146
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.AddSubContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 148
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 149
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ModContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 151
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 152
                        localctx.op = self.match(GrammarParser.MOD)
                        self.state = 153
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RelationalContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 154
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 155
                        localctx.op = self.relationalOp()
                        self.state = 156
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.AndContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 159
                        localctx.op = self.match(GrammarParser.AND)
                        self.state = 160
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.OrContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 162
                        localctx.op = self.match(GrammarParser.OR)
                        self.state = 163
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.StringConcatContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 165
                        self.match(GrammarParser.DOT)
                        self.state = 166
                        self.expr(9)
                        pass

             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT_KEYWORD(self):
            return self.getToken(GrammarParser.INT_KEYWORD, 0)

        def FLOAT_KEYWORD(self):
            return self.getToken(GrammarParser.FLOAT_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(GrammarParser.BOOL_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(GrammarParser.STRING_KEYWORD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)




    def primitiveType(self):

        localctx = GrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitiveType)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                localctx.type_ = self.match(GrammarParser.INT_KEYWORD)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                localctx.type_ = self.match(GrammarParser.FLOAT_KEYWORD)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                localctx.type_ = self.match(GrammarParser.BOOL_KEYWORD)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                localctx.type_ = self.match(GrammarParser.STRING_KEYWORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(GrammarParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(GrammarParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(GrammarParser.LESS, 0)

        def GREATER(self):
            return self.getToken(GrammarParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(GrammarParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(GrammarParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_relationalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOp" ):
                listener.enterRelationalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOp" ):
                listener.exitRelationalOp(self)




    def relationalOp(self):

        localctx = GrammarParser.RelationalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relationalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




