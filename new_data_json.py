import json

file_path = 'products.json'

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)





# ¿Cómo leer archivos JSON en Python?
# JSON, que significa JavaScript Object Notation, es un formato liviano de intercambio de datos. 
# Es crucial para trabajar con datos en aplicaciones web y APIs. Aprender a manejarlo con Python es 
# esencial para desarrolladores que buscan eficiencia y flexibilidad.

# Para leer un archivo JSON en Python, sigue estos sencillos pasos:

# Importar la librería JSON: Primeramente, debes importar el módulo JSON de Python.

# import json
# Abrir el archivo JSON: Utiliza la función open para acceder al archivo. Asegúrate de especificar el modo de lectura.

# with open('Products.json', 'r') as file:
#     products = json.load(file)
# Iterar sobre el contenido: Una vez cargados los datos, puedes iterar sobre ellos como si fueran una lista de diccionarios.

# for product in products:
#     print(product)
# Cada producto se imprimirá con sus claves y valores gracias a la estructura de diccionario que utiliza JSON.

# ¿Cómo extraer claves específicas de un archivo JSON?
# En JSON, puedes extraer información específica iterando sobre las claves deseadas. Imagina que quieres solo los nombres y precios de los productos:

# Iterar y extraer claves: Usa bucles para acceder a la información específica que necesitas.

# for product in products:
#     print(f"Product: {product['name']}, Price: ${product['price']}")
# Al ejecutar este fragmento, obtendrás los nombres y precios de cada producto. Esta técnica es útil si trabajas con grandes volúmenes de datos.

# ¿Cómo añadir información a un archivo JSON?
# Añadir información a un archivo JSON es tan sencillo como leerlo. Supongamos que quieres añadir un nuevo producto:

# Crear el nuevo producto: Define el producto que deseas agregar en forma de diccionario.

# new_product = {
#     "name": "Wireless Charger",
#     "price": 75,
#     "quantity": 100,
#     "brand": "ChargeMaster",
#     "category": "Accessories",
#     "entry_date": "2024-07-01"
# }

# Abrir y modificar el archivo: Primero, lee los datos existentes y luego añade el producto nuevo al final de la lista.

# with open('Products.json', 'r') as file:
#     products = json.load(file)

# products.append(new_product)

# with open('Products.json', 'w') as file:
#     json.dump(products, file, indent=4)
# Ejecutar y verificar: Tras ejecutar el código, verifica que el nuevo producto se haya añadido correctamente al archivo JSON.

# Manipular archivos JSON es una habilidad poderosa y esencial para cualquier desarrollador. Te permite conservar la estructura y 
# legibilidad del archivo mientras gestionas información de manera eficaz. Además, la práctica constante y el aprendizaje con ejercicios adicionales, 
# como convertir archivos entre CSV y JSON, potenciarán tus habilidades en el manejo de datos. ¡Sigue aprendiendo y ampliando tus conocimientos!