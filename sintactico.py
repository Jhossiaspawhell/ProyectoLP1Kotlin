# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from lex import tokens
from lex import reserved
 
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
               | retor'''

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
def p_variableConTipoBool(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL '
# Variable sin tipo
def p_variableSinTipo(p):
     '''variableSinTipo : valovar VARIABLE IGUAL datosprimitivos
                        | valovar VARIABLE IGUAL repeOper'''
#################################################LISTAS#######################################################


def p_ListadeTipoInt(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPAREN'
def p_ListadeTipoString(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPAREN'
     #FALTA BOOL
def p_ListadeTipoBool(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF repeBool LPAREN  RPAREN'
#Lista sin tipo
def p_ListaSinTipo(p):
     'ListaSinTipo : valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPAREN'
#################################################CONJUNTOS####################################################
# val conjunto: Set<Int> = setOf(1, 3, 4)
# val conjuntoMezclado = setOf(2, 4.454, "casa", 'c')  
def p_ConjuntodeTipoInt(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPAREN'
def p_ConjuntoTipoString(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPAREN'
     #FALTA BOOL
def p_ConjuntodeTipoBool(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN  repeBool RPAREN'
#Lista sin tipo
def p_ConjuntoSinTipo(p):
     'ConjuntoSinTipo : valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPAREN'
#################################################PAIR####################################################





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
                        | ESIGUAL'''

#Tipo de dato
def p_tipoDato(P):
    '''tipoDato : INT
                | STRING
                | BOOLEAN'''

#Argumento
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
              | sublistFinal
              | sublistVar'''

def p_sublistIndex(p):
    'sublistIndex : VARIABLE LCLASP NUMBER DOSPUNTOS NUMBER RCLASP'

def p_sublistDefectoInicio(p):
    'sublistInicio : VARIABLE LCLASP DOSPUNTOS NUMBER RCLASP'

def p_sublistDefectoFinal(p):
    'sublistFinal : VARIABLE LCLASP NUMBER DOSPUNTOS RCLASP'

def p_sublistVariable(p):
    'sublistVar : VARIABLE LCLASP VARIABLE RCLASP '

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
    ''' retor : RETURN VARIABLE'''


def p_repetirOperacion(p):
    '''repeOper : operacion'''


def p_repetirOperacionTodo(p):
    '''repeOper : operacion repeOper'''


def p_operacion(p):
    '''operacion : suma
                | resta
                | multiplicacion
                | division'''


def p_suma(p):
    '''suma : NUMBER PLUS NUMBER'''


def p_resta(p):
    '''resta : NUMBER MINUS NUMBER'''


def p_multiplicacion(p):
    '''multiplicacion : NUMBER TIMES NUMBER'''


def p_division(p):
    '''division : NUMBER DIVIDE NUMBER'''

def p_error(p):
    global textoSalida
    print(p)
    textoSalida+="Regla no reconocida \n" + str(p)
 
# Build the parser
parser = yacc.yacc()

data = '''
val lastName = "Mgbemena"
val firstName: String = "Chike"
val primos: List < Int > = listOf (2)
val nombres: List<String> = listOf("Juan")
val listaMezclada = listOf("Juan", 1, 's') 
val conjunto: Set<Int> = setOf(1, 3, 4)
val conjuntoMezclado = setOf(2, 4, "casa", 'c')  
for(a in 1..5){}
for(a in lista){}
if(a == 0){}
if(a < 0){}
if(a != 0){}
if(a){}
if(True){}
when(hola){}
when{}
fun hola(String f){}
fun hola(int n, Boolean p):int{}
fun hola(){}
fun hola():String{}
print(2)
println(2)
a.contains(b)
a=readLine()
fun Primos():INT{
val ENTRADA: INT = 0
val contador: int = 0 
val CONJUNTO: Set <INT> = setOf(1, 3, 4,2)
ENTRADA = readLine()
for(NUMEROPRIMO in CONJUNTO){
if(ENTADA > NUMEROPRIMO){
print(NUMEROPRIMO)
}
}
return contador
}
a.size()
b.contains(2)
c.contains(d)
"asd".contains("a")
c.contains(d)
"e".contains(f)
"z".rindex(r,1,2)
p.contains(q)
p.contains("q",2)
a[1:5]
b[:5]
c[1:]
'''

def analizarSin(data):
    global textoSalida  
    textoSalida = ""
    result = parser.parse(data)
    textoSalida+=str(result)+"\n"
    return textoSalida

analizarSin(data)