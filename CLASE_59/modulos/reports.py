# Genera un informe de ventas para un mes específico.
def generate_sales_report(month, sales):
    return f'Sales Report - {month}: Total sales: ${sales}'

# Genera un informe de gastos para un mes específico.
def generate_expenses_report(month, expenses):
    return f'Expenses Report - {month}: Total expenses: ${expenses}'



"""
MODULOS 
Crear módulos en Python es una manera de organizar y 
reutilizar el código, facilitando la mantenibilidad y 
claridad del proyecto. Un **módulo** es un archivo .py que contiene 
funciones, clases o variables que se pueden importar en otros archivos 
o módulos de un proyecto.

### 1. Creación de un Módulo Básico

Imaginemos que queremos crear un módulo llamado matematica.py que contenga 
funciones matemáticas personalizadas.

**Paso 1:** Crear el archivo del módulo.

En el mismo directorio del proyecto, crea un archivo llamado matematica.py y añade funciones en él.

**Paso 2:** Importar el módulo en otro archivo.

En un archivo diferente, como main.py, importa el módulo y utiliza sus funciones:


### 2. Importación Específica y Alias

Puedes importar funciones específicas o dar alias a las funciones o módulos para hacer 
el código más legible.

### 3. Uso de \_\_name\_\_ == "\_\_main\_\_"

El bloque if \_\_name\_\_ == "\_\_main\_\_": permite ejecutar pruebas o código dentro del 
propio módulo sin que se ejecute cuando el módulo es importado en otro archivo.

### 4. Creación de Paquetes

Un **paquete** es una colección de módulos organizados en una estructura de carpetas. 
Para crear un paquete, crea una carpeta con un archivo \_\_init\_\_.py y coloca módulos en ella. 
Esto permite importar submódulos.

### Resumen

1. **Módulo**: Archivo .py con funciones, clases o variables reutilizables.
2. **Paquete**: Carpeta con un archivo \_\_init\_\_.py que organiza múltiples módulos.
3. **Importación específica y alias**: Personaliza la importación de módulos o funciones.
4. **Pruebas con \_\_name\_\_ == "\_\_main\_\_"**: Permite probar el código en el módulo mismo sin que se ejecute al importarse.

Estos conceptos son fundamentales para crear código bien organizado y fácil de mantener en Python.
"""