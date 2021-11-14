from typing import DefaultDict
import ply.lex as lex

#Autor: Jhossias Calderon
#Ingreso de palabras reservadas
reserved = {
    'as' : 'AS', 'as?' : 'as?',
    'break' : 'BREAK', 'class' : 'CLASS',
    'continue' : 'CONTINUE', 'do' : 'DO',
    'else' : 'ELSE', 'false' : 'FALSE', 'for' : 'FOR',
    'fun' : 'FUN', 'if' : 'IF', 'in' : 'IN', '!in' : '!IN',
    'interface' : 'INTERFACE', 'is' : 'IS',
    '!is' : '!IS',
    'null' : 'NULL', 'object' : 'OBJECT',
    'package' : 'PACKAGE',
    'return' : 'RETURN', 'super' : 'SUPER', 'this' : 'THIS',
    'throw' : 'THROW',
    'true' : 'TRUE', 'try' : 'TRY',
    'typealias' : 'TYPEALIAS', 'typeof' : 'TYPEOF', 'val' : 'VAL', 'var' : 'VAR',
    'when' : 'WHEN', 'while' : 'WHILE',
    'by' : 'BY',
    'catch' : 'CATCH', 'constructor' : 'CONSTRUCTOR', 'delegate' : 'DELEGATE',
    'dynamic' : 'DYNAMIC', 'field' : 'FIELD',
    'file' : 'FILE',
    'finally' : 'FINALLY', 'get' : 'GET',
    'import' : 'IMPORT', 'init' : 'INIT',
    'param' : 'PARAM', 'property' : 'PROTERTY',
    'receiver' : 'RECEIVER', 'set' : 'SET',
    'setparam' : 'SETPARAM', 'value' : 'VALUE',
    'where' : 'WHERE'
}


# List of token names.   This is always required
tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'POW',
    #Variables
    'VARIABLE',


)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


#Jhossias Calderon
#Variables
def t_VARIABLE(t): 
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t


#identificador
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

#Jhossias Calderon
# Expresión para considerar que un numero es de tipo entero
def t_NUMBER(t):
    r'\d+|\-\d+'
    t.value = int(t.value)
    return t

#Expresión para considerar que un numero es de tipo float
def t_FLOAT(t):
    r'\d+\.\d+|\-\d+\.\d+'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
 3 + 4 * 10
   + -20 *2 + ab
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)