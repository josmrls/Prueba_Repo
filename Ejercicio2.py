# Crea una función maximo que reciba dos números y retorne el mayor de ellos.

def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

maximo = maximo(float(input("Ingrese el primer número:")), float(input("Ingrese el segundo número:")))
print(f"El número mayor es: {maximo}")
