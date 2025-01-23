import asyncio #IMPORTAMOS asyncio

async def process_data(data): #INICIAMOS UNA FUNCION ASINCRONA CON LA PALABRA RECERBADA async
    print(f'Procesando {data}...')
    #Simular una operación
    await asyncio.sleep(10) # UTILIZAMOS await JUNTO CON asyncio LOS CUALES NOS AYUDA A QUE NOSOTROS PODAMOS DEFINIR LA ESPERA DEL PROGRAMA SIN AFECTAR EL BLOQUE sleep EL TIEMPO EN ESPERA 
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt') # 
    print(f'Resultado: {result}')

asyncio.run(main()) # LLAMAMOS A asyncio Y LE PEDIMOS QUE CORRA EL PROCESO MAIN 


"""
CUANDO ENVIAMOS UNA PETICION AL SERVIDOR ESTE LA PROCESA Y LA REGRESA 

CLIENTE     SERVIDOR
   |            |
   |  --------> |
   |            |
   |            |
   | <----------|
   |            |

CUANDO TRABAJAMOS CON EL ASINCRONIZMO PODEMOS ENVIAR MULTIPLES TAREAS Y ESTE LAS REGRESA 
EN EL MISMO TIEMPO DE EJECUCION 

EN PYTHON ESTO VIENE CON LAS 
CORRUTIVAS Y ASYNCION 
UNA CORRUNTINA ES UNA FUNCION QUE PUEDE SER PAUSADA Y RETOMADA MAS TARDE 
PALABRAS CLAVE 
async  |  await

LA LIBRERIA QUE VAMOS A USAR ES asyncio

LA CUAL RECIBE UNA RESPUESTA 
    |
LUEGO CREA UN EVENT LOOP 
    |
Y FINALMENTE DEVUELVE LA RESPUESTA EN CADA UNA DE LAS TAREAS 
   
   
   """