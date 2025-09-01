'''
Crea una función categoria_edad que reciba la edad de una persona y devuelva "Niño" si
es menor de 12 años, "Adolescente" si está entre 12 y 17 años, y "Adulto" si es mayor de
18.
'''

def categoria_edad(edad):
    if edad < 12:
        return print("Es un niño")
    elif 12 >= edad <= 17:
        return print("Es un adolescente")
    elif edad > 17:
        return print("Es un adulto")

categoria_edad = categoria_edad(int(input("Ingrese la edad: ")))
