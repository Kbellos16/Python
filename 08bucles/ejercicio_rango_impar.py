'''Pedir al usuario que ingrese 2 numeros, después,
 se debe mostrar el rango de esos 2 números, pero,
   solo imprimiendo los números que sean impares'''

numero1= int(input('Escribe un numero:  '))
numero2= int(input('Escribe un segundo numero:  '))
if numero1 < numero2:
    for j in range(numero1,(numero2+1)):
            if not(j % 2):
                continue
            print(j)

else:
    for j in range(numero2,(numero1+1)):
        if not(j % 2):
            continue
        print(j)