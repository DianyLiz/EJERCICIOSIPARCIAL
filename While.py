#imprimir 10 valores con ciclo while
import os
os.system('cls' if os.name == 'nt' else 'clear')

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# print ("Ciclo controlado por un banderin")
# while True:
#     entrada = input("Ingresa s para salir ")
#     if entrada.upper()  == "s":
#         break

# print ("Ciclo controlado por un banderin 2")
# bandera = "x"
# while bandera != "S":
#     bandera = input("Ingresa S para salir ")

print ("Ciclo controlado por un banderin 2")
bandera = True
while bandera != False:
    bandera = input("Ingresa S para salir ")   
    if bandera.upper() == "S":
        bandera = False
        print ("Ciclo finalizado")