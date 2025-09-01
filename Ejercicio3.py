# Crea una función es_bisiesto que reciba un año y determine si es bisiesto (divisible entre
# 4 pero no entre 100, o divisible entre 400).

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return print(f"El año {año} es bisiesto.")
    else:
        return print(f"El año {año} no es bisiesto.")

es_bisiesto = es_bisiesto(int(input("Ingrese un año: ")))