'''
Crea una función calificar que reciba una calificación y retorne "Aprobado" si es mayor o
igual a 10, o "Reprobado" si es menor
'''

def calificar(calficacion):
    if calficacion >= 10:
        return print("El estudiante está Aprobado")
    else:
        return print("El estudiante está Reprobado")
calificar = calificar(float(input("Ingrese la calificación del estudiante: ")))
