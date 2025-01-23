def divide(a: int, b: int) -> float:
    #validar qeu ambos parametros sean enteros
    if not isinstance(a,int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser enteros.')
    
    #Verificamos que el divisor no sea cero
    if b ==0:
        raise ValueError('El divisor no puede ser cero.')
    
    return a/b

#Ejemplo de uso
try: # INTENTAR 
    res = divide(10,'2') #Error de tipo por que un tipo de dato es str 
    print(res)
except TypeError as e: # DECLARAMOS UNA VARIABLE PARA QUE GUARDE LA INFORMACION DE LA EXEPCION 
    print(f'Error: {e}')

#Ejemplo de uso
try:
    res = divide(10,0) #Error de división por cero
    print(res)
except ValueError as e:
    print(f'Error: {e}')

#Ejemplo de uso
try:
    res = divide(10,2) #División correcta
    print(res)
except (ValueError, TypeError) as e: #PODEMOS HACER EL USO DE AMBAS EXEPCIONES
    print(f'Error: {e}')



    """
    isinstance ES UNA FUNCION QUE VALIDA QUE LA INSTANCIA NO SEA ENTEROS 
    ES COMO PREGUNTRA SI EL DATO PERTENECE AL EL TIPO QUE ESTA SOLICITANDO  isinstance(a,int)

    raise PODEMOS VOLVER A TRAER UNA EXEPCION Y QUE SALTE EN EL CODIGO PERO PODEMOS PERSONALIZARLA 
    Y  PODEMOS PONER UN  TypeError  JUNTO CON UN MENSAJE QUE DESCRIBA LA FALLA 

    try / except  
    INTENTA / EXEPCION

    """