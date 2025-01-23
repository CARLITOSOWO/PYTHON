'''
IMPLEMENTA UNA CLASE CuentaBanacaria CON UN METODO PROTEGIDO 
PARA ACTUALIZAR EL SALDO Y UN METODO PRIVADO PARA REGISTRAR LAS 
TRANSACCIONES INTERNAMENTE 

1.-EL METODO PROTEGIDO (_actualizar_saldo) SOLO DEBE SER UTILIZADO DENTRO DE LA CLASE
Y SUS SUBCLASES 

2.-EL METODO PRIVADO (__registrar_transaccion) DEBE SER COMPLETAMENTE INTERNO 
Y NO ACCESIBLE FUERA DE LA CLASE 

'''
class CuentaBancaria:#CREACION DE CONSTRUCTOR 
    def __init__(self, name, number_bank, _initial_balance):
        self.name = name
        self.number_bank = number_bank
        self._initial_balance = _initial_balance
        self.__record = []

    def _update_balance(self, option, quantity):#CREAMOS EL METODO DE ACTUALIZAR BALANCE 
        if option == 'deposite': # CREAMOS UN FI CON LA VARIABLE option QUE SEA IGUAL A DEPOSITO COMO PARAMETRO DE ENTRADA 
            self._initial_balance += quantity # A LA VARIABLE PROTEGIDA _initial_balance LE SUMAMOS EL VALOR DE LA VARIABLE quantity
            print(f'Ha depositado: ${quantity}. Su saldo actual es de: ${self._initial_balance}') # IMPRIMIMOS UN MENSAJE 
            self.__record_transaction(option, quantity) # MANDAMOS A LA FUNCION PRIVADA  EL VALOR DE ESTAS DOS VARIABLES option Y quantity
        elif option == 'withdraw': #CREAMOS UNA OPCION EXTRA EN EL IF PARA RETIROS COMPARANDO EL VALOR DE LA VARIABLE option CON EL PARAMETRO QUE ENVIEMOS AL LLAMAR
            if self._initial_balance < quantity: #CREAMOS UN IF QUE COMPARE LA VARIABLE PROTEGIDA CON LA CANTIDAD SI ESTA ES MENOR 
                print("No tiene el saldo suficiente para retirar. ") #MANDAMOS ESTE MENSAJE 
            else: #SI NO 
                self._initial_balance -= quantity # A LA VARIABLE PROTEGIDA LE RESTAMOS EL VALOR SOLICTADO E IMPRIMIMOS EL MENSAJE 
                print(f"Ha retirado: ${quantity}. Su saldo actual es de: ${self._initial_balance}") 
                self.__record_transaction(option, quantity) # MANDAMOS A LA FUNCION PRIVADA  EL VALOR DE ESTAS DOS VARIABLES option Y quantity
        
    def __record_transaction(self, option, quantity): #CREAMOS LA FUNCION DE REGISTRAR TRANSACCION 
        self.__record.append((option, quantity))

    def show_record(self): #CREAMOS LA FUNCION DE MOSTRAR  REGISTRO 
        return self.__record


cuenta_1 = CuentaBancaria('Sebastian', '1', 0) #CREAMOS UNA VARIABLE QUE LLAME A LA CLASE Y MANDE LOS SIGUIENTES PARAMETROS DE INICIO 
cuenta_1._update_balance('deposite', 5000) # LLAMAMOS AL METODO DE ACTUALIZAR BALANCE CON LA VARIABLE ANTES CREADA 
cuenta_1._update_balance('deposite', 40000)
print(cuenta_1.show_record())

