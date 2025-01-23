x = 5 #Variable global

def modify_global():
    global x
    x+=3
    print(f'Valor modificado: {x}')

modify_global()
print(x)


"""
LAS VARIABLES GLOBALES CAMBIAN SI ESTAS FUERON ALTERADAS POR UNA FUNCION COMO EN EL 
CODIGO ANTERIROR DONDE X ENTRA VALIENDO 5 DESPUES DE LA MODIFICACION SU VALOR GLOBAL ES DE 8 
"""