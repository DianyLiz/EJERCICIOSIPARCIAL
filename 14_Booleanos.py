import os
os.system('cls' if os.name == 'nt' else 'clear')

# Valores Booleanos
mibool = True

a = 6 > 5
b = 30 == 15*3

# Comparaciones
print(mibool == a and mibool == b) # Mostrara verdadero o falso dependiendo de las comparaciones
print(not(mibool == a and mibool == b)) # Invierte el valor de la comparacion