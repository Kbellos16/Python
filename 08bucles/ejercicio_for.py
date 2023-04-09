'''Imprimir por pantalla los numeros del 1 al 10, luego,
 pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range(1,11):
    print(i)
numero1= int(input('Escribe un numero:  '))
numero2= int(input('Escribe un segundo numero:  '))
if numero1 < numero2:
    for j in range(numero1,numero2):
        print(j)
else:
    for j in range(numero2,numero1):
        print(j)
