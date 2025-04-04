#Cálculo del volumen de un cilindro y su área superficial 
Radio_del_cilindro = float(input("Dime el radio del cilindro: "))
Altura_del_cilindro = float(input("Dime la altura del cilindro: "))
Area_de_la_base = 3.1416 * (Radio_del_cilindro * Radio_del_cilindro)
Volumen_del_cilindro = Area_de_la_base * Altura_del_cilindro
Area_Lateral = 2 * 3.1416 * Radio_del_cilindro * Altura_del_cilindro
Area_Superficial_del_cilindro = Area_Lateral + (Area_de_la_base * 2)
print("El radio del cilindro es de: ", Radio_del_cilindro,"y su altura es de: ",Altura_del_cilindro)
print(f"El volumen del cilindro es de: {Volumen_del_cilindro:.2f}")
print(f"El area superficial del cilindro es de: {Area_Superficial_del_cilindro:.2f}")



