from abc import ABC, abstractmethod
"PYTHON IS  STRONGLY TYPED AND DYNAMYC"
"MUTABLES AND IMMUTABLE "
"TUPLAS AND DITIONARY"
"IN A SET {} THERE CAN'T BE EQUAL  ELEMENTS"
"METHODOS TO STRING"
"OPERATORS"
"CONDITIONALS "
"IF, ELIF  ELSE WHILE" "BREAK, CONTINUE"
"FOR WITH ELSE "
"MATCH"

"KWARGS "

# def sumador(**kwargs):
#     # Operador ternario
#     # Operador ternario
#     inicial = kwargs['inicial'] if 'initial' in kwargs else 0
#     final = kwargs['final'] if 'final' in kwargs else 0  # Operador ternario
#     resultado = 0

#     for x in range(inicial, final+1):
#         resultado += x

#     return resultado


# print(sumador())
# print(sumador(inicial=10))
# print(sumador(final=15))
# print(sumador(inicial=10, final=15))

"FUNCIONES LAMBDA"
# def anonima(nombre, nombre2): return print('hola ', nombre, 'y ', nombre2)


# anonima('Pedro', 'Juan')

"CLASES "
"ENCAPSULACTIION"
"INHERITANCE"
"METHOD CONSTRUCTOR"
"COMPOSICION"

"CLASES  DINAMICAS"


# class Dino:
#     def __init__(self):
#         self.__encendido = False

#     def encender(self):
#         self.__encendido = True

#     def apagar(self):
#         self.__encendido = False

#     def estado(self):
#         return self.__encendido


# d = Dino()
# d.encendido = False
# print(d.estado())
# x = d.estado()
# d.encender()
# d.apagar()
# print(d.estado())


"CLASS STATIC"


# class Estatica:
#     numero = 1

#     def incremento():
#         Estatica.numero += 1


# Estatica.incremento()
# print(Estatica.numero)

# "EXAMPLE"


# class Opciones:
#     userName = ''
#     codigo = ' '


"CLASS INHERITANCE"


# class Juguete:
#     def __init__(self):
#         self.__encendido = False

#     def encender(self):
#         self.__encendido = True

#     def __apagar(self):
#         self.__encendido = False

#     def estado(self):
#         return self.__encendido


# class Potato(Juguete):
#     def __init__(self, parametro):
#         super().__init__(parametro)

#     def ponerOreja(self):

#         pass


# class Dino(Potato, Juguete):
#     pass


"CLASS ABSTRACT"


# class Animal(ABC):
#     @abstractmethod
#     def sonido(self):
#         pass

#     def saludo(self):
#         print('Hola')


# class Perro(Animal):
#     def sonido(self):
#         print('Gua')


# class Gato(Animal):
#     def sonido(self):
#         print('Miau')


# p = Perro()
# p.saludo()
# p.sonido()

# g = Gato()
# g.saludo()
# g.sonido()

"RELACIONES HAS-A"


class Motor():
    tipo = 'Diesel'


class Ventanas():
    cantidad = 5


class Ruedas():
    cantidad = 4

    def cambiarCantidad(self, valor):
        self.cantidad = valor


class Carroceria():
    ventanas = Ventanas()
    ruedas = Ruedas()


class Coche():
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print(c.motor.tipo)
print(c.carroceria.ventanas.cantidad)

print(c.carroceria.ruedas.cantidad)

c.carroceria.ruedas.cambiarCantidad(88)
print(c.carroceria.ruedas.cantidad)
