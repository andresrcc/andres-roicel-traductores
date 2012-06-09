# Autores: Roicel Laya 04-37161
# Andres Cordova 05-38050
#
#---------------------------------------------------------

# COMENTARIOS IMPORTANTES
#
# Se deben sustituir todas las operaciones debajo
# de cada produccion por las operaciones referentes
# a las clases de ArbolSintaxis.
#

#Imports
import sys
from ply import yacc as yacc
import Lexer
import ArbolSintaxis as ast

#Se Extraen Los Tokens
tokens = Lexer.tokens

#Precedencias
precedence = (
    ('left', 'TkPuntoYComa'),
    ('nonassoc', 'TkAsignacion'),
    ('left', 'TkDisyuncion'),
    ('left', 'TkConjuncion'),
    ('nonassoc', 'TkIgual', 'TkDesigual'),
    ('nonassoc', 'TkMenor', 'TkMayor',
     'TkMenorIgual', 'TkMayorIgual'),
    ('left', 'TkSuma', 'TkResta'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
    ('right', 'UTkResta'),
)

#Gramatica

# Regla inicial
def p_inicial(p):
    '''INICIAL : TkUsing IDENTIFICADORES TkOfType TIPOVAR TkBegin INSTRUCCION TkEnd
               | TkBegin INSTRUCCION TkEnd'''
    if len(p) > 4:
        p[0] = ast.Inicial(p[6])
    else:
        p[0] = ast.Inicial(p[2])

# Regla para los identificadores de using
def p_lista_using(p):
    'IDENTIFICADORES : IDENTIFICADORES TkComa TkIdent'

# Identificador del using
def p_ident_using(p):
    'IDENTIFICADORES : TkIdent'

#Regla para la incorporacion de alcance
def p_incorporacion_alcance(p):
    '''INSTRUCCION : TkUsing IDENTIFICADORES TkOfType TIPOVAR TkBegin INSTRUCCION TkEnd
                   | TkBegin INSTRUCCION TkEnd'''
    if len(p) > 4:
        p[0] = ast.Inicial(p[6])
    else:
        p[0] = ast.Inicial(p[2])

#Regla para la secuenciacion
def p_secuenciacion(p):
    'INSTRUCCION : INSTRUCCION TkPuntoYComa INSTRUCCION'
    p[0] = ast.Secuenciacion(p[1],p[3])

##################################           Instrucciones           #################################
# Asignacion
def p_asignacion(p):
    'INSTRUCCION : IDENTIFICADOR TkAsignacion EXPRESION'
    p[0] = ast.Asignacion(p[1],p[2],p[3])

# Repeticion indeterminada
def p_repeticion_indeterminada(p):
    'INSTRUCCION : TkWhile EXPRESION TkRepeat INSTRUCCION TkDone'
    p[0] = ast.RepeticionIndeterminada(p[2],p[4])

# Repeticion determinada
def p_repeticion_determinada(p):
    '''INSTRUCCION : TkWith IDENTIFICADOR TkFrom EXPRESION TkTo EXPRESION TkRepeat INSTRUCCION TkDone
                   | TkFrom EXPRESION TkTo EXPRESION TkRepeat INSTRUCCION TkDone'''
    if len(p) > 8:
        p[0] = ast.RepeticionDeterminada(p[4],p[6],p[8],p[2])
    else:
        p[0] = ast.RepeticionDeterminada(p[2],p[4],p[6])

# Condicional
def p_condicional(p):
    '''INSTRUCCION : TkIf EXPRESION TkThen INSTRUCCION TkElse INSTRUCCION TkDone
                   | TkIf EXPRESION TkThen INSTRUCCION TkDone'''
    if len(p) > 6:
        p[0] = ast.Condicional(p[2],p[4],p[6])
    else:
        p[0] = ast.Condicional(p[2],p[4])

# Leer entrada (read)
def p_read_entrada(p):
    'INSTRUCCION : TkRead IDENTIFICADOR'
    p[0] = ast.Entrada(p[2])

# Imprimir (print)
def p_print_salida(p):
    'INSTRUCCION : TkPrint LIENZO'
    p[0] = ast.Salida(p[2])

# Identificador de repeticion determinada
# y asignacion
def p_ident_asig_repdet(p):
    'IDENTIFICADOR : TkIdent'
    p[0] = ast.Ident(p[1])

# Lienzo de la instruccion print
def p_lienzo_print(p):
    'LIENZO : TkLienzo'
    p[0] = ast.Lienzo(p[1])

# Tipos de las variables de una incorporacion
# de alcance
def p_tipo_var(p):
    '''TIPOVAR : TkInteger
               | TkBoolean
               | TkCanvas'''

##################################           Fin Instrucciones           #############################

###########################            Expresiones            #############################

#Expresion puede ser operacion binaria
def p_expresion_opbinaria(p):
    '''EXPRESION : EXPRESION TkSuma EXPRESION
                 | EXPRESION TkResta EXPRESION
                 | EXPRESION TkMult EXPRESION
                 | EXPRESION TkDiv EXPRESION
                 | EXPRESION TkMod EXPRESION
                 | EXPRESION TkMenor EXPRESION
                 | EXPRESION TkMayor EXPRESION
                 | EXPRESION TkIgual EXPRESION
                 | EXPRESION TkDesigual EXPRESION
                 | EXPRESION TkMenorIgual EXPRESION
                 | EXPRESION TkMayorIgual EXPRESION
                 | EXPRESION TkConjuncion EXPRESION
                 | EXPRESION TkDisyuncion EXPRESION
                 | EXPRESION TkHorConcat EXPRESION
                 | EXPRESION TkVerConcat EXPRESION'''
    p[0] = ast.ExpBinaria(p[1],p[2],p[3])

#Expresion unaria del simbolo menos
def p_expresion_umenos(p):
    'EXPRESION : TkResta EXPRESION %prec UTkResta'
    p[0] = ast.UResta(-p[2])

#Expresion puede ser numero, booleano, variable o lienzo
def p_expresion_TkNum(p):
    'EXPRESION : TkNum'
    p[0] = ast.Num(p[1])

def p_expresion_TkIdent(p):
    'EXPRESION : TkIdent'
    p[0] = ast.Ident(p[1])

# Booleano puede ser verdadero o falso
def p_expresion_TkBoolean(p):
    '''EXPRESION : TkTrue
                 | TkFalse'''
    p[0] = ast.BoolN(p[1])

# Lienzos
def p_expresion_TkLienzo(p):
    'EXPRESION : TkLienzo'
    p[0] = ast.Lienzo(p[1])

##################################           Fin Expresiones          ################################

# Errores de Sintaxis
def p_error(p):
    print "Error de Sintaxis"
    sys.exit()

#Construimos el Parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('AsGArD > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    result.show(0)
