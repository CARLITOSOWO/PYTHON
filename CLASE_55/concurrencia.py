import threading # NOS AYUDA CON LOS HILOS 
import time #SIMULA EL TIEMPO QUE TARDA UNA TAREA 

#función que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} completada')

threads = [] #LISTA DE HILOS QUE SE VAN CREANDO 

for i in range(3): #VAMOS A ITERAR ENTRE LOS 3 HILOS 
    #Crear nuevo hilo que ejecutará la función
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

#Esperar a que todos los hilos terminen
for thread in threads:
    #Asegura de el programa espere a que cada hilo termine
    thread.join()

print('Todas las solicitudes completadas')


"""
LA CONCURRENCIA 1 PROCESADOR

DESDE EL COMIENZO HEMOS TRABAJADO DE MANERA SECUECIAL ESTO QUIERE DECIR QUE SE DEBE DE TERMINAR UNA 
TAREA PARA COMENZAR OTRA 
______________________ 1 HILO
1PASO   2PASO   3PASO 
------------------------>
LINEA DE TIEMPO 

CUANDO USAMOS LA CONCURRENCIA VAMOS A INICIAR CON UN FRAGMENTO DE LA PRIMER TAREA ESTA SE PAUSARA 
Y COMENZARA OTRO FRAGMENTO DE LA SEGUNDA TAREA 

------------------------>
LINEA DE TIEMPO 
______________________ 1 HILO
1PASO 
            2PASO 
______________________ 2 HILO
    3PASO 
            4PASO 
______________________ 3 HILO
    5PASO 
                6PASO 

"""