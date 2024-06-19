import os
os.system('cls' if os.name == 'nt' else 'clear')


lista_1 = ["C","C++","Python","Java"]
lista_2= ["PHP","SQL","Visual Basic"]

print (lista_1 + lista_2)

print(lista_1[1:3]) #>> ["C++""Python"]

lista_12= lista_1 + lista_2
print (lista_12)    

lista_3 = ["d","a","c","b","e"]
lista_4 = [5, 4, 7, 1, 9]

lista_13= lista_1+lista_3
print (lista_13)

lista_14= lista_1+lista_4
print (lista_14)

lista_5=[True,False]

lista_5.append(True)
print (lista_5)

lista_5.pop(True)
print (lista_5)


lista_5.reverse()
print (lista_5)
