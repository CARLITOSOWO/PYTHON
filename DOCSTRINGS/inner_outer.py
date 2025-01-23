x = 'global' #Variable global

#Función externa
def outer_function():
    x = 'enclosing'
    #Función interna
    def inner_function():
        x = 'local' #Variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)


"""
PODEMOS DEFINIR FUNCIONES DENTRO DE LAS MISMA 
RESPETA EL NIVEL DE IDENTACION PARA QUE LAS VARIABLES PUEDAN FUNCIONAR 
Y NO GENEREN ERRORES AL MOMENTO DE UTILIZARLAS 

"""