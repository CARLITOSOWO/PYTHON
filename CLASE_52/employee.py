class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá')
employee.show_employee()

"""
CREAMOS UNA FUNCION QUE ALMACENE LA INFORMACION DE UN EMPLEADO DONDE VAMOS A USAR LOS args Y LOS kwargs
EN ESTE CASO LOS args ALMACENAN LAS HABILIDADES ESTO DEBIDO A QUE LOS EMPLEADOS TIENE DIFERENTES HABILIDADES Y DIFERENTE NUEMRO 
Y UN DETALLE DE ESTOS 

LOS ARGUMENTOS QUE NO SON POSICIONALES PASAN DE MANERA DIRECTA A LOS args COMO SON LOS LENGUAJES DE PROGRAMACION EN LA VARIABLE employee
LOS ARGUMENTOS COMO LA EDAD Y LA CIUDAD COMO ESTAMOS DEFINIENDO DONDE GUARDARLOS PASAN EN AUTOMATICO A LOS kwargs age=30, city = 'Bogotá'

"""