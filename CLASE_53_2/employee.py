class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #ATRIBUTO PROTEGIDO OSEA DEBEMOS ACCEDER A EL DENTRO DE LA CLASE 

    @property #GETTER OSEA ACCEDEMOS A LA INFORMACION Y LA REGRESA 
    def salary(self): #ESTA FUNCION RETORNA LA INFORMACION QUE ESTA DENTRO DEL ATRIBUTO PROTEGIDO SIN LA NECESIDAD DE CREAR UNA FUNCION QUE LA MUESTRE
        return self._salary

    @salary.setter # SETTER CAMBIA LA INFORMACION 
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary

# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(employee.salary)  

# Modificar el salario de forma controlada
employee.salary = 6000
print(employee.salary)  # ->

# Intentar establecer un salario negativo
#employee.salary = -1000  

# Eliminar el salario
del employee.salary  


"""
property
ESTE NOS AYUDA A TENER TODA LA FUNCIONALIDAD DE UN METODO PERO SE VE COMO SI FUERA UN ATRIBUTO 

LOS OBJETOS PUEDEN TENER 3 PROPIEDADES 
GETTER -> PUEDEN DEVOLVER INFORMACION
SETTER -> PUEDEN MODIFICAR INFORMACION
DELETER -> ELIMINAR LA INFORMACION 

EN ESTE EJEMPLO SE APLICAN LOS TRES  

-> COMO PODEMOS VER CREAMOS UN OBJETO DE TIPO EMPLEADO employee = Employee("Ana", 5000)
Y LLAMAMOS DIRECTAMENTE A LA FUNCION DE SALARIO salary PERO COMO TIENE property ESTA NOS DEVUELVE LA 
INFORMACION SOLICITADA 



"""
