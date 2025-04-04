#Conversión de unidades de tiempo
Total_segundos = int(input("Dime la cantidad total de segundos: "))
Horas = int(Total_segundos / 3600)
Segundos_Remanentes = int(Total_segundos - (Horas * 3600))
Minutos = int(Segundos_Remanentes / 60)
Segundos_restantes = int((Segundos_Remanentes - (Minutos * 60)))
print("La cantidad de horas es de :", Horas,"h.")
print("La cantidad de minutos es de:", Minutos,"m.")
print("La cantidad de segundos restantes es de:", Segundos_restantes,"s.")
