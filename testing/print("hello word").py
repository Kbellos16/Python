print("hello word")
my_list= list()
print(len(my_list))
my_list = [10,20,30]
print(my_list)

print(my_list[0]) # llamar a la posicion de la lista
print(my_list.count(10)) # cuenta cuantos valores existen en la lista
other_list=[38,"jose",1.86,"vieira"]
age, name, height, last_name = other_list
print(age,last_name) # imprime en funcion de la variable que esta ubicada en la lista
other_list.append(200)# insertar datos

other_list.insert(2,'strumu')
print(other_list)
my_list.reverse()
print(my_list)
