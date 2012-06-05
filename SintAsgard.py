# Autores: Roicel Laya    04-37161
#          Andres Cordova 05-38050
#
#---------------------------------------------------------

# COMENTARIOS IMPORTANTES
#
# Se deben sustituir todas las operaciones debajo
# de cada produccion por las operaciones referentes
# a las clases de ArbolSintaxis.
# 

#Imports
from ply import yacc as yacc 
import Lexer
import ArbolSintaxis as ast

#Se Extraen Los Tokens
tokens = Lexer.tokens

#Precedencias
precedence = (
    ('right', 'TkAsignacion'),
    ('left', 'TkDisyuncion'),
    ('left', 'TkConjuncion'),
    ('left', 'TkIgual', 'TkDesigual'),
    ('left', 'TkMenor', 'TkMayor', 
     'TkMenorIgual', 'TkMayorIgual'),
    ('left', 'TkSuma', 'TkResta'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
)

#Gramatica Inicial
#Instrucciones

#Secuenciacion
def p_instruccion(p):
    'instruccion : expresion TkPuntoYComa expresion' 

#Condicional
def p_instruccionIf(p):
    'instruccion : TkIf expresion TkThen instruccion'
    if p[2] == true:
        p[0] = p[4]

def p_instruccionBegin(p):
    '''instruccion   : TkBegin instruccion TkEnd
                     | TkUsing expresion TkBegin instruccion TkEnd'''
    if p[1] == 'begin':
        p[0] = [1]
#Como se incluye la lista de declaraciones de using?
    elif p[1] == 'using':
        p[0] = p[4]
       
def p_instruccionOfT(p):
    'instruccion : expresion TkOfType TkNum'
    p[0] = int(p[1])


#Expresion puede ser operacion binaria
def p_expresion(p):
    '''expresion : expresion TkSuma  expresion
                 | expresion TkResta expresion
                 | expresion TkMult  expresion
                 | expresion TkDiv   expresion
                 | expresion TkMod   expresion
                 | expresion TkMenor expresion
                 | expresion TkMayor expresion
                 | expresion TkIgual expresion
                 | expresion TkDesigual expresion
                 | expresion TkMenorIgual expresion
                 | expresion TkMayorIgual expresion
                 | expresion TkConjuncion expresion
                 | expresion TkDisyuncion expresion'''
    p[0] = ast.OpBinaria(p[1],p[2],p[3]).show()

#Expresion puede ser numero, booleano, o variable
def p_expresion_TkNum(p):
    'expresion : TkNum'
    p[0] = ast.Num(p[1]).show()

def p_expresion_TkIdent(p):
    'expresion : TkIdent'
    p[0] = ast.Ident(p[1]).show()

def p_expresion_TkBoolean(p):
    'expresion : TkBoolean'
    p[0] = p[1]

# Booleano puede ser verdadero o falso

def p_true(p):
    'expresion : TkTrue'
    p[0] = True

def p_false(p):
    'expresion : TkFalse'
    p[0] = False

#Asignacion
def p_TkIdent_AsigTkNum(p):
    'expresion : TkIdent TkAsignacion TkNum'
    p[0] = p[1]

def p_TkIdent_TkT(p):
    'expresion : TkIdent TkAsignacion TkTrue'
    p[0] = p[1]

def p_TkIdent_TkF(p):
    'expresion : TkIdent TkAsignacion TkFalse'

#Operadores Unarios
#Negacion
def p_TkNeg_TkTrue(p):
    'expresion : TkNegacion TkTrue'
    p[0] = False

def p_TkNeg_TkFalse(p):
    'expresion : TkNegacion TkFalse'
    p[0] = True

#Negativo 
def p_TkNeg_TkNum(p):
    'expresion : TkResta TkNum'
    p[0] = - p[2]

#Parentizacion
def p_expresion_Paren(p):
    'expresion : TkParAbre expresion TkParCierra'
    p[0] = p[2]


#Secuenciacion


# Errores de Sintaxis
def p_error(p):
    print "Error de Sintaxis"

#Construimos el Parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('AsGArD >')
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    print result

#Parsear
ast.show()
