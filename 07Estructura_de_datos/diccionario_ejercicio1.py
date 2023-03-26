'''En el siguiente diccionario se encuentran capitales de los paises en el mundo,
 debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
 en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo 
 que ese pais no se encuentra.
"Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama":"Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"} '''
capitales_paises= {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama":"Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
pais= input("Escriba un pais que desee conocer la capital:\n").capitalize()
if pais in capitales_paises:
    print(capitales_paises[pais])
else:
    print("No tenemos registro de este país")