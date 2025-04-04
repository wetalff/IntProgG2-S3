#Cálculo de área y perímetro de un rectángulo 
Base_Rec = float(input("Dime la base del rectangulo: "))
Alt_Rec = float(input("Dime la altura del rectangulo: "))
Area_Rec = Base_Rec * Alt_Rec
Base_por_dos = Base_Rec * 2
Alt_por_dos = Alt_Rec * 2
Perimetro = Base_por_dos + Alt_por_dos
print("El area del rectangulo es: ",Area_Rec)
print("El perimetro del rectangulo es: ",Perimetro)
