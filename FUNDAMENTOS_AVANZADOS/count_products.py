from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict: #ESTABLECE UN VALOR POR DEFECTO 
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)



"""
ES UNA FUNCION QUE CUENTA PRODUCTOS  DE UNA COLECCION QUE NOSOSTROS VAMOS A USAR 

defaultdict ESTABLECE UN VALOR POR DEFECTO EN CASO DE QUE ESTE NO EXISTA EN LA COLECCION 


"""