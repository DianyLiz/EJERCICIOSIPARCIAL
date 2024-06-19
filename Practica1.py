
texto = input("Por favor, ingresa un texto: ").lower()
letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()
f_letra1 = texto.count(letra1)
f_letra2 = texto.count(letra2)
f_letra3 = texto.count(letra3)
print(f"1. Frecuencia de letras:")
print(f"   - La letra '{letra1}' aparece {f_letra1} veces.")
print(f"   - La letra '{letra2}' aparece {f_letra2} veces.")
print(f"   - La letra '{letra3}' aparece {f_letra3} veces.")
palabras = texto.split()
cantidad_palabras = len(palabras)

print(f"2. Cantidad de palabras en el texto: {cantidad_palabras}")
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"3. Primera letra del texto: '{primera_letra}', Última letra del texto: '{ultima_letra}'")
palabras_invertidas = palabras[::-1]
texto_invertido = ' '.join(palabras_invertidas)
print(f"4. Texto con palabras invertidas: {texto_invertido}")

if 'python' in palabras:
    print("5. La palabra 'Python' está presente en el texto.")
else:
    print("5. La palabra 'Python' no está presente en el texto.")
