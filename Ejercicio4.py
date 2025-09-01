# Crea una función convertir_moneda que reciba una cantidad en dólares y un tipo de
# cambio, y devuelva la cantidad en la nueva moneda.

def convertir_moneda(cantidad_dolares, tipo_cambio=110):
    conversion = cantidad_dolares * tipo_cambio
    return print(f"La cantidad de {cantidad_dolares}$ es igual a {conversion}Bs")

convertir_moneda = convertir_moneda(float(input("Ingrese la cantidad en dólares: ")))
print("Tasa Cambiaria BCV: 110 Bs")
