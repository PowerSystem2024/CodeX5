# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir a una función
# Defninimos una funcion
def mi_funcion(): # Para identificar a la funciion utilizamos parentesis
    print("Saludos a todos los alumnos de la tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion # se puede llamar a una funcion N cantidad de veces

# Desempaquetando de listas o list umpacking
def show(name, lastname):
    print(name+" "+lastname)
person = ["Ariel","Betancud"]
show(person[0],person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastname":"Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n ==3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se terminó")

# List comprehension. lista de compresion
names = ["Paolo","Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0]== "P"] # Estro regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "MX"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b ["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a traves del canal de youtube")
    print(f"Nombre {name}, Apellido: {lastName}")
mi_funcion2("Jorge","Lucero")
mi_funcion2("Ariel","Betancud")
mi_funcion2("Analia","Pedrosa")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a+b
#resultado = sumar(78,22)
#print(f"El resultado de la suma es : {resultado}")
print(f"El resultado de la suma es : {sumar(55,45)}")

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma:{sumar2(22, 66)}")

# Argumentos, variables en funciones
def listaNombres(*nombres): # Normalmente se utiliza *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres("Lucas","Jose","Claudia","Rosa","Maria")
listaNombres("Marcos","Daniel","Romina","Pepe","Marcela","Carlos")

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir argumentos
    for llave, valor in terminos.items(): # kwargs siginfica : key word argument
        print(f"{llave}: {valor}")

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE = "Integrated Develoment Enviroment", PK = "Primary Key")
listarTerminos(Nombre = "Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito","Pedro","Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10,11) # NO es un objeto iterable
desplegarNombres((10,11)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22,55]) # La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero - 1) # Caso Recursivo
    
numeroFactorial =int(input("Digite el numero para calcular el factorial: "))
resultado = factorial(numeroFactorial) # Lo hacemos en codigo duro
print(f"El factorial del numero 5 es: {resultado}") # Tarea que el usuario ingre el numero para calcular el facotiral