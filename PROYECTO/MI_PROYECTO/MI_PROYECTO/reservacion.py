from collections import defaultdict
from datetime import datetime

class Reservacion:
    def __init__(self, reservacion_id, cliente_nombre, numero_cuarto, check_in, check_out):
        self.reservacion_id = reservacion_id
        self.cliente_nombre = cliente_nombre
        self.numero_cuarto = numero_cuarto
        self.check_in = check_in
        self.check_out = check_out

class SistemaReservacion:
    def __init__(self):
        self.reservaciones = defaultdict(list)

    def agregrar_reservacion(self, reservacion):
        self.reservaciones[reservacion.numero_cuarto].append(reservacion)
        print(f"LA RESERVA PARA EL CLIENTE {reservacion.cliente_nombre} EN LA HABITACION CON NUMERO { reservacion.numero_cuarto}")

    def cancela_reservacion(self, reservacion_id):
        for cuarto, reservaciones in self.reservaciones.items():
            for r in reservaciones:
                if r.reservacion_id == reservacion_id:
                    reservaciones.remove(r)
                    print(f"LA RESERVACION CON ID {reservacion_id} FUE CANCELADA")
                    return
        print("RESERVACION NO ENCONTRADA")



