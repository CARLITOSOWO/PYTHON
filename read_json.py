import json

#Lectura del archivo
with open('products.json', mode='r') as file:
    products = json.load(file)

#Mostrar el contenido
for product in products: #POR CADA VARIABLE_NUEVA DENTRO DE PRODUCTS 
    #print(product)
    print(f"Product: {product['name']}, Price: {product['price']}")




