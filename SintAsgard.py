# Autores: Roicel Laya 04-37161
# Andres Cordova 05-38050
#
#---------------------------------------------------------

#Imports
from ply import yacc as yacc
import Lexer
import ArbolSintaxis as ast

#Se Extraen Los Tokens
tokens = Lexer.tokens

#Precedencias
precedence = (
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
#Instrucciones

#Regla inicial
def p_instruccion(p):
    '''instruccion : instruccion TkPuntoYComa instruccion
                   | asignacion'''

#Expresion puede ser operacion binaria
def p_expresion_opbinaria(p):
    '''expresion : expresion TkSuma expresion
                 | expresion TkResta expresion
                 | expresion TkMult expresion
                 | expresion TkDiv expresion
                 | expresion TkMod expresion
                 | expresion TkMenor expresion
                 | expresion TkMayor expresion
                 | expresion TkIgual expresion
                 | expresion TkDesigual expresion
                 | expresion TkMenorIgual expresion
                 | expresion TkMayorIgual expresion
                 | expresion TkConjuncion expresion
                 | expresion TkDisyuncion expresion
                 | expresion TkHorConcat expresion
                 | expresion TkVerConcat expresion'''
    p[0] = ast.ExpBinaria(p[1],p[2],p[3])

#Expresion unaria del simbolo menos
def p_expresion_umenos(p):
    'expresion : TkResta expresion %prec UTkResta'
    p[0] = ast.UResta(-p[2])

#Expresion puede ser numero, booleano, variable o lienzo
def p_expresion_TkNum(p):
    'expresion : TkNum'
    p[0] = ast.Num(p[1])

def p_expresion_TkIdent(p):
    'expresion : TkIdent'
    p[0] = ast.Ident(p[1])

# Booleano puede ser verdadero o falso
def p_expresion_TkBoolean(p):
    '''expresion : TkTrue
                 | TkFalse'''
    p[0] = ast.BoolN(p[1])

# Lienzos
def p_expresion_TkLienzo(p):
    'expresion : TkLienzo'
    p[0] = ast.Lienzo(p[1])

# Asignacion
def p_asignacion(p):
    'asignacion : TkIdent TkAsignacion expresion'
    p[0] = ast.Asignacion(p[1],p[2],p[3])

# Errores de Sintaxis
def p_error(p):
    print "Error de Sintaxis"

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
