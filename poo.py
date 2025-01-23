# SE GENERA UN CONSTRUCTOR PARA QUE EN UN FUTURO ESTE PUEDA ALMACENAR/UTILIZAR LA INFORMACION DE UNA VARIABLE 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"HOLA MI NOMBRE ES {self.name} Y TENGO {self.age}")

person1 = Person("ANA", 34)
person2 = Person("LUIS",24)

person1.greet()
person2.greet()