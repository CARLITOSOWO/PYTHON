'''
1*- FUNCION PARA AGREGAR Y ELIMINAR EMPLEADOS EN UNA LISTA 
2*- UN BLOQUE if __name__ == "__main__": QUE PERMITA PROBRA EL FUNCIONAMIENTO DEL SCRIPT EJECUTABLE DIRECTAMENTE 
'''
employeers = [#DEFINIMOS LA LISTA QUE VAMOS A USAR
    {'name': 'Carlos', 'role': 'admin'},
    {'name': 'Juan', 'role': 'employee'},
    {'name': 'Jose', 'role': 'employee'},
    {'name': 'Ana', 'role': 'employee'}
]

#CREAMOS LA FUNCION DE ELIMAR EMPLEADO 
def delete_employeer(employeers: list[dict], name_employeer: str):#DONDE SOLICITAMOS COMO PARAMETROS UNA LISTA , Y EL NOMBRE DE TIPO DE DATO STR
    for employeer in employeers:#CREAMOS UN FOR PARA ITERAR EN LA LISTA Y HAGA LA BUSQUEDA EN TODA ELLA 
        if (employeer["name"] == name_employeer):#SI EMPLOYER NOMBRE == AL NOMBRE INGRESADO 
            employeers.remove(employeer)# CON LA FUNCION remove ELIMINAMOS EL REGISTRO DE LA LISTA 
            return True
    return False

#CREAMOS LA FUNCION DE AGRGAR EMPLEADO 
def add_amployeer(employeers: list[dict], name: str, role: str):
    employeers.append({"name": name,"role": role})# CON LA FUNCION append AGREGAMOS EL REGISTRO DE LA LISTA

if __name__ == "__main__":#UN BLOQUE if __name__ == "__main__": QUE PERMITA PROBRA EL FUNCIONAMIENTO DEL SCRIPT EJECUTABLE DIRECTAMENTE 
    print(delete_employeer(employeers, "Juan"))#IMPRIMIMOS LA FUNCION DE ELIMINAR EMPLEADO Y LE PASAMOS LOS PARAMETROS NECESARIOS PARA QUE FUNCIONE 
    print(employeers)#IMPRIMIMOS LA LISTA PARA VER EL CAMBIO 
    add_amployeer(employeers, "Antonio", "admin")#IMPRIMIMOS LA FUNCION DE AGREGAR EMPLEADO Y LE PASAMOS LOS PARAMETROS NECESARIOS PARA QUE FUNCIONE 
    print(employeers)#IMPRIMIMOS LA LISTA PARA VER EL CAMBIO 

