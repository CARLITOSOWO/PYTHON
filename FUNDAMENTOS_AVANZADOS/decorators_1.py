def log_transaction(func):
    def wrapper():
        print('1 Log de la transacción...')
        func()
        print('3 Log terminado...')
    return wrapper
        

@log_transaction
def process_payment():
    print('2 Procesando pago....')

process_payment()





"""
Los decoradores en Python son funciones que modifican el comportamiento 
de otras funciones o métodos. Son una herramienta muy útil para añadir 
funcionalidades o preprocesamientos sin tener que cambiar el código original 
de la función decorada.

SIREVN PARA MODIFICAR LOS COMPORTAMIENTOS DE LAS FUNCIONES YA SEA ANTES O DEPUES 
ESTOS SON LOS DECORADORES LOS CUALES COMO PARAMETRO SIEMPRE DEBEN DE RECIBIR UNA FUNCION 

wrapper(): SOLO ES UNA FUNCION CREADA PARA ENVOLVER A LA FUNCION QUE ESTAMOS LLAMANDO 


@log_transaction CON ESTA PARTE DE CODIGO ES QUE LLAMAMOS AL DECORADOR 
SU ESTRUCTURA ES @ + EL NOMBRE DE LA FUNCION QEU MODIFICA 


"""