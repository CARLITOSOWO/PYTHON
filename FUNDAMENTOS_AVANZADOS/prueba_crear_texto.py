#Este programa muestra cómo escribir datos en un archivo de texto.This 

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

#Asignando ["This is Lagos \n","This is Python \n","This is Fcc \n"]  a 
#la variable L, se puede usar cualquier letra o palabra de tu elección.
#Las variables son contenedores en los que se pueden almacenar valores.
#El \n se coloca para indicar el final de la línea.

file.write("Hello There \n")
file.writelines(L)
file.close()

# Usar close() para cambiar los modos de acceso a archivos