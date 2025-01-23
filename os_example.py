import os
"""
¿Cómo utilizar la librería OS en Python para trabajar con archivos y directorios?
Interactuar con el sistema operativo desde Python es una tarea que se hace mucho más 
sencilla gracias a la librería OS. Sin necesidad de instalaciones adicionales, esta herramienta 
permite automatizar y manejar archivos y directorios, lo que simplifica enormemente el flujo de trabajo.
Veamos algunos ejemplos prácticos de su uso.

¿Cómo obtener el directorio de trabajo actual?
La librería OS nos facilita la tarea de conocer en qué carpeta estamos trabajando. 
Esto es especialmente útil cuando deseamos manipular archivos en nuestro directorio actual 
sin tener que especificar rutas absolutas.
"""


#Obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

"""
Cuando ejecutas este código, Python te indicará el directorio 
corriente en el que te encuentras, ayudándote a tener un mejor control sobre tu ubicación en el sistema de archivos.


¿Cómo listar archivos de cierto tipo?
Muchas veces, necesitamos desplegar una lista de archivos de un tipo específico, como los archivos de texto.
"""
#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

"""
En este snippet, usamos list comprehension para filtrar y obtener solo los archivos que terminan con .txt, facilitando así su manipulación posterior.
"""
"""
¿Cómo renombrar un archivo?
Renombrar archivos es otra funcionalidad que podemos implementar fácilmente con OS. Supongamos que queremos cambiar el nombre del archivo caperucita.txt a cuento.txt.
"""

#Renombrar archivo
os.rename('caperucita.txt', 'cuento.txt')
print('Archivo renombrado')
"""
Así podrás modificar nombres de archivos de manera simple y rápida, ayudando a mantener tus directorios organizados.
"""
#Listar los archivos .txt PARA MOSTRAR EL CAMBIO 

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)