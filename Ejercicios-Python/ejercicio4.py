#Cálculo del tiempo total de un viaje con escalas
Primer_tramo_de_vuelo = float(input("Dime la duración del primer tramo de vuelo (en horas): "))
Primera_escala = float(input("Dime la duración de la primera escala (en horas): "))
Segundo_tramo_de_vuelo = float(input("Dime la duración del segundo tramo de vuelo (en horas): "))
Segunda_escala = float(input("Dime la duración de la segunda escala (en horas): "))
Tercer_tramo_de_vuelo = float(input("Dime la duración del tercer tramo de vuelo (en horas): "))
tiempo_total = Primer_tramo_de_vuelo + Primera_escala + Segundo_tramo_de_vuelo + Segunda_escala + Tercer_tramo_de_vuelo
print("El tiempo total del viaje es de: ",tiempo_total," horas")

