class Cuartos:
    def __init__(self, cuarto_numero, tipo_cuarto, precio):
        self.cuarto_numero = cuarto_numero
        self.tipo_cuarto = tipo_cuarto
        self.precio = precio
        self.disponible = True

class AdministradorCuartos:
    def __init__(self):
        self.cuartos = {}
    
    def agregar_cuarto(self, cuarto):
        self.cuartos[cuarto.cuarto_numero] = cuarto
        print(f"LA HABITACION CON EL NUMERO {cuarto.cuarto_numero} FUE AGREGADA")

    def revisar_disponibilidad(self, cuarto_numero):
        cuarto = self.cuartos.get(cuarto_numero)
        if cuarto and cuarto.disponible:
            print(f"LA HABITACION CON EL NUMERO {cuarto_numero} ESTA DISPONIBLE")
            return True
        print(f"LA HABITACION CON EL NUMERO {cuarto_numero} NO ESTA DISPONIBLE")
        return False