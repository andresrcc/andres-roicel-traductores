from collections import OrderedDict

#AMBIENTE SERA HASH TABLE EN PYTHON
class Ambiente(dict):
    """El Ambiente es el conjunto de tablas de simbolos 
    generadas por declaraciones de variables de un 
    programa en AsGArD. Es implementado como 
    una pila de tablas de simbolos.
    """

#Agrega un nuevo alcance a la tabla de simbolos
    def agregar(self,alcance):
        if len(self) == 0:
            self['0'] = alcance
        else:
            self[str(len(self))] = alcance

#Obtiene el tipo de un simbolo en la tabla
#jerarquica de simbolos
    def tipo(self,simbolo):
        nivel = len(self)-1 #comenzamos en el ultimo nivel
        print nivel
        print self[str(nivel)]
        while nivel >= 0:
            alcance = self.get(str(nivel))
            print alcance
            if simbolo in alcance:
                return alcance[simbolo]
            nivel = nivel - 1
        return "Variable no declarada previamente"

if __name__ == "__main__":
    l = dict({'x':'int', 'b':'bool', 'c':'int'})
    k = Ambiente()
    k.agregar(l)
    print k
    m = dict({'x':'bool', 'a':'int','d':'bool'})
    k.agregar(m)
    print k
    print "Averiguemos el tipo de una variable"
    s = raw_input("Introduzca la variable: ")
    print k.tipo(s)
