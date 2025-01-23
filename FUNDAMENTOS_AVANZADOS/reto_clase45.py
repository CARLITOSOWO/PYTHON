"""
IMPLEMENTA UN DOCORADOR LLAMADO log_employee_action QUE 
REGISTRE CUALQUIER ACCION REALIZADA POR UN EMPLEADO 
EN UN ARCHIVO DE TEXTO 

SOLUCION 
1ER PASO 
CREE LAS FUNCIONES NECESARIAS PARA LOS REGISTROS DE ACTIVIDADES 
2DO PASO
CREE LOS DECORADORES DE CADA FUNCION Y LAS LINEAS DE CODIGO QUE LOS MANDAN A LLAMAR 
3ER PASO 
CON LA FUNCION open EN MODO 'W' WRITE/ESCRITURA CREE EL ARCHIVO TXT Y DEFINI LAS VARIABLES QUE 
ALMACENAN EL TEXTO QUE SE GUARDARA EN EL REGISTRO TXT
4TO PASO 
CON LA FUNCION writelines LLAME A LAS VARIABLES ANTES MENCIONADAS PARA QUE SE GRABEN LOS MENSAJES 

"""

def empleado_contratado ():
    print('HAY EMPLEADO CONTRATADO ?: \n')
    respuesta_teclado = int(input ("1 = SI 2 = NO"))
    if respuesta_teclado == 2:
        print('CONTRATA A UN EMPLEADO \n')
        x = False
    else:
        x = True
    return x





def marcar_entrada(func):
    def decorador():
        if empleado_contratado() == True:
            print('EL ACABA DE MARCAR ENTRADA')
            func()
        else:
            print('CONTRATA A UN EMPLEADO PRONTO')
    return decorador


def trabajando(func):
    def decorador2():
        print('EL EMPLEADO ESTA TRABAJANDO')
        func()
    return decorador2


def llamada_telefonica(func):
    def decorador3():
        print('EL EMPLEADO RECIBIO UNA LLAMADA DE UN CLIENTE')
        func()
    return decorador3





"""
@trabajando
@llamada_telefonica
"""
@marcar_entrada
def salida_comer():
    print('EL EMPLEADO SALIO A COMER')
    


salida_comer()



"""
    file = open("practica_45.txt","w")
    COM = ["EL EMPLEADO SALIO A COMER \n"]
    ENTR =  ["EL ACABA DE MARCAR ENTRADA \n"]
    TRA =  ["EL EMPLEADO ESTA TRABAJANDO \n"]
    TEL = ["EL EMPLEADO RECIBIO UNA LLAMADA DE UN CLIENTE \n"]


    file.writelines(COM)
    file.writelines(ENTR)
    file.writelines(TRA)
    file.writelines(TEL)
    file.close()
    """