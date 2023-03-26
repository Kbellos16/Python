'''Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir
que riman un poco y si no, que no riman.'''

palabra1= input("introduzca una palabra:\n")
palabra2= input("introduzca segunda palabra:\n")
if len(palabra1)< 3 or len(palabra2)< 3 :
     print("Lo siento no riman estas palabras")
elif palabra1[-3:]==palabra2[-3:]:
    print("Estas palabras tienen buena rima")
elif palabra1[-2:]==palabra2[-2:]:
    print("Estas palabras riman un poco")
else:
    print("Lo siento no riman estas palabras")
