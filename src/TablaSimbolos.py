from collections import OrderedDict

class Ambiente(list):
    """El Ambiente es el conjunto de tablas de simbolos 
    generadas por declaraciones de variables de un 
    programa en AsGArD. Es implementado como 
    una pila de tablas de simbolos.
    """



if __name__ == "__main__":
    print "Probando la clase ambiente"
    l = dict(x='int',y='bool',z='int')
    k = Ambiente()
    k.append(l)
    m = dict(x='bool',d='bool',f='bool')
    k.append(m)
    print "El Ambiente contiene las tablas de simbolos \
generadas por todas las declaraciones en orden"
    print "Entonces, por ejemplo podemos distinguir una variable x local de tipo bool"
    print "de una variable x global de tipo int"
    print "Veamos este Ambiente como ejemplo"
    print k
    p = k.pop()
    print "Popeamos la ultima tabla creada (tabla actual): "
    print p
    print "La tabla jerarquica queda: "
    print k
    print "Busquemos el tipo de la variable x"
    t = p['x']
    print "El tipo de la variable x local es:"
    print t
    print "Buscando en la otra tabla (contexto global): "
    m = k.pop()
    print m
    mm = m['x']
    print "El tipo de la variable x global es:"
    print mm
    k.append(m)
    k.append(p)
    print "Rearmamos la tabla de simbolos"
    print k
