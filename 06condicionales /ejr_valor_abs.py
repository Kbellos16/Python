numero= input('introduzca un numero:\n')
def if_integer(numero):
  try:
    float(numero)
    return True
  except ValueError:
    return False

'''if if_integer(numero):
    numero =int(numero)
    if numero >=0: 
        print(numero)  
    else:
        print(numero*(-1))
else:
   print("este no es un numero valido")'''
if if_integer(numero):

    print(abs(int(numero)))
else:
   print("este no es un numero valido")
