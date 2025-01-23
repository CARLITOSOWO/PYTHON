"""
CREA UN MODLUO LLAMADO finance.py QUE CONTENGA FUNCIONES 
PARA CALCULAR EL BALANCE DE UN MES (DIFERENCIA ENTRE INGRESOS Y GASTOS )
Y DETERMINAR SI EL MES HAS SIDO RENTABLE 

1.-LA FUNCION calculate_balance(income,expenses) DEBE DEVOLVER LA 
DIFERENCIA ENTRE INGRESOS Y GASTOS 

2.-DEVOLVER TRUE SI EL BALANCE ES POSITIVO Y FALSE SI ES NEGATIVO 
"""

def calculate_balance(income,expenses):
    balance = income - expenses
    if balance < 0:
        return f'El balance es $ {balance} -> {False}'
    else:
        return f'El balance es $ {balance} -> {True}'



#ESTA PARTE DEL CODIGO VA EN OTRO ARCHIVO .py LLAMADO reports
from reports import calculate_balance

balance = calculate_balance(400,100)
print(balance)

balance_2 = calculate_balance(100,600)
print(balance_2)

