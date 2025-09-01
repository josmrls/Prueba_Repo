'''
Crea una función es_multiplo que reciba dos números y retorne True si el primero es
múltiplo del segundo, y False en caso contrario.
'''

def es_multiplo(a, b):
    if a % b == 0:
        print(f"{a} es múltiplo de {b}")
        return True
    else:
        print(f"{a} no es múltiplo de {b}")
        return False

es_multiplo = es_multiplo(float(input("Ingrese el primer número:")), float(input("Ingrese el segundo número:")))

