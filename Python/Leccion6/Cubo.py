class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese lops valores
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input("Ingrese el ancho del cubo: "))
altura = int(input("Ingrese la altura del cubo: "))
profundidad = int(input("Ingrese la profundidad del cubo: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")