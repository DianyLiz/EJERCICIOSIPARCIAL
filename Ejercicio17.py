import os
os.system('cls' if os.name == 'nt' else 'clear')

edad1 = int(input("Ingrese su Edad de identidad: "))

edad = 2024 - int(edad1)
anio = 2024 - edad1

for i in range(1,edad1+1): 
    anio = 2024 - edad1
    print("Edad: ",i,"=",anio +i)   