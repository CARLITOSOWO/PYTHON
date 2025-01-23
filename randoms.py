import random
"""
¿Cómo se pueden generar números y selecciones aleatorias con Random?
La generación de números y elecciones aleatorias es una tarea comúnmente 
requerida, y la librería Random en Python nos ofrece varias herramientas útiles para este propósito.
¿Cómo generar un número entero aleatorio?
Para generar números al azar dentro de un rango específico, randint es extremadamente práctica.
"""

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

"""
¿Cómo elegir un elemento aleatorio de una lista?
Podemos usar Random para hacer selecciones aleatorias de listas predefinidas. Supongamos que queremos elegir un color al azar.
Aquí, usamos choice para realizar selecciones impredecibles, lo cual es ideal para situaciones que requieren diversidad o variación en los resultados.
"""
#Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)
"""
¿Cómo desordenar una lista?
Si deseamos barajar o mezclar elementos de una lista, shuffle es el método indicado.
Esta función reordena los elementos de la lista, dejando abierta un sinfín de 
aplicaciones posibles, desde juegos de cartas hasta simulaciones.

Cada librería de la biblioteca estándar de Python ofrece una amplia gama de posibilidades
para el aprendizaje y la automatización de tareas cotidianas. Continúa explorando la documentación
y descubre más funcionalidades que enriquecerán tus aplicaciones.
"""
#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)