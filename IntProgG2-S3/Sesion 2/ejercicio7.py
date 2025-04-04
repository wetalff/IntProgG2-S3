#Cálculo del precio final de un producto con impuestos y descuentos 
Precio_Original_del_producto = float(input("Dime el precio original del producto: "))
Porcentaje_de_descuento = float(input("Dime el porcentaje del descuento a aplicar: "))
Precio_descuento = Precio_Original_del_producto - ((Precio_Original_del_producto * Porcentaje_de_descuento)/100)
IVA = float(input("Dime el porcentaje del IVA: "))
Precio_final = Precio_descuento + ((Precio_descuento * IVA)/100)
print(f"El precio original del producto es de: {Precio_Original_del_producto}, el descuento aplicado es del: {Porcentaje_de_descuento:.2f}, porciento, el precio con descuento es de: {Precio_descuento}, el IVA calculado es de: {IVA}, y el precio final es de: {Precio_final:.2f}")
