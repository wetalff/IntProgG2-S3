#Cálculo del salario neto de un empleado
Salario_Bruto = float(input("Dime el salario bruto del empleado: "))
impuesto_sobre_la_renta = 0.10 * Salario_Bruto
Seguro_social = 0.05 * Salario_Bruto
Fondo_de_pensiones = 0.03 * Salario_Bruto
Descuentos_Totales = impuesto_sobre_la_renta + Seguro_social + Fondo_de_pensiones
Salario_Neto = Salario_Bruto - Descuentos_Totales
print("El salario bruto del empleado es: ", Salario_Bruto)
print("El descuento total incluyendo el impuesto sobre la renta, el seguro social y el fondo de pensiones es de: ", Descuentos_Totales)
print("El salario neto del empleado es: ", Salario_Neto)



