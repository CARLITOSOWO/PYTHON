# DICCIONARIOS EN PYTHON 
# PARA ESPECIFICAR EL USO DE DICCIONARIOS EN PYTHON USAMOS LA LLAVES EN LA DECLARACION 
print("CREACION DE DICCIONARIO DE DATOS _____________OwO")
numbers ={1:"uno", 2:"dos", 3:"tres"}
print (numbers)


# AL IGUAL QUE LAS LISTAS POR MEDIO DE LA INDEXACION PODEMOS ACCEDER A UN ELEMENTO DEL DICCIONARIO 
print("INDEXACION CON DICCIONARIO DE DATOS _____________OwO")
dic_inde ={1:"OwO", 2:"O_O", 3:"O.O"}
print (dic_inde[2])


# COMO BORRA ELEMENTO DE UN DICCIONARIO 
# ESTO SE HACE MEDIANTE UNA LLAVE LA CUAL ES LA QUE DEFINIMOS AL MOMENTO DE CREARLO QUE ES LO QUE ESTA A LA IZQUIERDA DE LOS DOS PUNTOS ":"
print("ELIMINACION DE DATOS POR MEDIO DE LLAVE O IDENTIFICADOR _____________OwO")
information = {"Nombre": "CARLOS",
                 "Apellido": "Lopez",
                "Altura": "1.70",
                "Edad": "27"
                }
print ("ANTES DE BORRAR LA INFORMACION")
print (information)
del information ["Edad"]
print ("DESPUES DE BORRAR LA INFORMACION")
print (information)


# METODOS  KEYS PARA BUSCAR LAS LLAVES DEL DICCIONARIO 
print("METODO KEYS _____________OwO")
claves = information.keys()
print (claves)
print("TIPO DE DATO_____________OwO")
print (type(claves))


# EL METODO VALUES SIRVE PARA PODER VER EL VALOR DE LAS LLAVES 
print("METODO VALUES PARA PODER VER EL VALOR DE LAS LLAVES_____________OwO")
values = information.values()
print (values)


# TAMBIEN PODEMOS EJECUTAR LOS PARES DE VALOR (CADA LLAVE CON SU RESPECTIVO VALOR) CON LA FUNCION "items"
print("PARES DE VALOR_____________OwO")
pares = information.items()
print(pares)

#AGENDA
print ("AGENDA DE CONTACTOS_____________OwO")
contactos = {
                "CARLOS D":{
                "Apellido": "Lopez",
                "Telefono": 5574242058,
                "Edad": 27
                }
                ,
                "RODRIGO":{
                "Apellido": "MORALES",
                "Telefono": "5566884422",
                "Edad": 15
                }
                ,
                "AARON":{
                "Apellido": "URBINA",
                "Telefono": 551122334455,
                "Edad": 19
                }
                ,
                "JULIO":{
                "Apellido": "URBINA",
                "Telefono": 55777888999444,
                "Edad": 15
                }
                ,
                "ROMINA":{
                "Apellido": "URBINA",
                "Telefono": 554466446646646,
                "Edad": 9
                }
                ,
                "JEANTTE":{
                "Apellido": "ABADIA",
                "Telefono": 554477885533,
                "Edad": 40
                }

}

print (contactos["CARLOS D"])



print ("AGENDA DE CONTACTOS_____________OwO")
contactos = {
                "CARLOS D":{
                "Apellido": "Lopez",
                "Telefono": 5574242058,
                "Edad": 27
                }
                ,
                "RODRIGO":{
                "Apellido": "MORALES",
                "Telefono": "5566884422",
                "Edad": 15
                }
                ,
                "AARON":{
                "Apellido": "URBINA",
                "Telefono": 551122334455,
                "Edad": 19
                }
                ,
                "JULIO":{
                "Apellido": "URBINA",
                "Telefono": 55777888999444,
                "Edad": 15
                }
                ,
                "ROMINA":{
                "Apellido": "URBINA",
                "Telefono": 554466446646646,
                "Edad": 9
                }
                ,
                "JEANTTE":{
                "Apellido": "ABADIA",
                "Telefono": 554477885533,
                "Edad": 40
                }

}









