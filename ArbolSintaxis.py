# Autores: Roicel Laya    04-37161
#          Andres Cordova 05-38050
#
#----------------------------------------------------------

#Arbol Sintactico Abstracto

class Arbol:
    "Representa al Arbol de Sintaxis Abstracta"
    def __init__(self,izq,op,der):
        self.izq  = izq
        self.der  = der
        self.op   = op



class Expresion(Arbol):
    "Representa las expresiones del lenguaje"
    pass

class Instruccion(Arbol):
    "Represenita las instrucciones del lenguaje"
    pass

#Operacion Binaria (Nodo)
class OpBinaria(Expresion):
    "Representa las Operaciones Binarias del lenguajes"

    def __init__(self,izq,op,der):
        self.izq  = izq
        self.der  = der
        self.op   = op

    def show(self):
        """ Imprime el valor del nodo OpBinaria"""
        printme = str(self.izq) + str(self.op) + str(self.der)
        print printme


#Hojas
class Num(Expresion):
    "Clase Num: Representa los numeros del lenguaje"
    def __init__(self,valor):
        self.valor = valor

    def show(self):
        """ Imprime el valor del nodo Num"""
        print self.valor

class Ident(Expresion):
    "Representa los identificadores del lenguaje"
    def __init__(self,valor):
        self.valor = valor

    def show(self):
        """ Imprime el Valor del nodo Ident"""
        print self.valor

class BoolN(Expresion):
    "Clase BoolN: Representa los Valores Booleanos del Lenguaje"
    def __init__(self,valor):
        self.valor = valor
    def show(self):
        """ Imprime el valor del nodo BoolN"""
        print self.valor

#Probando el modulo
if __name__ == "__main__":    
    print "Probando los metodos show de las clases"

#Probando los identificadores
    print "Clase Ident:\n"
    s = raw_input('Escriba el nombre de un identificador:')
    print "\nEl metodo show imprime: "
    f = Ident(s)
    f.show()

#Probando los numeros    
    print "Clase Num:\n"
    s = raw_input('Escriba un numero:')
    print "\nEl metodo show imprime: "
    g = Num(s)
    g.show()

#Probando las operaciones binarias:

    print "Clase OpBinaria:\n"
    s = raw_input('Escriba una operacion binaria (USE ESPACIOS ENTRE LOS SIMBOLOS):')
    print "\nEl metodo show imprime: "
    (a,b,c) = s.split()
    h = OpBinaria(a,b,c)
    h.show()

    print "Clase BoolN:\n"
    s = raw_input('Escriba un valor booleano: ')
    print "\nEl metodo show imprime: "    
    i = BoolN(s)
    i.show()
