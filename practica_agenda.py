contactos2 = {
"JEANETTE":{
"NOMBRE" : "JEANETTE",
"APELLIDO" : "ABADIA",
"Telefono": 554477885533,
"Edad": 40
}
,
"CARLOS":{
"NOMBRE" :"CARLOS",
"APELLIDO" : "LOPEZ",
"Telefono": 5574242058,
"Edad": 27
}
,
"RODRIGO":{
"NOMBRE" : "RODRIGO",
"APELLIDO" : "MORALES",
"Telefono": 555555555555,
"Edad": 15
}
}

# METODOS  KEYS PARA BUSCAR LAS LLAVES DEL DICCIONARIO 
print("SELECCIONE EL CONTACTO PARA VER LA INFORMACION")
llaves = contactos2.keys()
print (llaves)
nombre = input("INGRESE EL NOMBRE AL CUAL QUIERE ACCEDER A LA INFORMACION:")
print (contactos2[nombre])




