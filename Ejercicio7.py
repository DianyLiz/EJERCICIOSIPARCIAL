
import os
os.system('cls' if os.name == 'nt' else 'clear')

renta = int (input("Ingrese su renta anual: "))

if(renta<60000 ):
    print("Su renta es del tipo impositivo de 10%")
elif(renta>=60000):
    print("Su renta es del tipo impositivo de 45%")
else:
    print("Error")