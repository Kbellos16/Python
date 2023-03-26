'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de 
cada paquete, así que deben calcular el peso de los payasos y muñecas que 
saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
 Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un
   programa que muestre el peso total de toda la venta.'''
payasos_peso=(112)
munecas_peso=(75)
pedido= ((23*payasos_peso)+(54*(munecas_peso)))
print("El peso total del pedido son de",pedido,"gramos")