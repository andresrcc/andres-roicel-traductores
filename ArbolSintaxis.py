# Autores: Roicel Laya    04-37161
#          Andres Cordova 05-38050
#
#----------------------------------------------------------

#Arbol Sintactico Abstracto

class Arbol:
    def __init__(self,izq,op,der):
        self.type = "Operacion Binaria"
        self.izq  = izq
        self.der  = der
        self.op   = op



class Expresion:

#Operacion Binaria (Nodo)
class OpBinaria(Expresion):
    def __init__(self,izq,op,der):
        self.type = "OperacionBinaria"
        self.izq  = izq
        self.der  = der
        self.op   = op


#Hojas
class Num(Expresion):
    def __init__(self,valor):
        self.type  = "Numero"
        self.valor = valor

class Ident(Expresion):
    def __init__(self,valor):
        self.type = "Identificador/Variable"
        self.valor = valor

class BoolN(Expresion):
    def __init__(self,valor):
        self.type  = "Booleano"
        self.valor = valor

#Probando el modulo
if __name__ == "__main__":
    
