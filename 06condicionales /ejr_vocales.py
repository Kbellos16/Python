vocal= input("dame una letra: \n").capitalize()
'''if vocal == "A" or vocal=="E" or vocal== "I" or vocal=="O" or vocal=="U":
     print("Tu letra es una vocal")
else: 
     print("tu letra es consonante")'''
if vocal in "AEIOU":
    print('es vocal')
else:
    print("es consonante")
    