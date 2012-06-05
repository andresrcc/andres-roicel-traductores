# Autores: Roicel Laya    04-37161
#          Andres Cordova 05-38050
#
#----------------------------------------------------------

#Arbol Sintactico Abstracto

class Arbol:
    "Representa al Arbol de Sintaxis Abstracta"
    def __init__(self,izq,op,der,tipo):
        self.tipo = tipo
        self.izq  = izq
        self.der  = der
        self.op   = op

    def show(self):
        print "Prueba:\n"
        return "Tipo: " + self.tipo + "\n" + \
            "Nodo Izq: " + self.izq + "\n" + \
            "Nodo Op: " + self.op + "\n" + \
            "Nodo Der: " + self.der


class Expresion(Arbol):
    "Representa las expresiones del lenguaje"
    pass

class Instruccion(Arbol):
    "Representa las instrucciones del lenguaje"
    pass

#Operacion Binaria (Nodo)
class OpBinaria(Expresion):
    "Representa las Operaciones Binarias del lenguajes"

    def __init__(self,izq,op,der):
        self.izq   = izq
        self.op    = op
        self.der   = der

    def show(self,profundidad):
        """ Imprime el valor del nodo OpBinaria"""

        if self.op == '+':
            self.operacion = 'Suma'
            self.tipo = 'integer'
        elif self.op == '-':
            self.operacion = 'Resta'
            self.tipo = 'integer'
        elif self.op == '*':
            self.operacion = 'Multiplicacion'
            self.tipo = 'integer'
        elif self.op == '/':
            self.operacion = 'Division'
            self.tipo = 'integer' 
        elif self.op == '%':
            self.operacion = 'Modulo'
            self.tipo = 'integer' 
        elif self.op == '<':
            self.operacion = 'Menor Estricto que'
            self.tipo = 'boolean'
        elif self.op == '>':
            self.operacion = 'Mayor Estricto que'
            self.tipo = 'boolean'
        elif self.op == '=':
            self.operacion = 'Igual'
            self.tipo = 'boolean'
        elif self.op == '/=':
            self.operacion = 'Desigual'
            self.tipo = 'boolean'
        elif self.op == '<=':
            self.operacion = 'Menor o Igual que'
            self.tipo = 'boolean'
        elif self.op == '<=':
            self.operacion = 'Mayor o Igual que'
            self.tipo = 'boolean'
        elif self.op == '/\\':
            self.operacion = 'Conjuncion'
            self.tipo = 'boolean'
        elif self.op == '\\/':
            self.operacion = 'Disyuncion'
            self.tipo = 'boolean'

        indentar = ' '*profundidad

        return indentar + "-Operacion: " + self.operacion + "\n" \
            + indentar + "-tipo: " + self.tipo + "\n" \
            + indentar + "-operando izquierdo:" + self.izq.show(profundidad+1)\
            +"\n" + indentar + "-operando derecho: " + self.der.show(profundidad+1)+"\n"
        


#Hojas
class Num(Expresion):
    "Clase Num: Representa los numeros del lenguaje"
    def __init__(self,valor):
        self.valor = valor
    def show(self, profundidad):
        """ Imprime el valor del nodo Num"""
        identar = ' '*profundidad
        return 'INT_LITERAL ' + str(self.valor)

class Ident(Expresion):
    "Representa los identificadores del lenguaje"
    def __init__(self,valor):
        self.valor = valor

    def show(self, profundidad):
        """ Imprime el Valor del nodo Ident"""
        indentar = ' '*profundidad
        return indentar + 'VAR ' + str(self.valor)
        

class BoolN(Expresion):
    "Clase BoolN: Representa los Valores Booleanos del Lenguaje"
    def __init__(self,valor):
        self.valor = valor

    def show(self,profundidad):
        """ Imprime el valor del nodo BoolN"""
        indentar = ' '*profundidad
        return indentar + 'BOOL ' + self.valor


#Area de Prueba del Modulo
if __name__ == "__main__":    
    print "Probando los metodos show de las clases"

#Probando los identificadores
    print "Clase Ident:\n"
    s = raw_input('Escriba el nombre de un identificador:')
    print "\nEl metodo show imprime: "
    f = Ident(s).show(1)
    print f

#Probando los numeros    
    print "Clase Num:\n"
    s = raw_input('Escriba un numero:')
    print "\nEl metodo show imprime: "
    g = Num(s).show(1)
    print g

#Probando las operaciones binarias:

    print "Clase OpBinaria:\n"
    s = raw_input('Escriba una operacion binaria (USE ESPACIOS ENTRE LOS SIMBOLOS):')
    print "\nEl metodo show imprime: "
    (a,b,c) = s.split()
    h = OpBinaria(a,b,c).show(1)
    print h

    print "Clase BoolN:\n"
    s = raw_input('Escriba un valor booleano: ')
    print "\nEl metodo show imprime: "    
    i = BoolN(s).show(1)
    print i
