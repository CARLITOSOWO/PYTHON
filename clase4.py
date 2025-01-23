name = "ESTE MENSAJE ES CON COMILLAS DOBLES"
name2 = 'ESTE MENSAJE ES CON COMILLAS SIMPLES'
name3 = '''ESTE MENSAJE 
ES CON COMILLAS TRIPLES Y PERMITE UN SALTO DE LINEA '''

print(type(name)) 
print(type(name2))
print(type(name3))

print(name)
print(name2)
print(name3)

# CON LA FUNCION type pedimos el tipo de dato de la variable que encierran los ()
# EXISTEN 3 MANERAS DE IDENTIFICAR LAS CADENAS DE CARACTERES
# 1.- LAS COMILLAS DOBLES ""
# 2.- LAS COMILLAS SIMPLES ''
# 3.- LAS COMILLAS TRIPELS  '''
# LAS COMILLAS DOBLES Y SIMPLES NO PERMITEN EL SALTO DE LINEA LAS TRIPLES SI 

print("_____ LA INDEXACION NOS PERMITE VER EL CARACTER EN LA POSICION QUE INDIQUEMOS")


# INDEXACION NOS PERMITE VER EL CARACTER EN LA POSICION QUE INDIQUEMOS PARA PODER VER LOS CARACTERES COMENZANDO DEL FINAL AL COMIENZO 
#PODEMOS USAR LOS NUMERO NEGATIVOS 
# EJEMPLO 
# C = 0     C = -5
# A =1      A = -4
# R =2      R = -3
# L =3      L = -2
# O =4      O = -1
# S =5      S = -0
print ("PRUEBA DE INDEXACION CON POSITIVOS")

indexacion = "CARLOS"
print (indexacion[0])
print (indexacion[1])
print (indexacion[2])
print (indexacion[3])
print (indexacion[4])
print (indexacion[5])

print ("PRUEBA DE INDEXACION CON NEGATIVOS")
print (indexacion[-0])
print (indexacion[-1])
print (indexacion[-2])
print (indexacion[-3])
print (indexacion[-4])
print (indexacion[-5])


# CONCATENACION 
#LA CONCATENACION ENC ADENA DE CARACTERES NO APLICA LOS ESPACIOS PARA ELLO SE DEBE DE AGREGAR + " " + EL ESPACION EN LA IMPRESION
print("CONCATENACION ______")

nombre = "CARLOS DAVID"
apellido = "LOPEZ ABADIA  "

print (nombre *5)
print (nombre + " " + apellido)

# BUENAS PRACTICAS UN CONSEJO ES QUE DEBEMOS DE RESPETAR EL TIPO DE COMILLAS QUE USAMOS EN LA DECLARACION DE NUESTRAS VARIABLES 
# PARA PODER REPLICAR LAS CADENAS USAMOS EL SIMBOLO * Y LE INDICAMOS EL NUMERO DE VECES


# LONGITUD SIRVE PARA PODER CONTAR LA CADENA O CUANTOS CARACTERES EXISTEN Y LO HACEMOS CON LA FUNCION "len" EL ESPACIO TAMBIEN ES UN 
# CARACTER
print("LONGITUD CON LA FUNCION len ______")

print (len(nombre))
print (len(apellido))


# METODOS 
# EL METODO lower CONVIERTE MAYUSCULAS A MINUSCULAS 
# EL METODO upper ES EL INVERSO DE lower PASA LOS CARACTERES A MAYUSCULAS 
# EL METODO strip ELIMINA LOS ESPACIOS EN BLANCO 

metodo_lower = "CON ESTE METODO CAMBIAMOS A MINUSCULAS"
metodo_upper = "con este medoto cambiamos a minusculas"
metodo_strip = " CON ESTE METODO ELIMINAMOS LOS ESPACIOS EN BLANCO     "



print("FUNCION LOWER_UPPER_STRIP_____")
print (metodo_lower.lower())
print (metodo_upper.upper())
print (metodo_strip.strip())
