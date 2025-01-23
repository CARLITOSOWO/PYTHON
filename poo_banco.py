class BankAccount:
    def __init__(self, account_holder ,balance):# CREACION DE CONSTRUCTOR
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True 

    def deposit(self, amount):#FUNCION DE DEPOSITAR DINERO 
        if self.is_active:
            self.balance += amount
            print(f"SE A DEPOSITADO {amount}.SALDO ACTUAL {self.balance}")
        else:
            print("NO SE PUEDE DEPOSITAR , CUENTA INACTIVA ")

    def withdraw(self, amount):#FUNCION DE RETIRAR DINERO 
        if self.active:
            if amount <= self.balance: #PODEMOS SACAR DINERO MIENTRAS TENGAMOS DINERO 
                self.balance -= amount
                print(f"SE A RETIRADO {amount}.Saldo actual {self.balance} ")
            
    def desactive_account(self):
        self.is_active = False
        print(f"LA CUENTA A SIDO DESACTIVADA ")

    def active_account(self):
        self.is_active = True
        print(f"LA CUENTA A SIDO ACTIVADA ")


cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

#LLAMADA A LOS METODOS 
cuenta1.deposit(200)
cuenta2.deposit(100)
cuenta1.desactive_account()
cuenta1.deposit(50)
cuenta1.active_account()
cuenta1.deposit(50)
