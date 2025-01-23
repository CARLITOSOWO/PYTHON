# Una Comprehension List es una forma concisa de crear listas en Python
# pues permite generar listas nuevas transformando cada elemento de una
# colección existente o creando elementos a partir de un rango.
# La sintaxis es compacta y directa, lo que facilita la comprensión del
# propósito de tu código de un vistazo.

# La estructura básica de una Comprehension List es:

# [expresión for elemento in iterable if condición]

# Las Comprehension Lists en Python son una herramienta poderosa y versátil 
# que permite escribir código más limpio y eficiente. Al dominar su uso, puedes
# realizar transformaciones y filtrados de datos de manera más concisa, lo que no solo
# mejora la legibilidad del código, sino que también puede optimizar su rendimiento.
# EJERCICIOS EN ARCHIVO clase15_ejercicios

squares = [x ** 2 for x in range(1,11)]
print("LOS CUADRADOS SON :" , squares)


celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius ]
print("\n")
print("TEMPERATURA EN GRADOS F:", fahrenheit)
print("\n")


#NUMEROS PARES 
print ("IMPRESION DE NUMEROS PARES ")
evens = [x for x in range (1,21) if x%2 ==0]
print (evens)
print("\n")


##MATRICES 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range (len(matrix[0]))]

print("MATRIX")
print (matrix)
print("\n")
print("TRAS")
print (transposed)







