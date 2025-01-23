class Circle:

    def __init__(self, radius:float):
        self._radius = radius
        
    @property
    def area(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')#RECUERDA QUE PODEMOS USAR EXEPCIONES PARA MOSTRAR ERRORRES 
        self._radius = value

circle = Circle(5)
#print(circle.area)
circle.radius = -10
print(circle.area)



'''
property
ESTE DECORADOR LO QUE HACE ES QUE NOSOSTROS PODEMOS ACCEDER A LA FUNCIONALIDAD DE UN METODO PERO COMO SI FUERA 
UN ATRIBUTO DE CLASE 

setter
CAMBIAR LA INFORMACION


'''