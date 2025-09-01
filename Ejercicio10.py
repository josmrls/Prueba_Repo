# Crea una función mayor_de_tres que reciba tres números y retorne el mayor de ellos.

def mayor_de_tres(a, b, c):
    if a > b and a > c:
        return print(f"El número {a} es mayor que {b} y {c}")
    elif a < b and b > c:
        return print(f"El número {b} es mayor que {a} y {c}")
    else:
        return print(f"El número {c} es mayor que {a} y {b}")

mayor_de_tres = mayor_de_tres(float(input("Ingrese primer número:")), float(input("Ingrese segundo número:")), float(input("Ingrese tercer número:")))

