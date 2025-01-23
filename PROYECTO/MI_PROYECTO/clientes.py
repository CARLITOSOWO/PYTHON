class Cliente:
    def __init__(self, cliente_id, nombre, email):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.email = email

class AdministracionClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        self.clientes[cliente.cliente_id] = cliente
        print(f'EL CLIENTE DE NOMBRE {cliente.nombre} FUE AGREGADO EXITOSAMENTE')
    
    def obtener_cliente(self, cliente_id):
        return self.clientes.get(cliente_id, "EL CLIENTE NO FUE ENCONTRADO.")