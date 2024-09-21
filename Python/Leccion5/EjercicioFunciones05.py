# Ejercicio 5: Convertidor de temperaturas
# Realizar 2 funciones para comvertir de grados celcius 
# a fahreinheit y viseversa/
# Investigar las formulas

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheint(celsius):
    return celsius * 9 /5 + 32 # La presedencia: multiplicacion, divisioon y suma

# Funcion que convierte de fahrenheit a celsius 
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 # Respetaer la presedencia utilizando parentesis

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheint(celsius)
print (f" {celsius} C a F -> {resultado:.2f}")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)

print (f" {fahrenheit} F a C -> {resultado:.2f}")