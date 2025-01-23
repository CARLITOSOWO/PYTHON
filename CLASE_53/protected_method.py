class BaseClass:
    def __init__(self):
        self._protected_variable = 'Protected'
        self.__private_variable = 'Private'

    def _protected_method(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method(self):
        self.__private_method()

base = BaseClass()
#print(base._protected_variable)
#base._protected_method()

#base.public_method()
print(base.__private_variable)


'''
CADA QUE TRABAJEMOS CON METODOS PRIVADOS O PROTEGIDOS TOMA EN CUENTA QUE DEMOS USAR EL GUIN BAJO _ ESTOS SIGINIFCA QUE NOSOTROS 
SI PODEMOS ACCEDER DESDE FUERA DE LA CLASE PERO DAMOS INFORMACION CUANDO ALGUIEN MAS INTENTE ACCEDER DESDE AFUERA 
+ YA SEA EN CONSTRUCTORES 
O EN FUNCIONES ESTO SE APLICA 

SE PUEDE ACCEDER A ELLOS DEBIDO A QUE PYTHON NO RESTRINGE EL ACCESO A CADA UNO DE ESTOS METODOS O A LA INFORMACION PROTEGIDA 
CUANDO QUEREMOS RESTRINGIR LA INFORMACION DEBEMOS CREAR UN METODOD QUE LO HAGA ESTE LLEVA DOS GUIONES BAJOS __ PARA INDICAR QUE 
ES UN METODO PRIVADO 

CUANDO TENENMOS UN METODO PUBLICO QUE LLAMA A UN METODO PRIVADO ESTE SI PUEDE ACCEDER A LA INFORMACION PRIVADA 
ESTO DEBIDO A QUE SE ENCUENTRAN EN EL MISMO NIVEL DE IDENTACION 


'''