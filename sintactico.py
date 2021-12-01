# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens
from lex import reserved

textoSalida = ""  # Texto en el que se escribe la salida
error="a"

##################################################

def p_t(p):
    '''todoConLinea : repetodo '''


def p_todo(p):
    '''todo :  lista
              | variable
              | conjunto
              | control
              | adicionales
              | funcion
              | sublist
              | readline
              | prin
              | contador
              | retor
              | comparacion
              | operacion
              | asignacion
              | operacionesSem'''


def p_repeTodoA(p):
    '''repetodo : todo'''


def p_repeTodo(p):
    'repetodo : todo repetodo'



##Listas
def p_Todaslaslistas(p):
    '''lista :  ListaConTipo
              | ListaSinTipo '''


##Variable
def p_Todaslasvariables(p):
    '''variable : variableConTipo
               | variableSinTipo '''


##Conjunto
def p_TodaslosConjunto(p):
    '''conjunto : ConjuntoConTipo
               | ConjuntoSinTipo '''


#################################################VARIABLE####################################################
# Variable con tipo
def p_variableConTipoString(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS STRING IGUAL STRINGPALABRA'


def p_variableConTipoInt(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS INT IGUAL NUMBER'
    # FALTA AÑADIR BOOL


def p_variableConTipoBool(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL '


# Variable sin tipo
def p_variableSinTipo(p):
    'variableSinTipo : valovar VARIABLE IGUAL datosprimitivos '


#################################################LISTAS#######################################################

# Corregir que ingrese mas de un elemento
def p_ListadeTipoInt(p):
    'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPAREN'


def p_ListadeTipoString(p):
    'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPAREN'


def p_ListadeTipoBool(p):
    'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF repeBool LPAREN  RPAREN'


# Lista sin tipo
def p_ListaSinTipo(p):
    'ListaSinTipo : valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPAREN'


#################################################CONJUNTOS####################################################
def p_ConjuntodeTipoInt(p):
    'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPAREN'


def p_ConjuntoTipoString(p):
    'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPAREN'
    # FALTA BOOL


def p_ConjuntodeTipoBool(p):
    'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN  repeBool RPAREN'


# Lista sin tipo
def p_ConjuntoSinTipo(p):
    'ConjuntoSinTipo : valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPAREN'


#############################################################################################################

# REGLAS QUE TE PUEDEN SERVIR
def p_algunTipo(p):
    '''datosprimitivos : NUMBER
              | STRINGPALABRA
              | BOOLEANPALABRA
              | VARIABLE '''


def p_valovar(p):
    '''valovar :  VAR
              | VAL'''


# PARA QUE SE REPITA INT
def p_repetirInt(p):
    'repeInt : valor'


def p_repetirInt_i(p):
    'repeInt : valor COMA repeInt'


def p_valor(p):
    '''valor : NUMBER
       | VARIABLE '''


# PARA QUE SE REPITA STRING
def p_repetirString(p):
    'repeString : String'


def p_repetirString_s(p):
    'repeString : String COMA repeString'


def p_String(p):
    '''String : STRINGPALABRA
       | VARIABLE'''


# PARA QUE SE REPITA BOOL
def p_repetirBool(p):
    'repeBool : bool'


def p_repetirBool_B(p):
    'repeBool : bool COMA repeBool'


def p_Bool(p):
    '''bool : BOOLEANPALABRA
       | VARIABLE'''


# PARA QUE SE REPITA CUALQUIERDATOPRIMITIVO
def p_repetirCualquiera(p):
    'repeCualquier : datosprimitivos'


def p_repetirCualquiera_i(p):
    'repeCualquier : datosprimitivos COMA repeCualquier'


# PARA COMPARAR VARIABLES Y NUMEROS

def p_comparacion(p):
    'comparacion : valor operadoresComp valor'


def p_operadoresComp(p):
    '''operadoresComp : MAYORQUE
                        | DIFERENTE
                        | MENORQUE
                        | ESIGUAL
                        | MAYORIGUAL
                        | MENORIGUAL'''

#Operaciones
def p_operacion(p):
    'operacion : NUMBER operadores NUMBER'


def p_operadores(p):
    '''operadores : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD'''

#Asignación

def p_adignacion(p):
    'asignacion : VARIABLE operadoresAsig NUMBER'


def p_operadoresAsig(p):
    '''operadoresAsig : PLUS IGUAL
                    | MINUS IGUAL
                    | TIMES IGUAL
                    | DIVIDE IGUAL
                    | MOD IGUAL'''



# Tipo de dato
def p_tipoDato(P):
    '''tipoDato : INT
                | STRING
                | BOOLEAN'''


# Argumento
def p_Argumento(P):
    'argumento : tipoDato VARIABLE'


def p_repetirArgumento(p):
    'repeArg : argumento'


def p_repetirArgumento_B(p):
    'repeArg : argumento COMA repeArg'


###############################################################
def p_control(p):
    '''control : if
              | for'''


def p_if(p):
    '''if : ifBoolean
            | ifComparacion
            | ifVariable'''


def p_for(p):
    '''for : forRango
           | forVariable'''


###############################################################
def p_ifBoolean(p):
    'ifBoolean : IF LPAREN BOOLEANPALABRA RPAREN LLLAVE  repetodo RLLAVE'


def p_ifComparacion(p):
    'ifComparacion : IF LPAREN comparacion RPAREN LLLAVE repetodo RLLAVE'


def p_ifVariable(p):
    'ifVariable : IF LPAREN VARIABLE RPAREN LLLAVE repetodo RLLAVE'


###############################################################
def p_forVariable(p):
    'forVariable : FOR LPAREN VARIABLE IN VARIABLE RPAREN LLLAVE repetodo RLLAVE'


def p_forRango(p):
    'forRango : FOR LPAREN VARIABLE IN NUMBER PUNTO PUNTO NUMBER RPAREN LLLAVE repetodo RLLAVE'


################################################################

def p_funcion(p):
    ''' funcion : funConSalidaArg
                | funConSalida
                | funSinSalidaArg
                | funSinSalida'''


def p_funcionConSalida(p):
    'funConSalida : FUN VARIABLE LPAREN repeArg RPAREN DOSPUNTOS tipoDato LLLAVE repetodo RLLAVE'


def p_funcionSinSalida(p):
    'funSinSalida : FUN VARIABLE LPAREN repeArg RPAREN LLLAVE repetodo RLLAVE'


def p_funcionConSalidaArg(p):
    'funConSalidaArg : FUN VARIABLE LPAREN RPAREN DOSPUNTOS tipoDato LLLAVE repetodo RLLAVE'


def p_funcionSinSalidaArg(p):
    'funSinSalidaArg : FUN VARIABLE LPAREN RPAREN LLLAVE repetodo RLLAVE'


#############################
def p_adicionales(p):
    '''adicionales : size
                  | rindex
                  | sublist
                  | contains'''


def p_size(p):
    '''size : VARIABLE PUNTO SIZE'''


def p_contains(p):
    '''contains :
                | VARIABLE PUNTO CONTAINS LPAREN datosprimitivos RPAREN
                | STRINGPALABRA PUNTO CONTAINS LPAREN  STRINGPALABRA RPAREN
                | STRINGPALABRA PUNTO CONTAINS LPAREN  VARIABLE RPAREN
                '''


def p_lastindexof(p):
    '''rindex : STRINGPALABRA PUNTO RINDEX LPAREN repeCualquier RPAREN
                | VARIABLE PUNTO RINDEX LPAREN repeCualquier RPAREN'''


def p_sublist(p):
    '''sublist : sublistIndex
              | sublistInicio
              | sublistFinal'''


def p_sublistIndex(p):
    'sublistIndex : VARIABLE LCLASP NUMBER DOSPUNTOS NUMBER RCLASP'


def p_sublistDefectoInicio(p):
    'sublistInicio : VARIABLE LCLASP DOSPUNTOS NUMBER RCLASP'


def p_sublistDefectoFinal(p):
    'sublistFinal : VARIABLE LCLASP NUMBER DOSPUNTOS RCLASP'


def p_readlin(p):
    '''readline : VARIABLE IGUAL READLINE
                | valovar VARIABLE IGUAL READLINE'''


def p_printoln(p):
    '''prin : PRINT LPAREN datosprimitivos RPAREN
            | PRINTLN LPAREN datosprimitivos RPAREN
            '''


def p_contador(p):
    '''contador : VARIABLE PLUS PLUS '''


def p_return(p):
    ''' retor : RETURN operacionesSem
                | RETURN VARIABLE '''



def p_error(p):
    global error
    error = "Syntax error in input!\n"

#semantico Gustavo Chonillo
def p_semantico_operaciones(p):
    '''operacionesSem : VARIABLE operadores VARIABLE
                        | STRINGPALABRA PLUS NUMBER
                        | STRINGPALABRA PLUS STRINGPALABRA
                        | STRINGPALABRA PLUS VARIABLE
                        | VARIABLE PLUS STRINGPALABRA
                        | NUMBER operadores VARIABLE
                        | VARIABLE operadores NUMBER
                    '''

def p_semantico_operaciones_error_str_ini(p):
    '''operacionesSem : STRINGPALABRA PLUS error'''
    global error
    error = " Error semántico, se esperaba una variable o número después del operador"

def p_semantico_operaciones_error_str_fin(p):
    '''operacionesSem : error PLUS STRINGPALABRA '''
    global error
    error = " Error semántico, se esperaba una variable antes del operador"

def p_semantico_operaciones_error_num_ini(p):
    '''operacionesSem : NUMBER operadores error'''
    global error
    error = " Error semántico, se esperaba un número o variable después del operador"

def p_semantico_operaciones_error_num_fin(p):
    '''operacionesSem : error operadores NUMBER'''
    global error
    error = " Error semántico, se esperaba un número o variable antes del operador"


#Semantico Jhossias Calderon
def p_semantico_boolean_op(p):
    '''boolean_operations : VARIABLE AND VARIABLE
                        | VARIABLE OR VARIABLE
                        | VARIABLE IGUAL VARIABLE
                        | VARIABLE NOIGUAL VARIABLE
                        | VARIABLE MAYORQUE VARIABLE
                        | VARIABLE MAYORIGUAL VARIABLE
                        | VARIABLE MENORQUE VARIABLE
                        | VARIABLE MENORIGUAL VARIABLE
                        | NUMBER IGUAL NUMBER
                        | NUMBER NOIGUAL NUMBER
                        | NUMBER MAYORQUE NUMBER
                        | NUMBER MAYORIGUAL NUMBER
                        | NUMBER MENORQUE NUMBER
                        | NUMBER MENORIGUAL NUMBER
                        | TRUE AND TRUE
                        | TRUE OR TRUE
                        | TRUE AND FALSE
                        | TRUE OR FALSE
                        | FALSE AND FALSE
                        | FALSE OR FALSE
                        | TRUE IGUAL TRUE
    '''
    # Semantic (prueba semantica)
    if p[2] == 'AND':
        p[0] = p[1] and p[3]
    elif p[2] == 'OR':
        p[0] = p[1] or p[3]
    elif p[2] == 'IGUAL':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'NOIGUAL':
        if p[1] != p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'MAYORQUE':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'MAYORIGUAL':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'MENORQUE':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'MENORIGUAL':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False
    if not isinstance(p[1], bool) and not isinstance(p[2], bool) :
        print("Semantic error in input!")


# Build the parser
parser = yacc.yacc()

"""while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)"""

def analizarSin(data):
    global textoSalida, error
    error =""
    textoSalida = ""
    result = parser.parse(data)
    textoSalida+=str(result)+"\n"+error
    return textoSalida


