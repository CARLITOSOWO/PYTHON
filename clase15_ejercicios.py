# Ejercicios:
print("Doble de los Números")
print("Dada una lista de números [1, 2, 3, 4, 5], crea una nueva")
print("lista que contenga el doble de cada número usando una List Comprehension.")
lista = [x * 2 for x in range(1,20)]
print ("LOS DOBLE DE LOS NUMEROS EN UN RANGO DE 1 A 20 SON: " ,lista)




# [expresión for elemento in iterable if condición]

# squares = [x ** 2 for x in range(1,11)]
# print("LOS CUADRADOS SON :" , squares)


# Ejercicios 2:
print("Filtrar y Transformar en un Solo Paso")
print("Tienes una lista de palabras sol mar montaña rio estrella y ")
print("quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.")


palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print("Palabras filtradas y en mayúsculas:", palabras_filtradas)


print("\n")

# Ejercicios 3:
print("Crear un Diccionario con List Comprehension")
print("Tienes dos listas, una de claves nombre edad ocupación y otra de valores Juan 30 Ingeniero")
print("Crea un diccionario combinando ambas listas usando una List Comprehension.")


claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {claves[i]: valores[i] for i in range(len(claves))}
print("Diccionario creado:", diccionario)

print("\n")
# Ejercicios 4:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Transpuesta con List Comprehension:", transpuesta_comprehension)

print("\n")
# Ejercicios 5:
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)

print("\n")
# Ejercicios 6:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", transformados)


