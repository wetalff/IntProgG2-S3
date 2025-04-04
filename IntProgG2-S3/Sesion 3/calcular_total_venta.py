#Leer x cantidad de producto comprado a x precio
#aplica el iva del 15%
#un descuento del 10
#Mostrar el total antes del IVA
#Monto del IVA
#Monto de descuento
#Total a pagar

""" Se debe leer el nombre del cliente, nombre del producto y mostrar una factura """
print("="*20)
print("Sistema de facturación")
print("="*20)
print("Ingresa los siguientes datos:")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
cantidad = float(input("Cantidad del producto: "))

total = precio * cantidad
IVA = total * 0.15
descuento = total * 0.10
Monto = total + IVA - descuento

import os
press_key = input("Presiona una tecla para continuar.....")
os.system("cls || clear")
print("+"*30)
print("Factura")
print("+"*30)
print(f"Cliente: {cliente}")
print("Productos \t Cantidad \t Precio \t total")
print(f"{producto:>15}  {cantidad:>15}  {precio:>15}  {total:>15}")
print(f"IVA: {IVA}")
print(f"Desc: {descuento}")
print(f"Monto: {Monto}")



