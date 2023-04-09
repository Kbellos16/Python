'''Crear una funcion que pida dos numeros. Si el primero es 
mayor al segundo, el programa debe retornar el valor 1; si 
el segundo es mayor al primero, debe 
retornar -1; si ambos son iguales, debe retornar 0'''

def devolver():
    numero= input ("introduzca un nùmero:" )
    numero2= input ("introduzca un segundo número:" )
    if numero > numero2:
        return 1
    elif numero2> numero:
        return -1
    else:
        return 0

print(devolver())
