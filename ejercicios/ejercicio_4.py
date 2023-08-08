class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_sup_izq.x - self. esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        perimetro = 2 * (base + altura)
        return perimetro

    def calcular_area(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        area = base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return base == altura






