# Generated from ./GrammarComponents/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,39,241,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,
        20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,
        26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,
        31,1,31,1,31,1,32,4,32,182,8,32,11,32,12,32,183,1,32,1,32,4,32,188,
        8,32,11,32,12,32,189,1,33,4,33,193,8,33,11,33,12,33,194,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,206,8,34,1,35,1,35,5,35,
        210,8,35,10,35,12,35,213,9,35,1,35,1,35,1,36,1,36,5,36,219,8,36,
        10,36,12,36,222,9,36,1,37,1,37,1,37,1,37,5,37,228,8,37,10,37,12,
        37,231,9,37,1,37,1,37,1,38,4,38,236,8,38,11,38,12,38,237,1,38,1,
        38,0,0,39,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,1,0,6,1,0,48,57,1,0,34,34,3,0,65,
        90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,2,0,10,10,13,13,3,0,
        9,10,13,13,32,32,248,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,
        0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,
        0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,
        0,0,1,79,1,0,0,0,3,84,1,0,0,0,5,90,1,0,0,0,7,93,1,0,0,0,9,95,1,0,
        0,0,11,100,1,0,0,0,13,106,1,0,0,0,15,108,1,0,0,0,17,110,1,0,0,0,
        19,112,1,0,0,0,21,116,1,0,0,0,23,118,1,0,0,0,25,122,1,0,0,0,27,128,
        1,0,0,0,29,133,1,0,0,0,31,140,1,0,0,0,33,142,1,0,0,0,35,144,1,0,
        0,0,37,146,1,0,0,0,39,148,1,0,0,0,41,150,1,0,0,0,43,152,1,0,0,0,
        45,154,1,0,0,0,47,156,1,0,0,0,49,159,1,0,0,0,51,162,1,0,0,0,53,164,
        1,0,0,0,55,166,1,0,0,0,57,169,1,0,0,0,59,172,1,0,0,0,61,174,1,0,
        0,0,63,177,1,0,0,0,65,181,1,0,0,0,67,192,1,0,0,0,69,205,1,0,0,0,
        71,207,1,0,0,0,73,216,1,0,0,0,75,223,1,0,0,0,77,235,1,0,0,0,79,80,
        5,114,0,0,80,81,5,101,0,0,81,82,5,97,0,0,82,83,5,100,0,0,83,2,1,
        0,0,0,84,85,5,119,0,0,85,86,5,114,0,0,86,87,5,105,0,0,87,88,5,116,
        0,0,88,89,5,101,0,0,89,4,1,0,0,0,90,91,5,105,0,0,91,92,5,102,0,0,
        92,6,1,0,0,0,93,94,5,40,0,0,94,8,1,0,0,0,95,96,5,101,0,0,96,97,5,
        108,0,0,97,98,5,115,0,0,98,99,5,101,0,0,99,10,1,0,0,0,100,101,5,
        119,0,0,101,102,5,104,0,0,102,103,5,105,0,0,103,104,5,108,0,0,104,
        105,5,101,0,0,105,12,1,0,0,0,106,107,5,41,0,0,107,14,1,0,0,0,108,
        109,5,123,0,0,109,16,1,0,0,0,110,111,5,125,0,0,111,18,1,0,0,0,112,
        113,5,102,0,0,113,114,5,111,0,0,114,115,5,114,0,0,115,20,1,0,0,0,
        116,117,5,61,0,0,117,22,1,0,0,0,118,119,5,105,0,0,119,120,5,110,
        0,0,120,121,5,116,0,0,121,24,1,0,0,0,122,123,5,102,0,0,123,124,5,
        108,0,0,124,125,5,111,0,0,125,126,5,97,0,0,126,127,5,116,0,0,127,
        26,1,0,0,0,128,129,5,98,0,0,129,130,5,111,0,0,130,131,5,111,0,0,
        131,132,5,108,0,0,132,28,1,0,0,0,133,134,5,115,0,0,134,135,5,116,
        0,0,135,136,5,114,0,0,136,137,5,105,0,0,137,138,5,110,0,0,138,139,
        5,103,0,0,139,30,1,0,0,0,140,141,5,59,0,0,141,32,1,0,0,0,142,143,
        5,44,0,0,143,34,1,0,0,0,144,145,5,46,0,0,145,36,1,0,0,0,146,147,
        5,42,0,0,147,38,1,0,0,0,148,149,5,47,0,0,149,40,1,0,0,0,150,151,
        5,37,0,0,151,42,1,0,0,0,152,153,5,43,0,0,153,44,1,0,0,0,154,155,
        5,45,0,0,155,46,1,0,0,0,156,157,5,61,0,0,157,158,5,61,0,0,158,48,
        1,0,0,0,159,160,5,33,0,0,160,161,5,61,0,0,161,50,1,0,0,0,162,163,
        5,60,0,0,163,52,1,0,0,0,164,165,5,62,0,0,165,54,1,0,0,0,166,167,
        5,60,0,0,167,168,5,61,0,0,168,56,1,0,0,0,169,170,5,62,0,0,170,171,
        5,61,0,0,171,58,1,0,0,0,172,173,5,33,0,0,173,60,1,0,0,0,174,175,
        5,38,0,0,175,176,5,38,0,0,176,62,1,0,0,0,177,178,5,124,0,0,178,179,
        5,124,0,0,179,64,1,0,0,0,180,182,7,0,0,0,181,180,1,0,0,0,182,183,
        1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,187,
        5,46,0,0,186,188,7,0,0,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,66,1,0,0,0,191,193,7,0,0,0,192,191,1,
        0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,68,1,0,
        0,0,196,197,5,116,0,0,197,198,5,114,0,0,198,199,5,117,0,0,199,206,
        5,101,0,0,200,201,5,102,0,0,201,202,5,97,0,0,202,203,5,108,0,0,203,
        204,5,115,0,0,204,206,5,101,0,0,205,196,1,0,0,0,205,200,1,0,0,0,
        206,70,1,0,0,0,207,211,5,34,0,0,208,210,8,1,0,0,209,208,1,0,0,0,
        210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,
        213,211,1,0,0,0,214,215,5,34,0,0,215,72,1,0,0,0,216,220,7,2,0,0,
        217,219,7,3,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,
        220,221,1,0,0,0,221,74,1,0,0,0,222,220,1,0,0,0,223,224,5,47,0,0,
        224,225,5,47,0,0,225,229,1,0,0,0,226,228,8,4,0,0,227,226,1,0,0,0,
        228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,
        231,229,1,0,0,0,232,233,6,37,0,0,233,76,1,0,0,0,234,236,7,5,0,0,
        235,234,1,0,0,0,236,237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,
        238,239,1,0,0,0,239,240,6,38,0,0,240,78,1,0,0,0,9,0,183,189,194,
        205,211,220,229,237,1,6,0,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    INT_KEYWORD = 12
    FLOAT_KEYWORD = 13
    BOOL_KEYWORD = 14
    STRING_KEYWORD = 15
    SEMI = 16
    COMMA = 17
    DOT = 18
    MUL = 19
    DIV = 20
    MOD = 21
    ADD = 22
    SUB = 23
    EQUAL = 24
    NOT_EQUAL = 25
    LESS = 26
    GREATER = 27
    LESS_EQUAL = 28
    GREATER_EQUAL = 29
    NOT = 30
    AND = 31
    OR = 32
    FLOAT = 33
    INT = 34
    BOOL = 35
    STRING = 36
    IDENTIFIER = 37
    COMMENT = 38
    WS = 39

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'read'", "'write'", "'if'", "'('", "'else'", "'while'", "')'", 
            "'{'", "'}'", "'for'", "'='", "'int'", "'float'", "'bool'", 
            "'string'", "';'", "','", "'.'", "'*'", "'/'", "'%'", "'+'", 
            "'-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'!'", 
            "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", 
            "SEMI", "COMMA", "DOT", "MUL", "DIV", "MOD", "ADD", "SUB", "EQUAL", 
            "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
            "NOT", "AND", "OR", "FLOAT", "INT", "BOOL", "STRING", "IDENTIFIER", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "INT_KEYWORD", "FLOAT_KEYWORD", 
                  "BOOL_KEYWORD", "STRING_KEYWORD", "SEMI", "COMMA", "DOT", 
                  "MUL", "DIV", "MOD", "ADD", "SUB", "EQUAL", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "NOT", 
                  "AND", "OR", "FLOAT", "INT", "BOOL", "STRING", "IDENTIFIER", 
                  "COMMENT", "WS" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


