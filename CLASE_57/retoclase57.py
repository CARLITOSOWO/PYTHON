"""
IMPLEMENAT UN SISTEMA DE DESCARGA DE ARCHIVOS 
ASINCRONICA DONDE CADA ARCHIVO TARDE UN TIEMPO 
VARIABLE EN DESCARGARSE

"""
import asyncio #IMPORTAMOS asyncio
import random #IMPORTAMOS random PARA DEFINIR EL TIEMPO DE DESCARGA 

async def donwload_process(file): # CREAMOS LA FUNCION ASINCRONICA DE DESCARGA DE ARCHIVOS 
    print(f'Descargando archivo {file}') 
    time=random.randint(1,10) #DEFINIMOS UNA VARIABLE DE TIEMPO LA CUAL UTILIZARA random CON VALORES ENTEROS INT EN UN RANGO DE 1 A 10 
    await asyncio.sleep(time) #INDICAMOS EL TIEMPO DE ESPERA CON LA VARIABLE time
    print(f'{file} downloaded') 
    return file # REGRESAMOS file 

async def main(): #CREAMOS UNA SEGUNDA FUNCION ASINCRONICA 
    print('Inicio de la descarga')
    result=await donwload_process('file1.txt') # CREAMOS VARIABLES QUE JALEN EL TIEMPO DE ESPERA Y TOMEN LA FUNCION donwload_process 
    result1=await donwload_process('file2.txt')
    result2=await donwload_process('file3.txt')
    print(f'{result,result1,result2}')


asyncio.run(main()) # LLAMAMOS A asyncio Y LE PEDIMOS QUE CORRA EL PROCESO MAIN 