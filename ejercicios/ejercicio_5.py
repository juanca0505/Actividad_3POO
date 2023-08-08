import math
class Ciruclo:
    def __init__(self, centro, radio):
        self. centro = centro
        self. radio = radio
    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia = self.centro.calcular_distancia(punto)
        return distancia <= self.radio
