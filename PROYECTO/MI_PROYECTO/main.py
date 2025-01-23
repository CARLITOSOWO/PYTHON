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
    room_mgmt.agregar_cuarto(Cuartos(101, "Single", 100))
    room_mgmt.agregar_cuarto(Cuartos(102, "Double", 150))

    # Agregar clientes
    customer1 = Cliente(1, "CARLOS", "Carlos@example.com")
    customer_mgmt.agregar_cliente(customer1)

    customer2 = Cliente(2, "RODRI", "Rodri@example.com")
    customer_mgmt.agregar_cliente(customer2)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.revisar_disponibilidad(101):
        reservation = Reservacion(1, "CARLOS", 101, datetime.now(), datetime.now())
        reservation_system.agregrar_reservacion(reservation)

        # Procesar pago asincrónicamente
        await proceso_pago("CARLOS", 100)

    if room_mgmt.revisar_disponibilidad(102):
        reservation = Reservacion(2, "RODRI", 102, datetime.now(), datetime.now())
        reservation_system.agregrar_reservacion(reservation)

        # Procesar pago asincrónicamente
        await proceso_pago("RODRI", 150)

if __name__ == "__main__":
    asyncio.run(main())
