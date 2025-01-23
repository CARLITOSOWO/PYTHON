import multiprocessing # NOS PERMITE TRABAJAR CON MULTIBLES HILOS 

#Función que calcule el cuadrado de un número
def calculate_square(n):
    return n*n

if __name__ == '__main__': #BLOQUE PRINCIPAL DE EJECUCION CON ESTE SE VA A EJECUTAR DE MANERA DIRECTA
    numbers = [1,2,3,4,5] #COLECCION DE NUMEROS 

    #crear un pool DE PROCESOS PARA EJECUTAR LAS FUNCIONES EN PARALELO
    with multiprocessing.Pool() as pool: # with multiprocessing = CON LOS MULTIPROCESOS 
        results = pool.map(calculate_square, numbers)

    print(f'Resultados: {results}')

    """
    EL PARALELISMO 3 PROCESADORES O MAS 

    ESTE DEPENDE DE LOS NUCLEOS DE PROCESAMIENTO QUE TIENE NUESTRO EQUIPO 
    EJEMPLO SI QUEREMOS QUE SE EJECUTEN 3 TAREAS DEBEMOS TENER 3 NUCLEOS 
    DONDE TODAS SE INICIAN AL MISMO TIEMPO Y VANA ATOMAR SU CURSO EN 
    PARALELO HASTA QUE TERMINENE 

------------------------>
LINEA DE TIEMPO 
______________________ 1 HILO
1PASO   2PASO  3PASO 
______________________ 2 HILO
4PASO   5PASO   6PASO 
______________________ 3 HILO
7PASO   8PASO   9PASO



.Pool() as pool: NOS AYUDA A EJECUTAR HILOS PERO EN PARALELO 
map La función map() permite aplicar una función a todos los elementos 
de un iterable (como una lista, tupla, etc.) y devuelve un objeto map 
que puede ser convertido en una lista u otro tipo de colección.

    """