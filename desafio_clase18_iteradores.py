print ("\n")
print("ITERAR CON NUMEROS PARES E IMPARES")
# RANGE
#CREAR ITERADOR PARA NUMEROS IMPARES

# LIMITE
limit = 25

# LA FUNCION RANGE ACEPTA 3 VALORES 
# EL INICION DE LA ITERACION EN ESTA CASO ES 1
#  EL LIMITE DE LA ITERACION EN ESTE CASO ES LA VARIABLE LIMIT+1
#  Y DE CUANTO EN CUANTO VA A IR ITERANDO EN ESTE CASO 2

#CREAR ITERADOR
impares = iter(range(1,limit+1,2))
pares = iter(range(0,limit+1,2))

# USAR ITERADOR
print("NUMEROS IMPARES")
for num in impares:
    print(num)

print("\n")

print("NUMEROS PARES")
for num2 in pares:
    print(num2)

print ("\n")
print("ITERAR CON NUMEROS PARES E IMPARES CON  DATOS DE TECLADO")
# RANGE
#CREAR ITERADOR PARA NUMEROS IMPARES
# LIMITE
limite_teclado = int(input ("INGRESE EL LIMITE: "))

limit_tec = limite_teclado

# LA FUNCION RANGE ACEPTA 3 VALORES 
# EL INICION DE LA ITERACION EN ESTA CASO ES 1
#  EL LIMITE DE LA ITERACION EN ESTE CASO ES LA VARIABLE LIMIT+1
#  Y DE CUANTO EN CUANTO VA A IR ITERANDO EN ESTE CASO 2

#CREAR ITERADOR
impares_tec = iter(range(1,limit_tec+1,2))
pares_tec = iter(range(0,limit_tec+1,2))

# USAR ITERADOR
print("NUMEROS IMPARES")
for num_tec in impares_tec:
    print(num_tec)

print("\n")

print("NUMEROS PARES")
for num_tec2 in pares_tec:
    print(num_tec2)