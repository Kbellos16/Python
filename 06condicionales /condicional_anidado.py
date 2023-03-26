nombre= input(("Introduzca nombre: \n")).capitalize()
edad = int(input('Ahora pon tu edad:\n '))
if nombre == "Juan":
    if edad >= 18:
        print("Eres Juan y eres mayor de edad")
    else: 
        print('eres Juan pero no mayor de edad')    
else: print("tu no eres Juan" )
