import os
os.system('cls' if os.name == 'nt' else 'clear')

# Condicionales If
edad = int(input("Ingresa tu edad: "))

if(edad>=21):
    print("Eres mayor de edad")
elif(edad>=18):
    print("Eres ciudadano")
else:
    print("Eres menor de edad")