# import os
# os.system('cls' if os.name == 'nt' else 'clear')

# palabra = input("Ingresa la palabra a evaluar: ")

# palabra_invertida = palabra[::-1]

# if palabra == palabra_invertida:
#     print("La palabra ingresada es palíndromo.")
# else:
#     print("La palabra ingresada no es palíndromo.")


# print ("hola mundoooo".count("hola1"))

import os
os.system('cls' if os.name == 'nt' else 'clear')


mensaje="hola12345"
mensaje2="hola mundo"
numero="12345"
decimal="123.456"

# print(mensaje.isdigit())
# print(numero.isdigit())
# print(decimal.isdigit())

# print(mensaje.isnumeric())
# print(numero.isnumeric())
# print(decimal.isnumeric())

# print(mensaje.isdecimal())
# print(numero.isdecimal())
# print(decimal.isdecimal())       

# print(mensaje.isalnum())
# print(mensaje2.isalnum())

# mensaje3 = mensaje2.replace("hola","hello")
# print(mensaje3)

mensaje = "hola mundo cruel"
print(mensaje.split(" "))
nombre = "Diany*Lizbeth*Enamorado*Fernandez"
print(nombre.split("*"))
print(nombre.count("*"))
print(nombre.replace("*",","))