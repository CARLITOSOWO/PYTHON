# LA RECURSIVIDAD
# 1 2 3 4 5 6 7 8 9 10
n = int(input("INGRESE UN LIMITE : "))

def suma_numeros (n):
    if n == 0:
        return 0
    else:
        return n + suma_numeros(n-1) # <--LA RECURSIVIDAD

for i in range(n):
    print(f"SUMANDO DE {i} ES: {suma_numeros(i)}")

