import random

pc = ["piedra","papel","tijera"]
# Elección de la computadora
pc = random.choice(pc)
eleccion = input("ELIGE PIEDRA PAPEL O TIJERA: ").lower()

if eleccion == pc:
    print("EMPATE")
elif eleccion == "piedra" and pc == "tijera":
    print("GANASTE")
elif eleccion == "papel" and pc == "piedra":
    print("GANASTE")
elif eleccion == "tijera" and pc == "papel":
    print("GANASTE")
else:
    print("PERDISTE")

print(f"La computadora eligió: {pc}")





