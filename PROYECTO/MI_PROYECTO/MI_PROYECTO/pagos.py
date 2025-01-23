import asyncio
import random

async def  proceso_pago(cliente_nombre, monto):
    print(f"EL CLIENTE {cliente_nombre} PAGARA LA SUMA DE {monto}")
    await asyncio.sleep(random.randint(1,4))
    print(f"EL PAGO DE $ {monto} COMPLETADO PARA {cliente_nombre}")
    return True