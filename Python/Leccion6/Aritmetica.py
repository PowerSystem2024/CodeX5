class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase en python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Metodo para sumar
    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def divide(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9) # Le pasamos los argumentos para los operandos.
print(aritmetica1.suma())

print(f"La resta de numeros es: {aritmetica1.resta()}")
print(f"La multiplicacion es: {aritmetica1.multiplicacion()}")
print(f"La division es: {aritmetica1.divide():.2f}")

