class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
print(Order.calculate_tax(1000, 18))



"""
En Python, los métodos estáticos y de clase (@staticmethod y @classmethod) 
son herramientas poderosas para gestionar el comportamiento de las clases sin 
tener que instanciar objetos. Aunque ambos tipos de métodos no actúan sobre una 
instancia, difieren en su uso y propósito:

### 1. Métodos Estáticos (@staticmethod)

Un método estático es una función que pertenece a una clase, pero no puede acceder ni 
modificar el estado de la clase o de sus instancias (no recibe el argumento self ni cls). 
Los métodos estáticos se utilizan cuando la funcionalidad de la función es relevante para la clase, 
pero no necesita interactuar con los atributos o métodos de clase o de instancia.

#### Uso de @staticmethod avanzado

En casos avanzados, los métodos estáticos pueden ser útiles para:
- Realizar cálculos complejos independientes de la clase.
- Encapsular funciones auxiliares que operan sobre datos externos.
- Realizar validaciones de datos que pueden usarse en múltiples métodos de la clase.


### 2. Métodos de Clase (@classmethod)

Un método de clase recibe el primer argumento cls, que representa la propia clase y 
permite manipular los atributos de la clase o crear nuevas instancias. Los métodos de clase 
son útiles para trabajar con datos a nivel de clase y pueden ser usados para construir métodos de 
fábrica, modificar atributos de clase o realizar operaciones que afectan a todas las instancias de la clase.

#### Uso de @classmethod avanzado

Los métodos de clase son especialmente útiles en situaciones donde necesitas:
- Crear instancias de la clase desde datos o configuraciones específicas.
- Implementar métodos de fábrica que devuelvan instancias preconfiguradas.
- Acceder y modificar datos a nivel de clase, como contadores de instancias.



"""