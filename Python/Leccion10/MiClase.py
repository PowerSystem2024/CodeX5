class MiClase:
    # Variablede clase, este atributodará a cada objeto el mismo valor
    variable_clase = 'Esta es una varaible de clase'

    def __init__(self, varaible_instancia):# La variable instancia, da diferentes valores
        self.varaible_instancia = varaible_instancia

print(MiClase.variable_clase)
miClase1  = MiClase('Esta es una variable de instancia')
print(miClase1.varaible_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.varaible_instancia)
print(miClase2.variable_clase)






