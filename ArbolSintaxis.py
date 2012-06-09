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

# Clase para manejar la regla inicial
class Inicial(Arbol):
    """Representa la regla inicial"""
    def __init__(self,valor):
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + str(self.valor.tipo)
        self.valor.show(profundidad)

#################################       Subclases para las expresiones       ##############################

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

#Hojas

# Clase para los numeros
class Num(Expresion):
    """Clase Num: Representa los numeros del lenguaje"""
    def __init__(self,valor):
        self.tipo = 'integer'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'INT_LITERAL ' + str(self.valor)

# Clase para los identificadores
class Ident(Expresion):
    """Clase Ident: Representa los identificadores del lenguaje"""
    def __init__(self,valor):
        self.tipo = 'ident'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'VAR ' + str(self.valor)

# Clase para los booleanos
class BoolN(Expresion):
    """Clase BoolN: Representa los Valores Booleanos del Lenguaje"""
    def __init__(self,valor):
        self.tipo = 'boolean'
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'BOOL_LITERAL ' + str(self.valor)

# Clase para los lienzos
class Lienzo(Expresion):
    """Clase Lienzo: Representa los Valores Lienzos del Lenguaje"""
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'LIENZO_LITERAL ' + str(self.valor)

class UResta(Expresion):
    def __init__(self,valor):
        self.tipo = None
        self.izq = None
        self.der = None
        self.valor = valor

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + 'INT_LITERAL ' + str(self.valor)

############################       Fin subclases para las expresions       ###########################


############################       Subclases para las instrucciones        ###########################

# Clase para la secuenciacion
class Secuenciacion(Instruccion):
    """Clase Secuenciacion: Representa la secuenciacion del Lenguaje"""
    def __init__(self,izq,der):
        self.tipo = 'SECUENCIACION'
        self.izq = izq
        self.der = der
        self.valor = None

    def show(self, profundidad):
        indentar = ' '*profundidad
        print indentar + '  ' + str(self.izq.tipo)
        self.izq.show(profundidad + 2)
        print indentar + '  ' + str(self.der.tipo)
        self.der.show(profundidad + 2)

# Clase para la asignacion
class Asignacion(Instruccion):
    """Clase Asignacion: Representa una asignacion en el Lenguaje"""
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
   def __init__(self,valor):
       self.tipo = 'ENTRADA/READ'
       self.valor = valor

   def show(self, profundidad):
       indentar = ' '*profundidad
       print indentar + '- read: '
       self.valor.show(profundidad+2)

# Clase para imprimir la salida (print)
class Salida(Instruccion):
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

# Probando los identificadores
    print "Clase Ident:\n"
    s = raw_input('Escriba el nombre de un identificador: ')
    print "\nEl metodo show imprime: "
    Ident(s).show(0)
    print "\n"

# Probando los numeros
    print "Clase Num:\n"
    s = raw_input('Escriba un numero: ')
    print "\nEl metodo show imprime: "
    Num(s).show(0)
    print "\n"

# Probando booleanos
    print "Clase BoolN:\n"
    s = raw_input('Escriba un valor booleano: ')
    print "\nEl metodo show imprime: "
    BoolN(s).show(0)
    print "\n"

# Probando expresiones binarias
    print "Clase ExpBinaria:\n"
    s = raw_input('Escriba una expresion binaria (de numeros): ')
    print "\nEl metodo show imprime: "
    (a,b,c) = s.split()
    ExpBinaria(Num(a),b,Num(c)).show(0)
    print "\n"

########################       Fin de prueba de expresiones       ########################


########################       Prueba de instrucciones        ########################

# Probando asignacion
    print "Clase Asignacion:\n"
    s = raw_input('Escriba una asignacion (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c) = s.split()
    Asignacion(Ident(a),b,Num(c)).show(0)

# Probando repeticion indeterminada
    print "Clase Repeticion Indeterminada:\n"
    s = raw_input('Escriba una repeticion indeterminada (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c,d,e,f,g,h,i) = s.split()
    RepeticionIndeterminada(ExpBinaria(BoolN(b),c,BoolN(d)),Asignacion(Ident(f),g,Num(h))).show(0)

# Probando repeticion determinada
    print "Clase Repeticion Determinada:\n"
    s = raw_input('Escriba una repeticion determinada (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c,d,e,f,g,h,i,j,k) = s.split()
    RepeticionDeterminada(Num(d),Num(f),Asignacion(Ident(h),i,Num(j)),Ident(b)).show(0)

# Probando secuenciacion
    print "Clase Secuenciacion:\n"
    s = raw_input('Escriba una secuenciacion (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c,d,e,f,g) = s.split()
    Secuenciacion(Asignacion(Ident(a),b,Num(c)), Asignacion(Ident(e),f,Num(g))).show(0)

# Probando condicional
    print "Clase Condicional:\n"
    s = raw_input('Escriba un condicional (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b,c,d,e,f,g) = s.split()
    Condicional(BoolN(b), Asignacion(Ident(d),e,Num(f))).show(0)

# Probando read
    print "Clase Entrada:\n"
    s = raw_input('Escriba un read (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b) = s.split()
    Entrada(Ident(b)).show(0)

# Probando print
    print "Clase Salida:\n"
    s = raw_input('Escriba un print (USE ESPACIOS ENTRE LOS SIMBOLOS): ')
    print "\nEl metodo show imprime: "
    (a,b) = s.split()
    Salida(Lienzo(b)).show(0)

########################       Fin de prueba de instrucciones       ######################
