import threading

# Variable compartida
saldo = 0
lock = threading.Lock()  # Crear un Lock

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # Bloquear el acceso para evitar condiciones de carrera
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}")  # Esperamos ver 200000 como saldo


"""

1. Sincronización de Hilos en Python
Cuando varios hilos intentan acceder a un mismo 
recurso al mismo tiempo, pueden ocurrir problemas de 
coherencia. Para evitar esto, se utilizan mecanismos de 
sincronización, como Lock y RLock, que garantizan que solo 
un hilo acceda a un recurso crítico a la vez.

Explicación:

El uso de Lock asegura que solo un hilo modifique la 
variable saldo en un momento dado, evitando que el 
resultado final sea incorrecto.
"""