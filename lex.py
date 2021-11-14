from typing import DefaultDict
import ply.lex as lex

#Autor: Jhossias Calderon, Gustavo Chonillo
#Ingreso de palabras reservadas
reserved = {
    'as' : 'AS', #'as?' : 'AS?',
    'break' : 'BREAK', 'class' : 'CLASS',
    'continue' : 'CONTINUE', 'do' : 'DO',
    'else' : 'ELSE', 'false' : 'FALSE', 'for' : 'FOR',
    'fun' : 'FUN', 'if' : 'IF', 'in' : 'IN', #'!in' : '!IN',
    'interface' : 'INTERFACE', 'is' : 'IS',
    #'!is' : '!IS',
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
    'param' : 'PARAM', 'property' : 'PROPERTY',
    'receiver' : 'RECEIVER', 'set' : 'SET',
    'setparam' : 'SETPARAM', 'value' : 'VALUE',
    'where' : 'WHERE', 'and' : 'AND', 'or' : 'OR'
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
    'LLLAVE',
    'RLLAVE',
    'MAYORQUE',
    'MENORQUE',
    'IGUAL',
    'MOD',
    'POW',
    # Gustavo Chonillo
    'PUNTO',
    'COMA',
    'PUNTOYCOMA',
    'DOSPUNTOS',
    'ESIGUAL',
    'DIFERENTE',
    'NEGACION',
    'LCLASP',
    'RCLASP',
    'INCREMENT',
    'DECREMENT',
    #Variables
    'VARIABLE',
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LLLAVE   = r'{'
t_RLLAVE   = r'}'
#Gustavo Chonillo
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL    = r'='
t_MOD      = r'%'
t_PUNTO    = r'\.'
t_COMA     = r','
t_PUNTOYCOMA=r';'
t_DOSPUNTOS= r':'
t_ESIGUAL  = r'=='
t_DIFERENTE= r'!='
t_NEGACION = r'!'
t_LCLASP   = r'\['
t_RCLASP   = r'\]'
t_INCREMENT= r'\+\+'
t_DECREMENT= r'--'
# RESERVADOS Gustavo Chonillo
t_AS       = r'(as)'
t_BREAK    = r'(break)'
t_CLASS    = r'(class)'
t_CONTINUE = r'(continue)'
t_DO       = r'(do)'
t_ELSE     = r'(else)'
t_FALSE    = r'(false)'
t_FOR      = r'(for)'
t_FUN      = r'(fun)'
t_IF       = r'(if)'
t_IN       = r'(in)'
t_INTERFACE= r'(interface)'
t_IS       = r'(is)'
t_NULL     = r'(null)'
t_OBJECT   = r'(object)'
t_PACKAGE  = r'(package)'
t_RETURN   = r'(return)'
t_SUPER    = r'(super)'
t_THIS     = r'(this)'
t_THROW    = r'(throw)'
t_TRUE     = r'(true)'
t_TRY      = r'(try)'
t_TYPEALIAS= r'(typealias)'
t_TYPEOF   = r'(typeof)'
t_VAL      = r'(val)'
t_VAR      = r'(var)'
t_WHEN     = r'(when)'
t_WHILE    = r'(while)'
t_BY       = r'(by)'
t_CATCH    = r'(catch)'
t_CONSTRUCTOR= r'(constructor)'
t_DELEGATE = r'(delegate)'
t_DYNAMIC  = r'(dynamic)'
t_FIELD    = r'(field)'
t_FILE     = r'(file)'
t_FINALLY  = r'(finally)'
t_GET      = r'(get)'
t_IMPORT   = r'(import)'
t_INIT     = r'(init)'
t_PARAM    = r'(param)'
t_PROPERTY = r'(property)'
t_RECEIVER = r'(receiver)'
t_SET      = r'(set)'
t_SETPARAM = r'(setparam)'
t_VALUE    = r'(value)'
t_WHERE    = r'(where)'
t_AND      = r'(and)'
t_OR       = r'(or)'

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
  while (true){
    a++
  }
  if (a and b){
    return 20
  }
  if (a in c)
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)