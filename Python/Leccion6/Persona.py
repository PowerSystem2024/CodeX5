class Persona: # Creamos una clase

   def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama método init Dunder
      self.nombre = nombre
      self.apellido = apellido
      self._dni = dni # Este atributo esta encapsulado de una manera sugerida
      self.edad = edad
      self.args = args
      self.kwargs = kwargs

   def mostrar_detalle(self): #self es igual a this
      print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}.')

persona1 = Persona('Ariel', 'Betancud', 34809657,48) # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona('Osvaldo', ' Giordanini',29876345,45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = ' Buccella'
persona1.edad = 40
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son : caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos ( acciones)
persona1.mostrar_detalle() # La referencia en estos casos se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error.

persona1.telefono = "29934898989"
print(f"Este es el telefono de: {persona1.nombre} {persona1.telefono}") # Hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error.

persona3 = Persona("Rogelio", "Romero", 44907210,22, "Telefono", "2658744", "Calle Lopez", 828, "Manzana", 77, "Casa", 18, altura=1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) # Esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos

#persona3.__nombre # Esta totalmente encapsulado


