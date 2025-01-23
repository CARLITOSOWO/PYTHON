import asyncio
from MI_PROYECTO.reservacion import Reservacion, SistemaReservacion
from MI_PROYECTO.clientes import Cliente, AdministracionClientes
from MI_PROYECTO.cuartos import Cuartos, AdministradorCuartos
from MI_PROYECTO.pagos import proceso_pago
from datetime import datetime

async def main():
    # Inicializar sistemas
    reservation_system = SistemaReservacion()
    customer_mgmt = AdministracionClientes()
    room_mgmt = AdministradorCuartos()

    # Crear habitaciones
    room_mgmt.add_room(Cuartos(101, "Single", 100))
    room_mgmt.add_room(Cuartos(102, "Double", 150))

    # Agregar clientes
    customer1 = Cliente(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Cliente(2, "Bob", "bob@example.com")
    customer_mgmt.add_customer(customer2)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(101):
        reservation = Reservacion(1, "Alice", 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await proceso_pago("Alice", 100)

    if room_mgmt.check_availability(102):
        reservation = Reservacion(2, "Bob", 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await proceso_pago("Bob", 150)

if __name__ == "__main__":
    asyncio.run(main())
