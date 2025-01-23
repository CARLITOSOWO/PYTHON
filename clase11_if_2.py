x = 15
y = 20

# IF CON AND 
# EN ESTE CASO SE NECESITA QUE AMBAS CONDICIONES SE CUMPLAN 

if x > 10 and y > 25:
    print ("X es mayor que 10 YYYY y es mayor que 15 15")

# IF CON OR 
# LO QUE NECESITA OR ES QUE SOLO UNA DE LAS CONDICIONALES SE CUMPLA 

if x > 10 or y > 25:
    print ("X es mayor que 10 OOOO y es mayor que 25")

# IF CON NOT
# SIREV PARA NEGARUNA CONDICIONAL QUE NOSOSTROS QUERAMOS EVALUAR 

if not x > 10:
    print ("X NOT es mayor que 10")


print("\n")


# IF ANIDADOS SON IF DENTRO DE OTRO IF
# SE DEBE RESPETAR EL NIVEL DE IDENTACION PARA PODER APLICAR LOS ELSE DE CADA IF 
is_member = True
age = 11

if is_member:
    if age>=15:
        print("TIENES ACCESO POR SER MIEMBRO Y POR SER MAYOR")
    else:
        print("NO TIENES ACCESO YA QUE ERES MIEMBRO PERO MENOR DE 15 AÑOS")
else:
    print("NO ERES MIEMBRO Y NO TIENES ACCESO")


# DESAFIO DE CLASE EN ARCHIVO piedra papel o tijeras
