#realizar la ecuacion de la resolvente 
# donde a es X**2 b es X* y c la constante
# 3X^2-5X+2=0  SOLUCION X=+1 X= 2/3 

from math import sqrt 
A= int(input('ingrese el valor de A:\n'))
B= int(input('ingrese el valor de B:\n'))
C= int(input('ingrese el valor de C:\n'))
x1=0
x2=0
if ((B**2)-(4*A*C)) < 0:
    print('Esta ecuación da un número imaginario')
else :
    x1= (((-B) +sqrt((B**2)-(4*A*C)))/(2*A))
    x2= (((-B) -sqrt((B**2)-(4*A*C)))/(2*A))
    print("El resultado es:\n X1=",x1,"\n x2=",x2)