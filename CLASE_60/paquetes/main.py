#Importa funciones de los modulos dentro del paquete (CARPETA)
from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sale

add_product('Laptop', 10)
remove_product('Laptop')
process_sale('Laptop', 2)


"""
DESDE MAIN ACCEDIMOS  A LAS FUNCIONES QUE ESTAN EN OTROS ARCHIVOS.py

SUBPAQUETE -> ES UNA CARPETA QUE SE ENCUENTRA DENTRO DEL PAQUETE PRINCIPAL
TIENE EXCATAMENTE LA MISMA ESTRUCTURA 

"""


