'''
Crea una función tipo_variable que reciba una variable y retorne un mensaje indicando el
tipo de dato de la variable (int, float, str, bool, etc.).
'''

def tipo_variable(variable):
    variable = type(variable)
    return print(f"La variable es de tipo: {variable}")

tipo_variable(True)