import math
"""
¿Cómo realizar cálculos matemáticos precisos con Math?
Cuando trabajamos con cálculos matemáticos en Python, la librería Math es una aliada invaluable. 
Ofrece una serie de funciones y constantes matemáticas, ideal para conseguir resultados precisos, como en el caso del número pi.

¿Cuál es la importancia de la constante pi?
Pi es una constante con decimales infinitos, y usarla con precisión es esencial para cálculos científicos o 
de ingeniería. La librería Math nos provee de pi con todos sus decimales disponibles.

Gracias a Math, obtenemos resultados matemáticamente precisos, que pueden ser fundamentales en diferentes aplicaciones científicas.
"""



#Hallar el area y perimetro de un circulo
radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)