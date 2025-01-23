import threading

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.lock = threading.RLock()

    def transferir(self, otra_cuenta, cantidad):
        with self.lock:
            self.saldo -= cantidad
            otra_cuenta.depositar(cantidad)

    def depositar(self, cantidad):
        with self.lock:
            self.saldo += cantidad

cuenta1 = CuentaBancaria(500)
cuenta2 = CuentaBancaria(300)

hilo1 = threading.Thread(target=cuenta1.transferir, args=(cuenta2, 200))
hilo2 = threading.Thread(target=cuenta2.transferir, args=(cuenta1, 100))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Saldo cuenta1: {cuenta1.saldo}")
print(f"Saldo cuenta2: {cuenta2.saldo}")


"""
3. Problemas de Sincronización y Cómo Evitarlos
A medida que manejas tareas más complejas, es posible que te 
encuentres con problemas como deadlocks y race conditions. 
Entender estos problemas es crucial para escribir código concurrente robusto.

Evitar Deadlocks con RLock
Un deadlock ocurre cuando dos o más hilos se bloquean 
mutuamente al esperar por un recurso que está siendo utilizado 
por otro hilo. Para evitar esto, podemos usar RLock en lugar de Lock.
Explicación:

Usamos RLock para evitar que múltiples operaciones simultáneas en una cuenta causen bloqueos
"""