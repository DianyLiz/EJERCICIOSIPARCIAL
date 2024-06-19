import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_diccionario = {"curso":"Python TOTAL","clase":"Diccionarios"}
mi_diccionario["recursos"] = ["notas","ejercicios","examen","proyecto"]
print(mi_diccionario["recursos"][3])

