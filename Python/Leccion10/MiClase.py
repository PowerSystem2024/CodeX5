class MiClase:
    # Variablede clase, este atributodará a cada objeto el mismo valor
    variable_clase = 'Esta es una varaible de clase'

    def __init__(self, varaible_instancia):# La variable instancia, da diferentes valores
        self.varaible_instancia = varaible_instancia

    @staticmethod
    def metodo_estatico(): # Metodo estatico se asocia a la clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.varaible_instancia)

print(MiClase.variable_clase)
miClase1  = MiClase('Esta es una variable de instancia')
print(miClase1.varaible_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.varaible_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()