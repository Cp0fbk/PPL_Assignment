// ID: 2212631
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//3.4 keywords
AUTO: 'auto';
BREAK: 'break';
BOOL: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'function';
IF: 'if';
INT: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

//3.5 operators 
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%'; 
NOT: '!'; AND: '&&'; OR: '||'; EQ: '=='; NOT_EQ: '!=';
LT: '<'; LTE: '<='; GT: '>'; GTE: '>='; CONCAT: '::';

//3.6 seperators 
LB: '('; RB: ')'; LS: '['; RS: ']'; LP: '{'; RP: '}';
DOT: '.'; COMMA: ','; SEMI: ';'; COLON: ':'; ASSIGN: '=';


// 3.3 identifiers
ID: ([a-zA-Z] |'_') ([a-zA-Z] | '_' | [0-9])*;


//3.7 literals
INTLIT: ('0' | [1-9] [0-9]* ('_' [0-9]+)*) {self.text = self.text.replace("_", "")};

FLOATLIT: INTpart DEC EXP {self.text = self.text.replace("_", "")} 
    | INTpart DEC {self.text = self.text.replace("_", "")}
    | INTpart EXP {self.text = self.text.replace("_", "")}
    | DEC EXP {self.text = self.text.replace("_", "")};

boollit: 'true' | 'false';

STRINGLIT: '"' STR* '"' {self.text = self.text[1:-1]};

fragment INTpart: INTLIT;
fragment DEC: '.' [0-9]*;
fragment EXP: [eE] [+-]? [0-9]+;

fragment STR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\"' | '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\';
fragment ESC_ILL: '\\' ~[bfrnt'\\] | '\'' ~'"';

arraylit: LP exprlist RP;
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;


literal: INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit;


// Comment
COMMENTS: (('//' ~[\n]*) | ('/*' .*? '*/')) -> skip; // Comments
WS : [ \t\r\f\b\n]+ -> skip ; // skip spaces, tabs

// Error
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR* ('\n' | '\r\n' | EOF) {
	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' STR* ESC_ILL {
	raise IllegalEscape(self.text[1:])
};

//-----------------------------------------------------------Parser-----------------------------------------------------------------------


program: decllist  EOF ;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;


//5.1 Variable declarations 
//5.1.1 variables
vardecl: (shortform | init) SEMI;
shortform: idlist COLON typee;
init: ID varlist expr;
varlist: COMMA ID varlist expr COMMA | COLON typee ASSIGN;
idlist: ID COMMA idlist | ID;



//5.1.2 parameter
param: INHERIT? OUT? ID COLON typee;

//5.2 Function declarations
funcdecl: ID COLON FUNC func_type LB paramlist RB (INHERIT ID)? block_statement;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;


//6.5 index operators
index_op: ID LS exprprime RS;

// 6.6 function call
func_call: ID LB arglist RB;
arglist: argprime | ;
argprime: expr COMMA argprime | expr;


expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQ | NOT_EQ | LT | GT | LTE | GTE) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: index_op | expr8;
expr8: ID | literal | LB expr RB | ID LB exprlist RB;

//7 statements
statement: (assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement 
            | block_statement | while_statement | do_while_statement);

assignment_statement: scalar ASSIGN expr SEMI;
scalar: ID | index_op;

if_statement: IF LB expr RB statement else_st;
else_st: ELSE statement | ;

for_statement: FOR LB scalar ASSIGN init_expr COMMA expr COMMA expr RB statement;
init_expr: init_expr (ADD | SUB) init_expr1 | init_expr1;
init_expr1: init_expr1 (MUL | DIV | MOD) init_expr2 | init_expr2;
init_expr2: SUB init_expr2 | init_expr3;
init_expr3:  LB expr RB | INTLIT;

while_statement: WHILE LB expr RB statement;

do_while_statement: DO block_statement WHILE LB expr RB SEMI;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

return_statement: RETURN expr? SEMI;

call_statement: spec_func SEMI | func_call SEMI;

block_statement: LP blist RP;
blist: statement blist | vardecl blist | ;


//4.1
typee: BOOL | INT | FLOAT | STRING | AUTO | array_type;
elem_type: INT | FLOAT | STRING | BOOL;
array_type: ARRAY LS dimen RS OF elem_type;
dimen: INTLIT COMMA dimen | INTLIT;
func_type: BOOL | INT | FLOAT | STRING | AUTO | array_type | VOID;

//8 special function
spec_func: readI| printI | readF | writeF | readB | printB | readS | printS | superr | preventD;

readI: READI LB RB;
printI: PRINTI LB expr RB;
readF: READF LB RB;
writeF: WRITEF LB expr RB;
readB: READB LB RB;
printB: PRINTB LB expr RB;
readS: READS LB RB;
printS: PRINTS LB expr RB;
superr: SUPER LB exprlist RB;
preventD: PREVENTDEFAULT LB RB;


//8 special function
READI: 'readInteger';
PRINTI: 'printInteger';
READF: 'readFloat';
READB: 'readBoolean';
PRINTB: 'printBoolean';
READS: 'readString';
PRINTS: 'printString';
WRITEF: 'writeFloat';
SUPER: 'super';
PREVENTDEFAULT: 'preventDefault';

