"""
1.-UN METODO ESTATICO PARA VERIFICAR SI EL MONTO DE UN PEDIDO 
ES MAYOR A UN MINIMO PERMITIDO (POR EJEMPLO, $50).

2.-UN METODO DE CLASE QUE PERMITA CREAR UN PEDIDO APLICANDO UN DESCUENTO GLOBAL 
"""

#CREAMOS UNA CLASE  CON UNA VARIABLE GLOBAL 
class Order:
    global_discount =10
    def __init__(self,amount): #CREAMOS UN CONSTRUCTOR CON LA VARIABLE INICIALIZADA amount
        self.amount = amount
    @classmethod #CREAMOS UNA LLAMADA DE CLASE 
    def update_global_discount(cls, new_discount): #CREAMOS UN METODO QUE ACTUALIZA EL DESCUENTO EL CUAL RECIBE COMO PARAMETRO UNA CLASE Y LA VARIABLE
        cls.global_discount = new_discount # LLAMAMOS A LA VARIABLE GLOBAL DE LA CLASE Y LE ASIGANMOS UN VALOR DE OTRA VARIABLE QUE EN UN FUTURO SERA MODIFICADO 
        
    @staticmethod #CREWAMOS UNA LLAMADA A UN METODO ESTATICO 
    def calculate_mount(amount): #CREAMOS EL METODO calculate_mount EL CUAL RECIBE COMO PARAMETRO amount
        if amount < 50 : #SI amount ES MENOR QUE 50 ENTONCES 
            return f"El monto es menor que el minimo permitido '{amount}'"
        else : #SINO 
            return f"El monto es mayor que el minimo permitido '{amount}'"
    @classmethod #CREAMOS UNA LLAMADA DE CLASE
    def discount(cls,amount): #CREAMOS UN METODO LLAMADO discount EL CUAL RECIBE COMO PARAMETRO UNA CLASE Y LA VARIABLE amount
        new_amount = amount - (amount*(cls.global_discount/100)) #OPERACION PARA CALCULAR EL NUEVO DESCUENTO 
        return f"El monto {amount} tiene un descuento global de {cls.global_discount} porciento el monto ajustado es {new_amount}"

print(Order.calculate_mount(50))
print(Order.global_discount)
Order.update_global_discount(10)
print(Order.global_discount)
print(Order.discount(300))
