#ciclo for

import os
os.system('cls' if os.name == 'nt' else 'clear')


# for i in range(10): 
#     print(i)

# for i in range(2,20,2):
#     print(i)

#ciclo for con listas 
# lista = ["uno","dos","tres","cuatro","cinco"]
# for item in lista:
#     print(item)

#invertir el orden de una lista
# lista = ["uno","dos","tres","cuatro","cinco"]
# for item in reversed(lista):
#     print(item)

#con tuplas
# tupla = ("uno","dos","tres","cuatro","cinco")
# for item in tupla:
#     print(item)

#con diccionarios
# diccionario = {"curso":"Python TOTAL",
#                "clase":"Ciclos For",
#                "tema":" For",
#                "duracion":"2 horas",
#                "profesor":"Diany Lizbeth Enamorado"
#                }
# print(diccionario)
# for llave in diccionario:
#     print(llave,":",diccionario[llave])

#con diccionarios invertidos    
# diccionario = {"curso":"Python TOTAL",
#                "clase":"Ciclos For",
#                "tema":" For",
#                "duracion":"2 horas",
#                "profesor":"Diany Lizbeth Enamorado"
#                }
# print(diccionario)
# for llave in reversed(diccionario):
#     print(llave,":",diccionario[llave])

#hacer un ejercicio que pida que tabla de multiplkicar desea saber y muestre la tabla en pantalla
# tabla = int(input("Ingrese la tabla de multiplicar: "))
# for i in range(1,11):
#    print(tabla,"x",i,"=",tabla*i)

factorial = int(input("Ingrese el factorial: "))
resultado = 1
for i in range(1,factorial+1): 
    resultado *= i
print(f"{factorial}! = {resultado}")      

