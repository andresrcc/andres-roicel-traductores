# Autores: Roicel Laya 04-37161
# Andres Cordova 05-38050
#
#----------------------------------------------------------

#Arbol Sintactico Abstracto

class Arbol:
    """Representa al Arbol de Sintaxis Abstracta"""
    def __init__(self,izq,valor,der,tipo):
        self.tipo = tipo
        self.izq = izq
        self.der = der
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + str(self.tipo)
        if self.izq:
            self.izq.show(profundidad + 2)
        if self.der:
            self.der.show(profundidad + 2)

class Expresion(Arbol):
    """Representa las expresiones del lenguaje"""
    pass

class Instruccion(Arbol):
    """Representa las instrucciones del lenguaje"""
    pass

#Expresion Binaria (Nodo)
class ExpBinaria(Expresion):
    """Representa las Operaciones Binarias del lenguajes"""

    def __init__(self,izq,valor,der):
        self.izq = izq
        self.der = der
        self.valor = valor
        if self.valor == '+':
            self.operacion = 'Suma'
            self.tipo = 'integer'
        elif self.valor == '-':
            self.operacion = 'Resta'
            self.tipo = 'integer'
        elif self.valor == '*':
            self.operacion = 'Multiplicacion'
            self.tipo = 'integer'
        elif self.valor == '/':
            self.operacion = 'Division'
            self.tipo = 'integer'
        elif self.valor == '%':
            self.operacion = 'Modulo'
            self.tipo = 'integer'
        elif self.valor == '<':
            self.operacion = 'Menor Estricto que'
            self.tipo = 'boolean'
        elif self.valor == '>':
            self.operacion = 'Mayor Estricto que'
            self.tipo = 'boolean'
        elif self.valor == '=':
            self.operacion = 'Igual'
            self.tipo = 'boolean'
        elif self.valor == '/=':
            self.operacion = 'Desigual'
            self.tipo = 'boolean'
        elif self.valor == '<=':
            self.operacion = 'Menor o Igual que'
            self.tipo = 'boolean'
        elif self.valor == '<=':
            self.operacion = 'Mayor o Igual que'
            self.tipo = 'boolean'
        elif self.valor == '/\\':
            self.operacion = 'Conjuncion'
            self.tipo = 'boolean'
        elif self.valor == '\\/':
            self.operacion = 'Disyuncion'
            self.tipo = 'boolean'

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + '- operacion: ' + str(self.operacion)
        print indentar + '- tipo: ' + str(self.tipo)
        if self.izq:
            print indentar + '- operando izquierdo: '
            self.izq.show(profundidad + 2)
        if self.der:
            print indentar + '- operando derecho: '
            self.der.show(profundidad + 2)

#Hojas
class Num(Expresion):
    """Clase Num: Representa los numeros del lenguaje"""
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'INT_LITERAL ' + str(self.valor)

class Ident(Expresion):
    """Representa los identificadores del lenguaje"""
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'VAR ' + str(self.valor)

class BoolN(Expresion):
    """Clase BoolN: Representa los Valores Booleanos del Lenguaje"""
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'BOOL_LITERAL ' + str(self.valor)

class UResta(Expresion):
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'INT_LITERAL ' + str(self.valor)

#Area de Prueba del Modulo
if __name__ == "__main__":
    print "Probando los metodos show de las clases"

#Probando los identificadores
    print "Clase Ident:\n"
    s = raw_input('Escriba el nombre de un identificador: ')
    print "\nEl metodo show imprime: "
    Ident(s).show(0)

#Probando los numeros
    print "Clase Num:\n"
    s = raw_input('Escriba un numero: ')
    print "\nEl metodo show imprime: "
    Num(s).show(0)

#Probando las operaciones binarias:

    print "Clase OpBinaria:\n"
    s = raw_input('Escriba una operacion binaria (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c) = s.split()
    h = ExpBinaria(a,b,c)
    print h.show(0)

    print "Clase BoolN:\n"
    s = raw_input('Escriba un valor booleano: ')
    print "\nEl metodo show imprime: "
    i = BoolN(s).show(0)
    print i
