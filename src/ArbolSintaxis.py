# Autores: Roicel Laya 04-37161
# Andres Cordova 05-38050
#
#----------------------------------------------------------

#Arbol Sintactico Abstracto

class Arbol:
    """Arbol de Sintaxis Abstracta del Lenguaje"""
    def __init__(self,izq,valor,der,tipo):
        self.tipo = tipo
        self.izq = izq
        self.der = der
        self.valor = valor

    def show(self, profundidad):
        print "estoy en el Arbol Principal"
        print "la profundidad del arbol es: " + profundidad
        print "mis hijos son:"
        print "izq: " + self.izq
        print "der: " + self.der

        indentar = ' '*profundidad
        print indentar + str(self.tipo)
        if self.izq:
            self.izq.show(profundidad + 2)
        if self.der:
            self.der.show(profundidad + 2)

class Expresion(Arbol):
    """ Las expresiones del lenguaje. Expresiones
    Binarias y Unarias tipicas (numericas y logicas)"""
    pass

class Instruccion(Arbol):
    """Las instrucciones del lenguaje: Secuenciacion
    Asignacion, Repeticion Indeterminada,
    Repeticion Determinada, Condicional, Entrada (read),
    Salida (print)"""
    pass

# Clase para manejar la regla inicial
class Inicial(Arbol):
    """La regla inicial y la incorporacion de alcance"""
    def __init__(self,valor):
        self.tipo = 'INCORPORACIONALCANCE'
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + str(self.valor.tipo)
        self.valor.show(profundidad + 2)

#################################       Subclases para las expresiones       ##############################

#Expresion Binaria (Nodo)
class ExpBinaria(Expresion):
    """Operaciones Binarias del lenguajes: Suma, Resta, Multiplicacion
    Division, Modulo, Mayor, Menor, Mayor Igual, Menor Igual, Igual,
    Desigual, Conjuncion Disyuncion, Concatenacion Horizontal,
    Concatenacion Vertical. 
    Ej: Concatenacion Horizontal: a : b, Concatenacion Vertical a | b
    con a y b expresiones tipo Lienzo."""

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
        elif self.valor == '>=':
            self.operacion = 'Mayor o Igual que'
            self.tipo = 'boolean'
        elif self.valor == '/\\':
            self.operacion = 'Conjuncion'
            self.tipo = 'boolean'
        elif self.valor == '\\/':
            self.operacion = 'Disyuncion'
            self.tipo = 'boolean'
        elif self.valor == ':':
            self.operacion = 'Concatenacion Horizontal'
            self.tipo = 'lienzo'
        elif self.valor == '|':
            self.operacion = 'Concatenacion Vertical'
            self.tipo = 'lienzo'

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

    def do(self):
        if self.valor == '+':
            return (self.izq.do() + self.der.do())
        elif self.valor == '-':
            return (self.izq.do() - self.der.do())
        elif self.valor == '*':
            return (self.izq.do() * self.der.do())
        elif self.valor == '/':
            return (self.izq.do() / self.der.do())
        elif self.valor == '%':
            return (self.izq.do()%self.der.do())
        elif self.valor == '<':
            return (self.izq.do() < self.der.do())
        elif self.valor == '>':
            return (self.izq.do() > self.der.do())
        elif self.valor == '=':
            return (self.izq.do() == self.der.do())
        elif self.valor == '/=':
            return (self.izq.do() != self.der.do())
        elif self.valor == '<=':
            return (self.izq.do() <= self.der.do())
        elif self.valor == '>=':
            return (self.izq.do() >= self.der.do())
        elif self.valor == '/\\':
            return (self.izq.do() and self.der.do())
        elif self.valor == '\\/':
            return (self.izq.do() or self.der.do())
        elif self.valor == ':':
            pass #Operacion tipo Lienzo
        elif self.valor == '|':
            pass #Operacion tipo Lienzo

            
#Hojas

# Clase para los numeros
class Num(Expresion):
    """Los numeros del lenguaje"""
    def __init__(self,valor):
        self.tipo = 'integer'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'INT_LITERAL ' + str(self.valor)

    def do(self):
        return int(self.valor)

# Clase para los identificadores
class Ident(Expresion):
    """Los identificadores del lenguaje"""
    def __init__(self,valor):
        self.tipo = 'ident'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'VAR ' + str(self.valor)

    def do(self):
        return self.valor

# Clase para los booleanos
class BoolN(Expresion):
    """Valores Booleanos del Lenguaje: true o false"""
    def __init__(self,valor):
        self.tipo = 'boolean'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'BOOL_LITERAL ' + str(self.valor)

    def do(self):
        return bool(self.valor)

# Clase para los lienzos
class Lienzo(Expresion):
    """Los Valores Lienzos del Lenguaje"""
    def __init__(self,valor):
        self.tipo = 'lienzo'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'LIENZO_LITERAL ' + str(self.valor)

# Clase para las expresiones parentizadas
class Parentizada(Expresion):
    """Las expresiones parentizadas"""
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        self.valor.show(profundidad)

# Clase para los enteros negativos
class UResta(Expresion):
    """Operador unario negativo. Ej: -4 """
    def __init__(self,valor):
        self.tipo = 'integer'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'NEGATIVO'
        self.valor.show(profundidad)

# Clase para las negaciones booleanas
class Negacion(Expresion):
    """Las negaciones booleanas."""
    def __init__(self,valor):
        self.tipo = 'boolean'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'NEGACION'
        self.valor.show(profundidad)

# Clase para la rotacion de los lienzos
class Rotacion(Expresion):
    """Las rotaciones de los lienzos"""
    def __init__(self,valor):
        self.tipo = 'lienzo'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'ROTACION'
        self.valor.show(profundidad)

# Clase para la trasposicion de los lienzos
class Trasposicion(Expresion):
    """Las trasposiciones de los lienzos"""
    def __init__(self,valor):
        self.tipo = 'lienzo'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'TRASPOSICION'
        self.valor.show(profundidad)

############################       Fin subclases para las expresiones       ###########################


############################       Subclases para las instrucciones        ############################

# Clase para la secuenciacion
class Secuenciacion(Instruccion):
    """Operador Secuenciacion. Ej: k:= 5 ; p:= k + 4"""
    def __init__(self,izq,der):
        self.tipo = 'SECUENCIACION'
        self.izq = izq
        self.der = der
        self.valor = None

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + str(self.izq.tipo)
        self.izq.show(profundidad + 2)
        print indentar + str(self.der.tipo)
        self.der.show(profundidad + 2)

# Clase para la asignacion
class Asignacion(Instruccion):
    """Operador Asignacion. Ej: a:= 4, a:= true"""
    def __init__(self,izq,valor,der):
        self.tipo = 'ASIGNACION'
        self.izq = izq
        self.der = der
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + '- var: '
        self.izq.show(profundidad + 2)
        print indentar + '- val: '
        self.der.show(profundidad + 2)

# Clase para la repeticion indeterminada
class RepeticionIndeterminada(Instruccion):
    """Expresion Repeticion indeterminada. Ej: while true repeat a:= a + 4 done"""
    def __init__(self,izq,der):
        self.tipo = 'REPETICIONINDETERMINADA'
        self.izq = izq
        self.der = der
        self.valor = None

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + '- guardia: '
        print indentar + '  ' + 'EXPRESIONBINARIA'
        self.izq.show(profundidad + 2)
        print indentar + '- exito: '
        print indentar + '  '  + str(self.der.tipo)
        self.der.show(profundidad + 2)

# Clase para la repeticion determinada
class RepeticionDeterminada(Instruccion):
    """Operador Repeticion Determinada. Ej: ej: with k from 3 to 7 repeat k:= k+1 done"""
    def __init__(self,izq,med,der,valor = None):
        self.tipo = 'REPETICIONDETERMINADA'
        self.izq = izq
        self.med = med
        self.der = der
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        if self.valor:
            print indentar + '- dummy: '
            self.valor.show(profundidad + 2)
        print indentar + '- limite inferior: '
        self.izq.show(profundidad + 2)
        print indentar + '- limite superior: '
        self.med.show(profundidad + 2)
        print indentar + '- instruccion: '
        print indentar + '  ' + str(self.der.tipo)
        self.der.show(profundidad + 2)

# Clase para el condicional
class Condicional(Instruccion):
    """Condicional tipico. Ej: if true then a:= b else b := a done"""
    def __init__(self,izq,der,valor = None):
        self.tipo = 'CONDICIONAL'
        self.izq = izq
        self.der = der
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + '- guardia: '
        print indentar + '  ' + 'EXPRESIONBINARIA'
        self.izq.show(profundidad + 2)
        print indentar + '- exito: '
        print indentar + '  '  + str(self.der.tipo)
        self.der.show(profundidad + 2)
        if self.valor:
            print indentar + '- fracaso: '
            print indentar + '  '  + str(self.valor.tipo)
            self.valor.show(profundidad + 2)

# Clase para leer la entrada (read)
class Entrada(Instruccion):
    """Instruccion read del lenguaje. Ej: read a
    Donde a es una variable que lee entrada por consola"""
    def __init__(self,valor):
       self.tipo = 'ENTRADA/READ'
       self.valor = valor

    def show(self, profundidad):
       indentar = ' '*profundidad
       print indentar + '- read: '
       self.valor.show(profundidad+2)

# Clase para imprimir la salida (print)
class Salida(Instruccion):
    """Instruccion print del lenguaje. Ej: print b
    Donde b es una variable de tipo lienzo que es impresa por consola"""
    def __init__(self,valor):
       self.tipo = 'SALIDA/PRINT'
       self.valor = valor

    def show(self, profundidad):
       indentar = ' '*profundidad
       print indentar + '- print: '
       self.valor.show(profundidad+2)

###########################        Fin subclases para las instrucciones        #######################

# Area de Prueba del Modulo
if __name__ == "__main__":
    print "Probando los metodos show de las clases"

###########################      Prueba de expresiones       #############################
#Prueba funciones do()
    print "Clase Ident:\n"
    s = raw_input('Escriba el nombre de un identificador: ')
    print "\nEl metodo do imprime  " 
    k = Ident(s).do()
    print k

    while True:
        print "Expresiones Binarias Numericas:\n"
        s = raw_input('Escriba una expresion binaria (use espacios entre simbolos: ')
        if s == "e": break
        print "\n El metodo do imprime "
        (a,b,c) = s.split()
        k = ExpBinaria(Num(a),b,Num(c)).do()
        print k

# Probando los identificadores
#    print "Clase Ident:\n"
#    s = raw_input('Escriba el nombre de un identificador: ')
#    print "\nEl metodo show imprime: "
#    
#    Ident(s).show(0)
#    print "\n"

# Probando los numeros
  #  print "Clase Num:\n"
  #  s = raw_input('Escriba un numero: ')
  #  print "\nEl metodo show imprime: "
  #  Num(s).show(0)
  #  print "\n"

# Probando booleanos
 #   print "Clase BoolN:\n"
 #   s = raw_input('Escriba un valor booleano: ')
 #   print "\nEl metodo show imprime: "
 #   BoolN(s).show(0)
 #   print "\n"

# Probando expresiones binarias
#    print "Clase ExpBinaria:\n"
#    s = raw_input('Escriba una expresion binaria (de numeros): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c) = s.split()
##    ExpBinaria(Num(a),b,Num(c)).show(0)
#    print "\n"

########################       Fin de prueba de expresiones       ########################


########################       Prueba de instrucciones        ########################

# Probando asignacion
#    print "Clase Asignacion:\n"
#    s = raw_input('Escriba una asignacion (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c) = s.split()    
#    Asignacion(Ident(a),b,Num(c)).show(0)

# Probando repeticion indeterminada
#    print "Clase Repeticion Indeterminada:\n"
#    s = raw_input('Escriba una repeticion indeterminada (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c,d,e,f,g,h,i) = s.split()
#    RepeticionIndeterminada(ExpBinaria(BoolN(b),c,BoolN(d)),Asignacion(Ident(f),g,Num(h))).show(0)

# Probando repeticion determinada
#    print "Clase Repeticion Determinada:\n"
#    s = raw_input('Escriba una repeticion determinada (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c,d,e,f,g,h,i,j,k) = s.split()
#    RepeticionDeterminada(Num(d),Num(f),Asignacion(Ident(h),i,Num(j)),Ident(b)).show(0)

# Probando secuenciacion
#    print "Clase Secuenciacion:\n"
#    s = raw_input('Escriba una secuenciacion (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c,d,e,f,g) = s.split()
#    Secuenciacion(Asignacion(Ident(a),b,Num(c)), Asignacion(Ident(e),f,Num(g))).show(0)

# Probando condicional
#    print "Clase Condicional:\n"
#    s = raw_input('Escriba un condicional (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b,c,d,e,f,g) = s.split()
#    Condicional(BoolN(b), Asignacion(Ident(d),e,Num(f))).show(0)

# Probando read
#    print "Clase Entrada:\n"
#    s = raw_input('Escriba un read (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b) = s.split()
#    Entrada(Ident(b)).show(0)

# Probando print
#    print "Clase Salida:\n"
#    s = raw_input('Escriba un print (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
#    print "\nEl metodo show imprime: "
#    (a,b) = s.split()
#    Salida(Lienzo(b)).show(0)

########################       Fin de prueba de instrucciones       ######################
