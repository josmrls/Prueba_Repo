'''
Crea una función es_par que reciba un número y devuelva "Par" si es par o "Impar" si es impar
'''

def es_par(numero):
    if numero % 2 == 0:
        return print(f"El número {numero} es Par")
    else:
        return print(f"El número {numero} es Impar")

es_par = es_par(float(input("Ingrese un número: ")))