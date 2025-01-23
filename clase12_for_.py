# EL CICLO FOR SU ESTRUCTURA ES LA SIGUIENTE 
numbers = [1, 2, 3, 4, 5, 6]

for  i  in numbers:
    print("AQUI EL VALOR DE i ES IGUAL A ",i+1)

print("\n")
print ("FUNCION FOR CON UN RANGO ESTABLECIDO ")
# TAMBIEN PODEMOS ITERAR EN UNA COLECCION DE DATOS DONDE LE DAMOS EL INICIO Y EL FINAL CON RANGE
#RANGE SOLO DARA EL RESULTADO HASTA UN NUMERO ANTES DEL DEFINIDO EN EL RANGO DE 10 SERA 9 COMO EN EL EJEMPLO
for i in range(10):
    print(i)

print("\n")
print ("FUNCION FOR CON UN RANGO ESTABLECIDO DE 3 A 10 ")
# SI QUEREMOS QUE INICIE DESDE ALGUN NUMERO SOLO TENEMOS QUE DEFINIRLO 
for u in range(3,10):
    print(u)

print("\n")
print("FOR CON IF")
# EN EL FOR TAMBIEN PODEMOS UTILIZAR LA CONDICIONAL IF 
frutas_ricas = ["Manzana","Pera","Uva","Naranja","Tomate"]
for fruta in frutas_ricas:
    print(fruta)
    if fruta == "Naranja":
        print("NARANJA ENCONTRADA ")


print("\n")
print("WHILE ___")
# WHILE MIENTRAS SE CUMPLA UNA CONDICION VAMOS A ENTRAR DENTRO DEL CUERPO DEL WHILE
# EN EL WHILE DEBEMOS CONSIDERAR QUE EN ALGUN PUNTO DEBEMOS MODIFICAR LA CONDICIONAL PARA EVITAR BUCLES INFINITOS
x = 0
while x < 5:
     if x ==3:
         break
     print (x)
     x +=1 #MODIFICACION PARA EVITAR BUCLES INFINITOS


print("\n")
print("CONTINUE ___")
# VAN A HABER CASOS DONDE QUERAMOS OMITIR UNA CONDICION O EL PASO SIGUIENTE PARA ELLO SUAMOS CONTINUE
numbers = [1, 2, 3, 4, 5, 6]
for  i  in numbers:
    if i ==3:
        continue
    print("AQUI SE SALTO EL VALOR DE 3:__ ",i)

