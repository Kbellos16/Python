#Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial():
    resultado = 1
    numero = int(input("Introduzca un número: "))
    n = abs(numero)
    if n == 0 or n == 1:
        print(1)
    elif n > 1:
        for i in range(1,(n+1)):
            resultado= resultado * i
    print(resultado)
            

factorial()
