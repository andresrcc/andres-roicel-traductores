# ------------------------------------------------------------
# Lexer.py
#
# Analizador lexico para el lenguaje AsGArD disenyado en el
# curso de Traductores e Interpretadores de la Universidad
# Simon Bolivar.
#
# Autores: Roicel Laya    04-37161
#          Andres Cordova 05-38050
# 
# ------------------------------------------------------------

#agregue from ply para que me corra 
from ply import lex as lex

# Lista de palabras reservadas
reservadas = {
   'begin' : 'TkBegin',
   'boolean' : 'TkBoolean',
   'canvas' : 'TkCanvas',
   'done' : 'TkDone',
   'else' : 'TkElse',
   'end' : 'TkEnd',
   'from' : 'TkFrom',
   'if' : 'TkIf',
   'integer' : 'TkInteger',
   'of type' : 'TkOfType',
   'print' : 'TkPrint',
   'read' : 'TkRead',
   'repeat' : 'TkRepeat',
   'then' : 'TkThen',
   'to' : 'TkTo',
   'using' : 'TkUsing',
   'while': 'TkWhile',
   'with' : 'TkWith',
   'false' : 'TkFalse',
   'true' : 'TkTrue'
}

# Lista de tokens
tokens = [
   'TkIdent',
   'TkNum',
   'TkLienzo',
   'TkComa',
   'TkPuntoYComa',
   'TkParAbre',
   'TkParCierra',
   'TkSuma',
   'TkResta',
   'TkMult',
   'TkDiv',
   'TkMod',
   'TkConjuncion',
   'TkDisyuncion',
   'TkNegacion',
   'TkMenor',
   'TkMenorIgual',
   'TkMayor',
   'TkMayorIgual',
   'TkIgual',
   'TkDesigual',
   'TkHorConcat',
   'TkVerConcat',
   'TkRot',
   'TkTras',
   'TkAsignacion'
] + list(reservadas.values())

# Reglas de expresion regular para tokens simples
t_TkFalse = r'false'
t_TkTrue = r'true'
t_TkComa = r','
t_TkPuntoYComa = r';'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'
t_TkSuma = r'\+'
t_TkResta = r'-'
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkMod = r'%'
t_TkConjuncion = r'/\\'
t_TkDisyuncion = r'\\/'
t_TkNegacion = r'\^'
t_TkMenor = r'<'
t_TkMenorIgual = r'<='
t_TkMayor = r'>'
t_TkMayorIgual = r'>='
t_TkIgual = r'='
t_TkDesigual = r'/='
t_TkHorConcat = r':'
t_TkVerConcat = r'\|'
t_TkRot = r'\$'
t_TkTras = r'\''
t_TkAsignacion = r':='

# Expresion regular para reconocer numeros
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Expresion regular para el caso particular
# del token TkOfType
def t_TkOfType(t):
    r'of(\s)+type'
    return t

# Expresion regular para reconocer literales
# lienzos
def t_TkLienzo(t):
    r'<( |empty|/|\\|_|-|\|)>'
    if t.value == "<empty>":
        t.value = t.value[1:6]
    else:
        t.value = t.value[1:2]
    return t

# Expresion regular para reconocer palabras
# reservadas o identificadores
def t_TkIdent(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'TkIdent')
    return t

# Para saber el numero de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios en blanco
t_ignore = ' \t'

# Ignorar comentarios
def t_comentarios(t):
    r'\{-(.|\n)*-\}'
    pass

# Regla para manejar errores
def t_error(t):
    t.type = "error"
    t.value = 'Error: Caracter inesperado "' + str(t.value[0]) + '" en la fila "' + str(t.lexer.lineno) + '", columna "(aun no se obtiene la columna donde ocurre el error...)"'
    t.lexer.skip(1)
    return t

# Construir el lexer
lexer = lex.lex()

# Sumamos uno al lineno para que cuente las lineas
# empezando por uno
lexer.lineno += 1
