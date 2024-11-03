class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


def add (self, other): # Other significa = otro
    return f'{self.nombre}  {other.nombre}'

def sub (self, otro): # Sub significa = substraccion (resta)
    return self.edad - otro.edad



personal = Persona('Ariel', 40)
persona2 = Persona('Betancud', 5)

# personal.__add___(persona2) sintaxis interna y automatica

print(personal + persona2) 