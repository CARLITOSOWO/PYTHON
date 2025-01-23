from typing import Any

class Carro:
    def __init__(self, modelo, serie, marca, precio):
        self.modelo = modelo
        self.serie = serie
        self.marca = marca
        self.precio = precio
        self.disponible = True

    def descompuesto(self):
        if self.available:
            self.available = False
            print(f"EL AUTO {self.modelo} SERIE {self.serie} MARCA {self.marca} PRECIO {self.precio} NO ESTA DISPONIBLE DEBIDO A QUE ESTA DESCOMPUESTO ")

    def vender_auto(self):
        if self.disponible:
            self.disponible = False
            print(f"EL AUTO DE MODELO {self.modelo} Y NUMERO DE SERIE {self.serie} MARCA {self.marca} CON EL PRECIO DE {self.precio} HA SIDO VENDIDO")

    def mostrar_autos_disponibles(self):
         print("LOS AUTOS DISPONIBLES: ")
         for auto in self.auto:
             if auto.available:
                 print(f"{auto.modelo} por {auto.serie}")


class Cliente:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id

class Tienda:
    def __init__(self):
        self.autos = []
        self.clientes = []

    def agregar_auto(self, auto):
        self.autos.append(auto)
        print(f"EL AUTO {auto.modelo} HA SIDO AGREGADO")
    
    def register_user(self, cliente):
        self.clientes.append(cliente)
        print(f"EL CLIENTE {cliente.nombre} HA SIDO REGISTRADO")

    def mostrar_autos_disponibles(self):
        print("LOS AUTOS DISPONIBLES: ")
        for auto in self.autos:
            if auto.disponible:
                print(f"{auto.modelo} por {auto.serie}")


#CREAR LOS CARROS 
auto1 = Carro("BOCHO", "123456789", "VOLSVAGUEN", "40000")
auto2 = Carro("TESLA", "159159159", "ELONK", "100000")

#CREAR UN USUARIO 
cliente1 = Cliente("CARLOS", "001")
cliente2 = Cliente("RODRI", "002")

#CREAR LA TIENDITA 
tiendita = Tienda()
tiendita.agregar_auto(auto1)
tiendita.agregar_auto(auto2)
tiendita.register_user(cliente1)
tiendita.register_user(cliente2)
tiendita.mostrar_autos_disponibles()




