#EJEMPLO DE ITERADOR 

#CREAMOS UNA LISTA
my_lista = [1,2,3,4]

#OBTENEMOS EL ITERADOR
my_iterador = iter(my_lista)

#USAR EL ITERADOR
print(next(my_iterador))
print(next(my_iterador))
print(next(my_iterador))
print(next(my_iterador))
# print(next(my_iterador))
# AL IMPRIMIR UNA VEZ MOSTRADOS TODOS LOS VALORES DE LA LISTA MARCARA ERROR POR QUE YA NO CUENTA CON INFORMACION PARA MOSTRAR Y NO PUEDE VOLVER
# EN LA POCISION DE LA LISTA 

#NEXT NO AYUDA A SABER CUALES SON LOS VALORES QUE SE VAN GUARDANDO EN MEMORIA 

print ("\n")
print("ITERAR EN CADENAS O STRING")
# CREACION DE CADENA 
text = "Hola mundo"

# CREANDO EL OBJETO ITERADOR
iter_text = iter(text)

# ITERAR EN LA CADENA 
for char in iter_text:
    print(char)




print ("\n")
print("ITERAR CON RANGE")
# RANGE
#CREAR ITERADOR PARA NUMEROS IMPARES

# LIMITE
limit = 10

# LA FUNCION RANGE ACEPTA 3 VALORES 
# EL INICION DE LA ITERACION EN ESTA CASO ES 1
#  EL LIMITE DE LA ITERACION EN ESTE CASO ES LA VARIABLE LIMIT+1
#  Y DE CUANTO EN CUANTO VA A IR ITERANDO EN ESTE CASO 2

#CREAR ITERADOR
odd_itter = iter(range(1,limit+1,2))

# USAR ITERADOR
for num in odd_itter:
    print(num)


print ("\n")
print("ITERAR CON UN GENERADOR")
# GENAERADOR ES UNA FUNCION QUE PRODUCE UNA SERIE DE NUMEROS EN LOS CUALES PODEMOS ITERAR 
# YA NO VAMOS A USAR LA PALABRA RESERVADA RETURN PARA DEVOLVER UN VALOR SINO QUE AHORA VAMOS A USAR LA PALABARA YIELD
def my_generador():
    yield 1
    yield 2
    yield 3

for value in my_generador():
    print(value)


print ("\n")
print("ITERAR CON SERIE DE FIBONACCI")
# TAMBIEN SE PUEDE USAR EN LA SERIE DE FIBONACCI 
# EXPLICACION CORTA DE SERIE DE FIBONACCI ES OBTENER UN NUMERO SUMANDO LOS DOS ANTERIORES 
# EJEMPLO 
# 0 1 1 2 3 5 8 13 21...

def fibonacci(limit):
    a, b = 0, 1 #SE DEFINEN DOS VARIABLES EN UNA SOLA LINEA DE CODIGO 
    while a < limit:
        yield a 
        a, b = b, a+b

for num in fibonacci(10):
    print(num)

