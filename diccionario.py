import os
os.system('cls' if os.name == 'nt' else 'clear')


estudiante = {}

numero = input("Ingrese el número: ")
nombre = input("Ingrese el nombre: ")
edad = input("Ingrese la edad: ")
estudiante[numero] = {'nombre': nombre, 'edad': edad}
print(f"Persona agregada: {estudiante[numero]}")

numero_buscar = input("Ingrese el número de la persona que desea buscar: ")
if numero_buscar in estudiante:
    print(f"Información de la persona: {estudiante[numero_buscar]}")
else:
    print("La persona con ese número no existe.")

if estudiante:
    print("Lista de personas ingresadas:")
    for numero, info in estudiante.items():
        print(f"Número: {numero}, Nombre: {info['nombre']}, Edad: {info['edad']}")
else:
    print("No hay personas ingresadas.")
