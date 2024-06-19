#Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b*x + c = 0
# a, b, c
def discriminante(a, b, c):
    discrim = (b**2)-(4*a*c)
    return discrim

def sdiscrimin():
  discrim 
  return

def raices(a, b, discrim):
  #raiz1=(-b + sqrt(discrim))/(2*a)
  #raiz2=(-b - sqrt(discrim))/(2*a)
  raiz1=(-b + (discrim**.5))/(2*a)
  raiz2=(-b - (discrim**.5))/(2*a)
  cero = -b/(2*a)
  return raiz1,raiz2,cero

    #enter code here

print('Calculo de raices')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
disc=discriminante(a,b,c)

if disc < 0:
  print("No hay raices positivas")

elif sdiscrimin == 0:
  print('Solo existe una raiz')
  print(raices(cero))
  
else:
  print("La raices son: ")    
  print(raices(a,b,c))