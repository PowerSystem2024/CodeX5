# Ejercicio 11: Agencia telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor 
# sea el telefono, el programa tendrá el siguiente menú de opciones:
#   1. Nuevo Contacto.
#   2. Borrar Contacto.
#   3. Ver Contactos existentes.
#   4. Salir.

agenda ={}
while True:
    print("\t Menu:")
    print("1. Nuevo Contacto.")
    print("2. Borrar Contacto.")
    print("3. Ver Contactos existentes.")
    print("4. Salir.")
    opcion = int(input("Digite una opcion del menu:"))
    if opcion == 1:
        nombre = input ("Digite nombre del contacto:")
        telefono = input ("Digite el numero de telefono:")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente!")
        else:
            print("Ese nombre de contacto ya exisite")
    elif opcion ==2:
        nombre = input ("Cual es el nombre del contacto:")
        if nombre in agenda:
            del(agenda[nombre])
            print ("Se ha eliminado exitosamente")
        else:
            print("Este contacto no existe en la agenda")
    elif opcion == 3:
        print ("Agenda de contacto")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contacto")
        break
    else:
        print("Se equivoco de opcion")

