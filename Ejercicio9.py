'''
Crea una función llamada determinar_signo que reciba un número y retorne "Positivo" si
es mayor que cero, "Negativo" si es menor que cero, y "Cero" si es exactamente cero.
'''

def determinar_signo(numero):
    if numero > 0:
        return print(f"El número '{numero}' es positivo")
    elif numero < 0:
        return print(f"El número '{numero}' es negativo")
    else:
        return print(f"El número '{numero}' es cero")

determinar_signo = determinar_signo(float(input("Ingrese un número: ")))
