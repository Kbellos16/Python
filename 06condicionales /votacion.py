'''Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir 
el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
indicar “Opción errónea”.
Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula'''

'''candidato1= "A" # candidato rojo
candidato2= "B"# candidato verde
candidato3= "C"# candidato azul'''
voto= input('Por cual candidato desea votar: \n candidato A:\n candidato B:\n canditado C:\n ').upper()
if voto == "A":
    print("Usted ha votado por el partido rojo")
elif voto == "B":
    print("Usted ha votado por el partido verde") 
elif voto == "C":
    print("Usted ha votado por el partido azul")
else:
    print('opción erronea')
    