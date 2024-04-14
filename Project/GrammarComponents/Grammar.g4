grammar Grammar;

/** The start rule; begin parsing here. */
program: statementList+ EOF;

statementList
    : statement (statement)*
    ;

statement
    : readStmt
    | writeStmt
    | printExpr
    | declaration
    | if
    | while
    | block
    | for
    | ';'
    ;

declaration
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';'
    ;

printExpr
    : expr ';'                                    
    ;

readStmt
    : 'read' expr (',' expr)* ';'                       
    ;

writeStmt
    : 'write' expr (',' expr)* ';'                             
    ;

if
    : 'if' '(' expr basicRPar statement (else)?        
    ;

else
    : 'else' statement
    ;

while
    : 'while' '(' expr basicRPar statement
    ;

basicRPar
    : ')'
    ;

block
    : '{' statementList '}'
    ;

for
    : 'for' '(' expr ';' expr ';' expr ')' statement
    ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | expr op=MOD expr                      # mod
    | expr op=relationalOp expr             # relational
    | NOT expr                              # not
    | expr op=AND expr                      # and
    | expr op=OR expr                       # or
    | SUB expr                              # neg
    | expr DOT expr                         # stringConcat
    | INT                                   # int
    | FLOAT                                 # float
    | BOOL                                  # bool
    | STRING                                # string
    | IDENTIFIER                            # id
    | '(' expr ')'                          # parens
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=STRING_KEYWORD
    ;

relationalOp
    : EQUAL
    | NOT_EQUAL
    | LESS
    | GREATER
    | LESS_EQUAL
    | GREATER_EQUAL
    ;



INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD : 'bool';
STRING_KEYWORD : 'string';

SEMI: ';';
COMMA: ',';
DOT: '.';
MUL : '*' ; 
DIV : '/' ;
MOD : '%' ;
ADD : '+' ;
SUB : '-' ;

EQUAL : '==' ;
NOT_EQUAL : '!=' ;
LESS : '<' ;
GREATER : '>' ;
LESS_EQUAL : '<=' ;
GREATER_EQUAL : '>=' ;

NOT : '!' ;
AND : '&&' ;
OR : '||' ;

FLOAT : [0-9]+'.'[0-9]+ ;
INT : ([0-9]+) ;
BOOL : 'true' | 'false' ;
STRING : '"' (~["])* '"' ;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

COMMENT : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ; // toss out whitespace