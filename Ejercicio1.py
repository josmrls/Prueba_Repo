# Crea una función llamada verificar_numero que reciba un número y retorne si el número
# es positivo, negativo o cero.

def verificar_numero(numero):
    if numero > 0:
        return 'El número es positivo.'
    elif numero < 0:
        return 'El número es negativo.'
    else:
        return 'El número es cero.'

verificar_numero = verificar_numero(float(input("Ingrese un número: ")))
print(verificar_numero)