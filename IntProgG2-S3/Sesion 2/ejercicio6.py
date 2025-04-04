#Cálculo del índice de masa corporal (IMC)
Peso_kg = float(input("Dime tu peso en kilogramos: "))
Altura_metros = float(input("Dime tu altura en metros: "))
IMC = (Peso_kg / (Altura_metros * Altura_metros))
print("Tu peso en kg es de:", Peso_kg,"Kg")
print("Tu altura en metros es de:", Altura_metros,"M")
print(f"Tu indice de masa corporal es de: {IMC:.2f}")
if IMC < 18.5:
    clasificación = "Bajo peso"
elif 18.5 <= IMC < 24.9:
    clasificación = "Peso normal"
elif 25 <= IMC < 24.9:
    clasificación = "Sobrepeso"
else:
    clasificación = "Obesidad"
    
print("La clasificacion de tu IMC es de:", clasificación)

