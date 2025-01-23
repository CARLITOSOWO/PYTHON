class MultiplierFactory:
    
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result)


"""
METAPROGRAMACION 
EN ELLA TENEMOS UN ORDEN LOGICO Y LOS METODOS __new__ VAN EN PRIMERA INSTANCIA 

__new__ CREA UNA NUEVA INSTANCIA Y DESDE EL CONTROLAR LA CREACION DE CADA UNO DE LOS OBJETOS HAY QUE TENER CUIDADO 
CON ESTE METODO YA QUE EL PUEDE3 RETORNAR ERRORES SI NO SABEMOS ESTRUCTURAR EL return 


La metaprogramación en Python es una técnica que permite a los programas manipular o generar código durante su ejecución. 
Esto se puede lograr a través de varias funcionalidades del lenguaje, como las clases, los decoradores, las funciones de alto orden y los metaclases.


"""