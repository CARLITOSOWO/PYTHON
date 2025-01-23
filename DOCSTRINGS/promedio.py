def calculate_average(numbers):
    """
    Calcula el promedio de una lista de numeros 

    Parametros:
    numbers (list): Una lista de numeros enteros o flotantes 

    Retorna:
    float: El promedio de los numeros en la lista
    """
    return sum(numbers) / len(numbers)

#Imprimiendo el resultado de la funcion 
print(calculate_average([1,2,3,4,5]))



"""
Los docstrings en Python son cadenas de texto utilizadas para documentar el propósito, 
uso y detalles de una función, clase o módulo. Se colocan al inicio de una función, clase 
o archivo, y permiten describir lo que hace el código, sus parámetros, valores de retorno 
y cualquier otro detalle relevante. Son esenciales para hacer el código más comprensible y 
facilitar su uso tanto para el desarrollador como para otros que lo puedan leer.

Propósitos de los Docstrings:
Documentación del código: Los docstrings sirven para explicar qué hace una función o clase 
y cómo se debe usar, lo cual es útil tanto para el propio programador como para otros 
colaboradores en el proyecto.
Generación automática de documentación: Herramientas como Sphinx pueden utilizar los 
docstrings para generar documentación automática de tu código.
Facilidad de uso: Al usar la función help() en Python, puedes acceder a los docstrings 
y obtener información rápida sobre la función, clase o módulo.
Estilo de codificación: Los docstrings forman parte de las buenas prácticas de 
programación en Python (PEP 257) y ayudan a mantener el código limpio y bien estructurado.
Sintaxis de un Docstring:
El docstring se coloca inmediatamente después de la definición de la función, 
clase o módulo, y debe estar entre comillas triples 

"""