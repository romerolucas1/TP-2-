material = input("¿De qué material está hecho el artefacto? ")
peso = float(input("¿Cuánto pesa el artefacto en kilogramos? "))
edad = int(input("¿Cuántos años tiene el artefacto? "))

if material.lower() == "oro" or material.lower() == "plata":
    if peso > 5 and edad > 50:
        print("El artefacto parece ser un tesoro oculto muy valioso.")
    else:
        print("El artefacto puede ser valioso, pero se necesita más información para estar seguro.")
else:
    print("El artefacto parece ser simplemente un adorno decorativo.")
