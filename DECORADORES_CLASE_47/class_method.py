class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count +=1

Counter.increment()
Counter.increment()
print(Counter.count)


'''
classmethod
CON ESTE DECORADOR ESTAMOS DEFINIENDO QUE EL METODO QUE VAMOS A ESCRIBIR ESTA MODIFICANDO 
A NUESTRA CLASE O A UN OBJETO EN ESPECIFICO 
TOMA EN CUENTA QUE EL PARAMETRO QUE TOMA ES cls QUE SIGNIFICA CLASE 

'''