import math

class Punto:
    def _init_(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

#EJERCICIO 3
    def mostrar_coordenadas(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y}")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        distancia=math.sqrt((self.x - otro_punto.x)**2 +(sel.y - otro_punto.y)**2)



