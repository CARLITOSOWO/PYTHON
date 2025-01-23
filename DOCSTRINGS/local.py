x = 100 #variable global

def local_function():
    x = 10 #Variable local
    print(f'El valor de la variable es {x}')

def show_global():
    print(f'El valor de la variable global es {x}')

#local_function()
print(x) 

"""
LA IDENTACION TAMBIEN APLICA A LAS VARIABLES DE TIPO LOCAL Y GLOBAL SI LA VARIABLE ESTA DEFINIDA EN UNA FUNCION SERA DE TIPO LOCAL Y NO SE PODRA 
ACCEDER A ELLA DE MANERA GLOBAL 
"""