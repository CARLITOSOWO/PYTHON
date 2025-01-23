"""
IMPLEMENTA UN SISTEMA DE GESTION DE PEDIDOS UTILIZANDO COLECCIONES Y ENUMERACIONES

"""

from collections import defaultdict, Counter
from enum import Enum


def contador_productos(orders: list[str]) -> defaultdict: #ESTABLECE UN VALOR POR DEFECTO 
    #Crea un diccionario con valor por defecto 0 
    cuenta = defaultdict(int)
    for productos in coleccion:
        cuenta[productos] +=1
    return cuenta

coleccion = ['MANDO','XBOX','HDMI','FUENTE_PODER','MONITOR','PC','TECLADO','ADAPTADOR_USB','CAPTURADORA','MOUSE',
             'MANDO','XBOX','HDMI','FUENTE_PODER','MONITOR','PC','TECLADO','ADAPTADOR_USB','CAPTURADORA','MOUSE',
             'MANDO','XBOX','HDMI','FUENTE_PODER','MONITOR','PC','PC','PC','PC','PC','LAPTOP'
             ]



cuentas = contador_productos(coleccion)
print(cuentas)
print('AHORA VA EL CONTADOR DE VENTAS LAS CUALES SON:')


def contador_ventas(products: list[str]) -> Counter:
    # Usa Counter para contar cuántos productos de cada tipo se han vendido
    return Counter(products)

result = contador_ventas(coleccion)
print(result) 

"""
Counter SIRVE PARA CONTAR CUANTOS PRODUCTOS SE HAN VENDIDO 
LA DIFERENCIA ES QUE EL VALOR POR DEFECTO 
"""


class OrderStatus(Enum):
    PENDIENTE = 1 #Pendiente
    ENVIADO = 2 #Enviado
    ENTREGADO = 3 #Entregado
    PERDIDO = 4 #Perdido


def revisar_estatus_orden(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDIENTE:
        return "LA ORDEN ESTA PENDIENTE."
    elif status == OrderStatus.ENVIADO:
        return "LA ORDEN FUE ENVIADA"
    elif status == OrderStatus.ENTREGADO:
        return "LA ORDEN FUEN ENTREGADA."
    elif status == OrderStatus.PERDIDO:
        return "EL PAQUETE SE PERDIO EN EL CAMINO OPS."
    
print(revisar_estatus_orden(OrderStatus.PERDIDO)) 





































