# LA FUNCION LAMBDA FUNCIONA COMO UNA ATAJO EN EL MOMEMTO DE CREAR FUNCIONES SIMPLES QUE SOLO CUMPLEN 
# CON UNA OPERACION ESTA SOLO ESPERA LOS PARAMETROS NECESARIO PARA REALIZAR DICHA OPERACION

add = lambda a , b: a + b 
print(add(10,4))


resta = lambda a , b: a - b 
print(add(10,4))

#CUADRADO DE UN NUMERO

numeros =range(11)

secuencia_numeros = list(map(lambda x: x**2, numeros))
print("CUADRADO :", secuencia_numeros)


#FILTER  UNA MANERA DE SELECCIONAR ALGUN ELEMENTO SI CUMPLE UNA CONDICION
print("\n")
print("OPTENER LOS NUMEROS PARES") 
evento_numbers = list(filter(lambda x: x%2 ==0, numeros))
print("LOS NUMEROS PARES SON :", evento_numbers)



