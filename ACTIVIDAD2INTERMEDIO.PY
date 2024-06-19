potencia_hechizo = float(input("Ingrese la potencia del hechizo: "))
nivel_resistencia_enemigo = float(input("Ingrese el nivel de resistencia del enemigo: "))

if potencia_hechizo >= nivel_resistencia_enemigo:
    print("¡El hechizo es lo suficientemente fuerte para derrotar al enemigo!")
else:
    print("El hechizo no es lo suficientemente fuerte para derrotar al enemigo.")
