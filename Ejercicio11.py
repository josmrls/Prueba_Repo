'''
Crea una función calcular_salario_neto que reciba el salario bruto de una persona y
aplique una deducción de impuestos del 10% para calcular el salario neto.
'''
def calcular_salario_neto(salario_bruto):
    return salario_bruto - ((salario_bruto * 10) / 100)

salario_bruto = float(input("Introduce el salario bruto: "))
calcular_salario_neto = print("El salario neto es: ", calcular_salario_neto(salario_bruto))