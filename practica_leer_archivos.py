# RETO conteo de las lineas del cuento de caperucita
with open ("juramento.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))