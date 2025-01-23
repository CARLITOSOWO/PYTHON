# LOS 4 PILARES 
# Encapsulación
# El encapsulamiento es una técnica que ayuda a proteger los datos dentro de un objeto
# y a garantizar que la interacción con esos datos se haga de una forma controlada y segura.
# A través de este principio, se promueve la modularidad y el mantenimiento 
# fácil del código, permitiendo una mejor organización del mismo
# Abstracción
# La abstracción consiste en ocultar los detalles complejos de la implementación de un objeto
# y exponer solo lo esencial, es decir, las funcionalidades necesarias para que el usuario o el
# resto del programa interactúe con él. De esta manera, se simplifica la interfaz del objeto y se 
# facilita el uso del mismo.

# La abstracción permite que puedas enfocarte en lo que un objeto hace y no en cómo lo hace.
# Esto se logra mediante la creación de clases y métodos que definen comportamientos 
# generales, mientras que los detalles específicos quedan encapsulados dentro de la implementación 
# de esos comportamientos.

# Diferencia entre abstracción y encapsulamiento:
# Encapsulamiento se refiere a ocultar los detalles internos (como los atributos) de una clase,
# de manera que solo se pueda interactuar con los métodos públicos.
# Abstracción se refiere a ocultar la complejidad de la implementación y mostrar 
# solo las características esenciales del objeto, permitiendo que se usen sin necesidad 
# de entender todo lo que ocurre internamente.

# La abstracción permite diseñar sistemas más claros al ocultar los detalles de implementación
# y mostrar solo lo esencial. Así, los desarrolladores pueden interactuar con los objetos sin 
# tener que entender cómo funcionan internamente. Se logra a través del uso de clases abstractas 
# y la definición de métodos generales que son luego implementados por las clases específicas.

# Herencia

# La herencia permite que una clase herede propiedades (atributos) y comportamientos (métodos) de otra clase.
# La clase derivada puede:

# 1.-Usar los métodos y atributos de la clase base.
# 2-.Sobrescribir (modificar) métodos de la clase base para cambiar su comportamiento.
# 3.-Añadir nuevos atributos y métodos específicos para la subclase.

# Herencia permite que una clase derive de otra, heredando atributos y métodos.
# 1.-Las subclases pueden sobrescribir los métodos de la clase base para adaptar el comportamiento o agregar nuevos comportamientos.
# 2.-Utilizar herencia permite una mejor reutilización de código y una organización jerárquica de las clases.
# 3.-La herencia es muy útil en la creación de sistemas modulares y reutilizables, y refleja relaciones jerárquicas, como la que existe 
# entre clases generales y específicas (por ejemplo, Animal y Perro).


# Poliformismo
# Su nombre proviene del griego, y significa "muchas formas". En programación, el polimorfismo permite que objetos de diferentes clases 
# sean tratados de la misma manera a través de una interfaz común, pero cada uno puede tener su propia implementación del comportamiento.
# En términos simples, el polimorfismo permite que un mismo nombre de método o operación sea utilizado para objetos de diferentes clases, 
# pero con comportamientos específicos según la clase del objeto. En otras palabras, se puede invocar el mismo método en diferentes tipos 
# de objetos, pero cada tipo de objeto puede responder de manera diferente a ese método.

# 1.-Polimorfismo permite que una misma operación (como llamar a un método) se ejecute de manera diferente dependiendo del tipo de objeto sobre el que se aplique.
# 2.-El polimorfismo en tiempo de ejecución se logra mediante la sobrescritura de métodos (overriding) en las subclases.
# 3.-Gracias al polimorfismo, puedes escribir código más general y flexible, ya que puedes trabajar con objetos de diferentes clases sin preocuparte 
# por los detalles específicos de cada tipo de objeto






class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulación 
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No está disponible")
    
    #Abstracción
    def check_available(self):
        return self.is_available
    
    #Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No está disponible"

#Herencia
class Bike(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

     #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No está disponible"

#Herencia
class Truck(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No está disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento,{vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
    
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership() #CREACION DE TIENDA 
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()