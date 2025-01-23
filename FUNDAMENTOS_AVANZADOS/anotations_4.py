from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None



"""
VA A EXISTIR CASOS DONDE UNA FUNCION NO NECESARIEAMENTE ACEPTARA UN SOLO TIPO DE DATO EN ESTOS CASO USAMOS LA 
LIBRERIA Optional
NOS DAS LA CAPACIDAD DE QUE AL BUSCAR UN TIPO DE DATO Y AL NO ENCONTRARLO RECIBIMOS UN NONE PARA QUE EL TIPO DE DATOS 
DE RESPUESTA NO ROMPA EL CODIGO Y SIGA FUNCIONANDO 

TIPOS DE DATOS EN ANOTACIONES 

* int :ENTEROS 
* float : NUMERO CON PUNTO FLOTANTE 
* str : CADEMAS DE TEXTO
* bool : VALORES BOOLEANOS TRUE-FALSE
* list : LISTAS 
* dict : DICCIONARIOS
* tuple : TUPLAS 
"""