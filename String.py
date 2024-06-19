import os
os.system('cls' if os.name == 'nt' else 'clear')



saludo = "Hola_Mundo"

try:
    print(saludo.index('o',4,7))
except ValueError:
    print("No se encontro la subcadena")
#rindex() devuelve la posicion de la ultima ocurrencia
print(saludo.rindex('o'))

print(saludo[0:4])

cedula = "1601200400767"
departamento = cedula[0:2]
print(departamento)
municipio = cedula[0:4]


print("Hola".islower())

print("Hola".isupper())

print(saludo[2:6])

print(saludo[3::3])
saludo="ho1l4a5_8m8u8n8d8o"
print(saludo[2::2])

saludo=saludo[::-1]
print(saludo[::-1])