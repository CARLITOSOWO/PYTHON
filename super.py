# ¿Qué es la función super() y cómo se usa en Python?
# La función super() en Python es una herramienta clave para 
# trabajar con la herencia en programación orientada a objetos. 
# Permite a las subclases acceder y extender los métodos y atributos 
# de su superclase sin referenciarlos explícitamente. Esto es muy útil 
# en estructuras de herencia complejas, ya que facilita el mantenimiento y 
# la extensión del código. En esta explicación, descubrirás cómo funciona super() 
# en el contexto de clases de Python y su importancia en la programación orientada a objetos.

# ¿Cómo se inicializan los atributos en clases con super()?
# En el mundo de la programación orientada a objetos, es fundamental 
# definir atributos y métodos de una clase. Los atributos representan las 
# características de la clase, mientras que los métodos definen las acciones
# que puede realizar. Al construir una clase, el constructor se utiliza para inicializar los atributos.

# En Python, una subclase puede heredar atributos y métodos de una superclase utilizando 
# la función super(). Por ejemplo, consideremos una clase Person con atributos como name y age 
# inicializados en su constructor:

# Cuando se crea una subclase Student que hereda de Person, se puede utilizar super() para acceder
# al constructor de Person y extenderlo, añadiendo atributos propios como student_id:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # COMO QUEREMOS HACER REFERENCIA AL CONSTRUCTOR DE LA SUPER CLASE O LA CLASE PADRE USAMOS super()
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

student = Student("Ana", 20, "S123")
student.greet()


#SUPER CON HERENCIA 
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Con este esquema, super() asegura que todos los niveles de herencia reciban los atributos
# iniciales adecuados, facilitando una estructura limpia y coherente.

# ¿Por qué es importante la herencia en la programación orientada a objetos?
# La herencia es uno de los cuatro pilares fundamentales de la programación orientada a objetos.
# Permite reutilizar y extender el código de manera eficiente, lo cual es crucial en la creación de aplicaciones complejas.

# Al comprender y aplicar la función super() en Python, los desarrolladores pueden construir sistemas
# jerárquicos con niveles de abstracción y especialización, promoviendo el diseño de software robusto y mantenible.

# Recuerda que la práctica constante y el estudio son esenciales para profundizar en estos conceptos y
# convertirte en un experto en programación orientada a objetos en Python. Continúa explorando y experimentando
# con clases y herencia para consolidar tu conocimiento.



# Métodos que Vienen por Defecto en Python
# En Python, todas las clases heredan de la clase base object. Esto significa que todas las clases tienen ciertos 
# métodos por defecto, algunos de los cuales pueden ser útiles para personalizar el comportamiento de tus clases.

# Métodos por Defecto Más Comunes
# __init__(self): Constructor de la clase. Es llamado cuando se crea una nueva instancia de la clase. Inicializa los atributos del objeto.

# __str__(self): Devuelve una representación en cadena del objeto, utilizada por print() y str(). Este método es útil para proporcionar una representación legible del objeto.

# __repr__(self): Devuelve una representación “oficial” del objeto, utilizada por repr(). Este método está diseñado para devolver una cadena que represente al objeto de manera
# que se pueda recrear.


# El método __str__ devuelve una representación en cadena del objeto, útil para mensajes de salida amigables.
# El método __repr__ devuelve una representación más detallada del objeto, útil para la depuración.
# Estos métodos proporcionan una manera conveniente de representar y comparar objetos, lo que facilita la depuración y el uso de los objetos en el código.