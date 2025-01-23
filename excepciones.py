# EL TRY - EXCEPT SIRVE PARA PODER MOSTRAR UN ERROR O DAR UNA DESCRIPCION DE QUE ESTA FALLANDO EN EL 
# CODIGO  NOSOTROS COMO PROGRAMADARES TENEMOS QUE HACER TRATAMIENTOS DE LOS ERRORES QUE PUEDEN SER 
# POR PARTE DE NOSOTROS O DEL LADO DEL USUARIO PERO SIN QUE EL CODDIGO SE ROPA O SE DETENGA 
# PERO TAMBIEN TRATAR DE DARLE UNA MENSAJE O UNA SOLUCION
# CADA TRY DEBE DE TENER SU EXCEPT 

try:
    divisor = int(input("INGRESE UN NUMERO DIVISOR: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e: # POR BUENA PRACTICA ES RECOMENDABLE POR EL TIPO DE ERROR 
    print("ERROR: EL DIVISIR NO PUEDE SER CERO")
    print("HA OCURRIDO UN ERROR",e)
except ValueError as e: # POR BUENA PRACTICA ES RECOMENDABLE POR EL TIPO DE ERROR 
    print("ERROR: DEBES INTRODUCIR UN NUMERO VALIDO")
    print("HA OCURRIDO UN ERROR",e)

# PODEMOS CAPTURAR LA EXCEPCION PARA PODER MOSTRAR DONDE SE ESTA EQUIVOCANDO 

# LAS EXCEPCIONES TIENEN CLASES PADRES Y CLASES HIJOS EN LAS 
# CUALES PODEMOS TRATAR A CADA UNO DE LOS HIJOS 
# O AL PADRE Y ESTE ABARQUE A TODOS SUS HIJOS 

# ESTE CODIGO MOSTRARA LOS TIPOS DE EXCEPCIONES
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)


