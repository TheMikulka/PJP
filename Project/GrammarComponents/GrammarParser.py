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
        4,1,38,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,5,3,55,
        8,3,10,3,12,3,58,9,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,69,
        8,5,10,5,12,5,72,9,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,80,8,6,10,6,12,
        6,83,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,123,8,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,147,8,10,10,
        10,12,10,150,9,10,1,11,1,11,1,11,1,11,3,11,156,8,11,1,12,1,12,1,
        12,0,1,20,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,3,1,0,18,19,1,0,
        21,22,1,0,23,28,177,0,27,1,0,0,0,2,33,1,0,0,0,4,48,1,0,0,0,6,50,
        1,0,0,0,8,61,1,0,0,0,10,64,1,0,0,0,12,75,1,0,0,0,14,86,1,0,0,0,16,
        95,1,0,0,0,18,101,1,0,0,0,20,122,1,0,0,0,22,155,1,0,0,0,24,157,1,
        0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,
        30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,37,3,4,2,
        0,34,36,3,4,2,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,3,1,0,0,0,39,37,1,0,0,0,40,49,3,10,5,0,41,49,3,12,6,0,
        42,49,3,8,4,0,43,49,3,6,3,0,44,49,3,14,7,0,45,49,3,16,8,0,46,49,
        3,18,9,0,47,49,5,15,0,0,48,40,1,0,0,0,48,41,1,0,0,0,48,42,1,0,0,
        0,48,43,1,0,0,0,48,44,1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,
        1,0,0,0,49,5,1,0,0,0,50,51,3,22,11,0,51,56,5,36,0,0,52,53,5,16,0,
        0,53,55,5,36,0,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,
        1,0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,15,0,0,60,7,1,0,0,0,
        61,62,3,20,10,0,62,63,5,15,0,0,63,9,1,0,0,0,64,65,5,1,0,0,65,70,
        3,20,10,0,66,67,5,16,0,0,67,69,3,20,10,0,68,66,1,0,0,0,69,72,1,0,
        0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,74,
        5,15,0,0,74,11,1,0,0,0,75,76,5,2,0,0,76,81,5,35,0,0,77,78,5,16,0,
        0,78,80,3,20,10,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,15,0,0,85,13,1,0,0,0,
        86,87,5,3,0,0,87,88,5,4,0,0,88,89,3,20,10,0,89,90,5,5,0,0,90,93,
        3,4,2,0,91,92,5,6,0,0,92,94,3,4,2,0,93,91,1,0,0,0,93,94,1,0,0,0,
        94,15,1,0,0,0,95,96,5,7,0,0,96,97,5,4,0,0,97,98,3,20,10,0,98,99,
        5,5,0,0,99,100,3,4,2,0,100,17,1,0,0,0,101,102,5,8,0,0,102,103,3,
        2,1,0,103,104,5,9,0,0,104,19,1,0,0,0,105,106,6,10,-1,0,106,107,5,
        29,0,0,107,123,3,20,10,12,108,109,5,22,0,0,109,123,3,20,10,9,110,
        123,5,33,0,0,111,123,5,32,0,0,112,123,5,34,0,0,113,123,5,35,0,0,
        114,123,5,36,0,0,115,116,5,4,0,0,116,117,3,20,10,0,117,118,5,5,0,
        0,118,123,1,0,0,0,119,120,5,36,0,0,120,121,5,10,0,0,121,123,3,20,
        10,1,122,105,1,0,0,0,122,108,1,0,0,0,122,110,1,0,0,0,122,111,1,0,
        0,0,122,112,1,0,0,0,122,113,1,0,0,0,122,114,1,0,0,0,122,115,1,0,
        0,0,122,119,1,0,0,0,123,148,1,0,0,0,124,125,10,16,0,0,125,126,7,
        0,0,0,126,147,3,20,10,17,127,128,10,15,0,0,128,129,7,1,0,0,129,147,
        3,20,10,16,130,131,10,14,0,0,131,132,5,20,0,0,132,147,3,20,10,15,
        133,134,10,13,0,0,134,135,3,24,12,0,135,136,3,20,10,14,136,147,1,
        0,0,0,137,138,10,11,0,0,138,139,5,30,0,0,139,147,3,20,10,12,140,
        141,10,10,0,0,141,142,5,31,0,0,142,147,3,20,10,11,143,144,10,8,0,
        0,144,145,5,17,0,0,145,147,3,20,10,9,146,124,1,0,0,0,146,127,1,0,
        0,0,146,130,1,0,0,0,146,133,1,0,0,0,146,137,1,0,0,0,146,140,1,0,
        0,0,146,143,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,
        0,0,149,21,1,0,0,0,150,148,1,0,0,0,151,156,5,11,0,0,152,156,5,12,
        0,0,153,156,5,13,0,0,154,156,5,14,0,0,155,151,1,0,0,0,155,152,1,
        0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,23,1,0,0,0,157,158,7,2,
        0,0,158,25,1,0,0,0,11,29,37,48,56,70,81,93,122,146,148,155
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'write'", "'if'", "'('", "')'", 
                     "'else'", "'while'", "'{'", "'}'", "'='", "'int'", 
                     "'float'", "'bool'", "'string'", "';'", "','", "'.'", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT_KEYWORD", 
                      "FLOAT_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", 
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
    RULE_while = 8
    RULE_block = 9
    RULE_expr = 10
    RULE_primitiveType = 11
    RULE_relationalOp = 12

    ruleNames =  [ "program", "statementList", "statement", "declaration", 
                   "printExpr", "readStmt", "writeStmt", "if", "while", 
                   "block", "expr", "primitiveType", "relationalOp" ]

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
    INT_KEYWORD=11
    FLOAT_KEYWORD=12
    BOOL_KEYWORD=13
    STRING_KEYWORD=14
    SEMI=15
    COMMA=16
    DOT=17
    MUL=18
    DIV=19
    MOD=20
    ADD=21
    SUB=22
    EQUAL=23
    NOT_EQUAL=24
    LESS=25
    GREATER=26
    LESS_EQUAL=27
    GREATER_EQUAL=28
    NOT=29
    AND=30
    OR=31
    FLOAT=32
    INT=33
    BOOL=34
    STRING=35
    IDENTIFIER=36
    COMMENT=37
    WS=38

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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statementList()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 133685115294) != 0)):
                    break

            self.state = 31
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
            self.state = 33
            self.statement()
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.statement() 
                self.state = 39
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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.readStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.writeStmt()
                pass
            elif token in [4, 22, 29, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.printExpr()
                pass
            elif token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.declaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.if_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.while_()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.block()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 47
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
            self.state = 50
            self.primitiveType()
            self.state = 51
            self.match(GrammarParser.IDENTIFIER)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 52
                self.match(GrammarParser.COMMA)
                self.state = 53
                self.match(GrammarParser.IDENTIFIER)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
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
            self.state = 61
            self.expr(0)
            self.state = 62
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
            self.state = 64
            self.match(GrammarParser.T__0)
            self.state = 65
            self.expr(0)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 66
                self.match(GrammarParser.COMMA)
                self.state = 67
                self.expr(0)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
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

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


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
            self.state = 75
            self.match(GrammarParser.T__1)
            self.state = 76
            self.match(GrammarParser.STRING)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 77
                self.match(GrammarParser.COMMA)
                self.state = 78
                self.expr(0)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


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
            self.state = 86
            self.match(GrammarParser.T__2)
            self.state = 87
            self.match(GrammarParser.T__3)
            self.state = 88
            self.expr(0)
            self.state = 89
            self.match(GrammarParser.T__4)
            self.state = 90
            self.statement()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(GrammarParser.T__5)
                self.state = 92
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
        self.enterRule(localctx, 16, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(GrammarParser.T__6)
            self.state = 96
            self.match(GrammarParser.T__3)
            self.state = 97
            self.expr(0)
            self.state = 98
            self.match(GrammarParser.T__4)
            self.state = 99
            self.statement()
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
        self.enterRule(localctx, 18, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(GrammarParser.T__7)
            self.state = 102
            self.statementList()
            self.state = 103
            self.match(GrammarParser.T__8)
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 106
                self.match(GrammarParser.NOT)
                self.state = 107
                self.expr(12)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(GrammarParser.SUB)
                self.state = 109
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(GrammarParser.INT)
                pass

            elif la_ == 4:
                localctx = GrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = GrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(GrammarParser.BOOL)
                pass

            elif la_ == 6:
                localctx = GrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(GrammarParser.STRING)
                pass

            elif la_ == 7:
                localctx = GrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(GrammarParser.IDENTIFIER)
                pass

            elif la_ == 8:
                localctx = GrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(GrammarParser.T__3)
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(GrammarParser.T__4)
                pass

            elif la_ == 9:
                localctx = GrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(GrammarParser.IDENTIFIER)
                self.state = 120
                self.match(GrammarParser.T__9)
                self.state = 121
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 146
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.MulDivContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 124
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 125
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.AddSubContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 127
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 128
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 129
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ModContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 131
                        localctx.op = self.match(GrammarParser.MOD)
                        self.state = 132
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RelationalContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 134
                        localctx.op = self.relationalOp()
                        self.state = 135
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.AndContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 137
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 138
                        localctx.op = self.match(GrammarParser.AND)
                        self.state = 139
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.OrContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 140
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 141
                        localctx.op = self.match(GrammarParser.OR)
                        self.state = 142
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.StringConcatContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 143
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 144
                        self.match(GrammarParser.DOT)
                        self.state = 145
                        self.expr(9)
                        pass

             
                self.state = 150
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
        self.enterRule(localctx, 22, self.RULE_primitiveType)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                localctx.type_ = self.match(GrammarParser.INT_KEYWORD)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                localctx.type_ = self.match(GrammarParser.FLOAT_KEYWORD)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                localctx.type_ = self.match(GrammarParser.BOOL_KEYWORD)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
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
        self.enterRule(localctx, 24, self.RULE_relationalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
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
        self._predicates[10] = self.expr_sempred
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
         




