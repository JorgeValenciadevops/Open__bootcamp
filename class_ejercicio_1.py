class Vehiculo():
    def __init__(self):
        self.color = 'Rojo'
        self.ruedas = 6
        self.puertas = 4


class Coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad = '80 Km/h'
        self.cilindrada = '1000 CC'

    def infoCoche(self):
        print('El coche es {} tiene {} ruedas y {} puertas, su cilidrada es de {} y alcanza una velocidad de {}'.format(
            self.color, self.ruedas, self.puertas, self.cilindrada, self.velocidad))


miCoche = Coche()
miCoche.infoCoche()
miCoche.ruedas = 10
miCoche.infoCoche()
