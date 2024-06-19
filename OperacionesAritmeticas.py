#OPERACIONES ARITMETICAS
import os

os.system('cls' if os.name == 'nt' else 'clear')

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

print("Suma:", x + y)
print("Resta:", x - y)
print("la multiplicacion es:", x * y)

if y == 0:
    print("la division es:", x / y)
else:
    x = -x/y
    print("No se puede realizar la division")



