#Cálculo del tiempo total de una película con comerciales
Duración_de_la_pelicula_en_minutos = int(input("Dime la duración de la pelicula en minutos: "))
Duración_de_los_comerciales_previos = int(input("Dime la duración de los comerciales previos en minutos: "))
Pausas_comerciales = int(input("Dime la cantidad de pausas comerciales que ocurrieron durante la pelicula: "))
Duración_de_las_pausas_comerciales = int(input("Dime la duracion de cada pausa comercial: "))
Total_de_comerciales = Pausas_comerciales * Duración_de_las_pausas_comerciales
Duración_total = Duración_de_la_pelicula_en_minutos + Duración_de_los_comerciales_previos + Total_de_comerciales
print("La duración original de la pelicula es de: ",Duración_de_la_pelicula_en_minutos,"minutos")
print("La duración total de los comerciales fue de: ",Total_de_comerciales,"Minutos")
print("EL tiempo total de la proyección fue de: ",Duración_total,"Minutos")
