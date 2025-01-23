# LA RECURSIVIDAD ES UNA TECNICA DE LA PROGRAMACION DONDE UN PROGRAMA SE LLAMA A SI MISMSO PARA PODER RESOLVER UN PROBLEMA

def factorial (n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1) # <--LA RECURSIVIDAD
    
factorial_5 = print(factorial(30)) # <-- LA RECURSIVIDAD


# TAMBIEN SE PUEDE UTILIZAR EN LA SERIE DE FIBONACCI

def fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    

numero = 5
print(fibo(numero))


