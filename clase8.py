# LISTAS LA PALABAR list ES UNA PALABRA RESERVADA EN PYTHON 


to_do = ["IR AL HOTEL",
         "IR A COMER",
         "MUSEO",
         "REGRESAR AL HOTEL"]

print (to_do)

numeros = [1,2,3,4, "cinco"]
print (numeros)

mix = ["uno" , 2 , 3.14 , True , [1,2,3] ] 
print (mix)
#EN LAS LISTAS PODEMOS CONTAR LOS ELEMENTOS GUARDADOS CON LA FUNCION "len"
print (len (mix))


# INDEXACION CON ELLA PODEMOS DEFINIR EL VALOR QUE QUEREMOS MOSTRAR DE LA LISTA DEFINIENDO ENTRE LOS [] EL INDICE DEL VALOR 
# SI QUEREMOS EMPEZAR CON LOS ELEMENTOS DEL FINAL USAMOS NUMEROS NEGATIVOS COMO EN EL EJEMPLO "ULTIMO ELEMENTO"
print ("PRIMER ELEMENTO :" , mix [0])
print ("SEGUNDO ELEMENTO :" , mix [1])
print ("ULTIMO ELEMENTO :" , mix [-1]) # ULTIMO ELEMENTO

# SLICING PODEMOS EXTRAER PORCIONES DE LA INFORMACION PARA PODER USAR EL SLICING DEBEMOD DEFINIR CON DOS PUNTOS EL INICIO : EL FINAL
ejemplo_slicing = "ESTE ES U EJEMPLO DEL SLICING"
print (ejemplo_slicing [2:4])

#AL IGUAL QUE QUE LAS CADENAS LAS LISTAS TIENE FUNCIONES___
# CON LA FUNCION "append" PODEMOS AGREGAR UN ELEMENTO AL FINAL DE LA LISTA YA DEFINIDA 
# LAS LISTAS DENTRO DE LAS LISTAS SON INDEPENDIENTES CON LA FUNCION "append" NO PODEMOS AGREGAR ELEMENTOS EN ELLAS 
nota = "FUNCION PARA AGREGAR ELEMENTO AL FINAL DE LA LISTA"
print (nota)
print (" _________________ OwO")
mix2 = ["uno" , 2 , 3.14 , True , [1,2,3] , "MIX 2" ] 
print (mix2)
mix2.append(False) #
print (mix2)

# INSERT ES LA FUNCION QUE SIRVE PARA INSERTAR ELEMENTOS EN EL LISTADO EN LA POSICION QUE LE INDIQUEMOS
nota2 = "FUNCION PARA INSERTAR UN ELEMENTO EN LA POSICION QUE INDIQUEMOS"
print (nota2)
print (" OwO_________________ OwO")
mix3 = ["INSERT" , "OwO" , "UuU" , "U_U" , "O_O" , "MIX 3" ] 
mix3.insert(1,["^_____^","^_^"]) #
print (mix3)

# EN LAS LISTAS TAMBIEN PODEMOS CONSULTAR CUAL ES LA POSICION O LA PRIMER APARACION DE UN ELEMENTO 
# INDEX SOLO DEVUELVE LA PRIMER APARACION DEL ELEMENTO 
print (mix3.index(["^_____^","^_^"]))


# CUANDO TRABAJAMOS CON LISTAS CON ELEMENTOS DE TIPO FLOAT O INT PODEMOS CONSULATR CUAL ES EL ELEMENTO MAYOR Y CUAL ES EL ELEMENTO MENOR 
num = [1,2,3,4,5,6,7,8,9,100,88,]
print("ELEMENTEO MAYOR DE LA LISTA: ",max(num))
print("ELEMENTEO MENOR DE LA LISTA: ",min(num))

# PODEMOS ELIMINAR ELEMENTOS DE LA LISTA O LA LISTA ENTERA CON LA FUNCION "DEL"
nota3 = "FUNCION PARA ELIMINAR UN ELEMENTO EN LA LISTA QUE INDIQUEMOS O LA LISTA COMPLETA"
print (nota3)
nume_borrar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print (nume_borrar)
del nume_borrar[-1] #PARA ELIMINAR UN DATO EN ESPECIFICO DE ACUERDO A SU POSICION
print (nume_borrar)
del nume_borrar[:2] #PARA ELIMINAR UN RANGO DE DATOS
print (nume_borrar)
del nume_borrar #PARA ELIMINAR LA LISTA COMPLETA
print (nume_borrar)

