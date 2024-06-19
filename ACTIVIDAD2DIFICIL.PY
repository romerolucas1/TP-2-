import math

def calcular_combinaciones(n, k):
    """
    Calcula el número total de combinaciones posibles de formar un equipo de tamaño k
    con n personajes disponibles.
    """
    combinaciones = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return combinaciones

n_personajes = int(input("Ingrese el número total de personajes disponibles: "))

tamano_equipo = int(input("Ingrese el tamaño del equipo que se formará: "))

total_combinaciones = calcular_combinaciones(n_personajes, tamano_equipo)

print(f"El número total de combinaciones posibles para formar un equipo de {tamano_equipo} aventureros es: {total_combinaciones}")
