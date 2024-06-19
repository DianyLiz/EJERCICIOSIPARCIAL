#crear un programa que de un descuento de 20% al cliente que lleve mas de 10 productos 

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Ingrese la cantidad de productos que lleva:")
cantidad = int(input())

print("Ingrese el precio del producto:")
precio = int(input())

total = cantidad * precio

if cantidad > 10:
    descuento = (0.20 / 100) * precio
    precio_desc = precio - descuento
    print("El precio con descuento es:", precio_desc)
else:
    print("El precio sin descuento es:", precio)

if total > 10000:
    print("Se te aplicó un 20% de descuento.")
else:
    print("No se te aplicó un 20% de descuento.")

print("Total de la compra es:", total)


