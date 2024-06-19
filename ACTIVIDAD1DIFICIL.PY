def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def calcular_combinaciones(n, k):
    """
    Calcula el número de combinaciones posibles para formar equipos.
    
    :param n: Número total de personas
    :param k: Tamaño del equipo
    :return: Número total de combinaciones posibles
    """
    if k > n:
        return 0  # No es posible formar equipos si k es mayor que n
    return factorial(n) // (factorial(k) * factorial(n - k))

# Ejemplo de uso
n = int(input("Ingresa el número total de personas: "))
k = int(input("Ingresa el tamaño del equipo: "))

combinaciones = calcular_combinaciones(n, k)
print(f"El número total de combinaciones posibles es: {combinaciones}")
