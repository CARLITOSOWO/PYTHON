def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora ():
    while True:
        print("SELECCIONE UNA OPERACION")
        print("1. SUMA")
        print("2. RESTA")
        print("3. MULTIPLICACION")
        print("4. DIVISION")
        print("5. SALIR")

        opcion = input("INGRESE UNA OPCION (1,2,3,4,5): ")

        if opcion == "5":
            print("ESTAS SALIENDO DE LA CALCULADORA")
            break
        if opcion in ["1","2","3","4"]:
            num1 = float(input("INGRESE EL PRIMER NUMERO: "))
            num2 = float(input("INGRESE EL SEGUNDO NUMERO: "))

            if opcion == "1":
                print ("LA SUMA ES :", suma(num1,num2))
            elif opcion =="2":
                print ("LA RESTA ES :", resta(num1,num2))
            elif opcion =="3":
                print ("LA MULTIPLICACION ES :", multiplicar(num1,num2))
            elif opcion =="4":
                print ("LA DIVISION ES :", dividir(num1,num2))    

        else:
            print("OPCION NO VALIDA POR FAVOR INTENTA DE NUEVO")

calculadora()
           








