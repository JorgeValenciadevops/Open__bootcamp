
class Alumno():
    def __init__(self, nombre='Alumno', nota=0.0):
        self.nombre = nombre
        self.nota = nota

    def imprimirNotas(self):
        if self.nota > 3:
            print(f'El alumno {self.nombre} aprobo , su nota es {self.nota}')
        else:
            print(f'El alumno {self.nombre} reprobo, su nota es {self.nota}')


alumno1 = Alumno('pedro', 2.9)
alumno1.imprimirNotas()
