#Conversión de una cantidad en dólares a distintas monedas
Cantidad_dolares = float(input("Dime la cantidad total de dolares a converitr: "))
Tasa_Euros = 0.92
Tasa_Libras = 0.77
Tasa_Yenes = 147.59
Cantidad_en_Euros = Cantidad_dolares * Tasa_Euros
Cantidad_en_Libras = Cantidad_dolares * Tasa_Libras
Cantidad_en_Yenes = Cantidad_dolares * Tasa_Yenes
print("La cantidad de dolares a convertida fue de: ",Cantidad_dolares," USD")
print("La cantidad de dolares mencionada convertida a euros fue de: ", Cantidad_en_Euros," Euros")
print("La cantidad de dolares mencionada convertida a libras fue de: ", Cantidad_en_Libras," Libras")
print("La cantidad de dolares mencionada convertida a yenes fue de: ", Cantidad_en_Yenes," Yenes")
