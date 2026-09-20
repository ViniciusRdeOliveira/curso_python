import math

#1 acessar o numero pi
print(math.pi)
print(f"{math.pi:.2f}") #com duas casas decimais

#2- acessar o numero de Euler

print(math.e)
print(f"{math.e:.2f}") 

#3- arredondamento de números para cima e para baixo

num = 10.4

print(math.ceil(num))
print(math.floor(num))

#4- FAtorial de um número

num2 = int(input("Digite umn numero:\n"))
print(math.factorial(num2))

#5- potencia de números

print(math.pow(5,5))

#6- raiz quadrada de um número
print(math.sqrt(169))

#7 Maximo divisor comum
mdc= math.gcd(20,100)
print(mdc)

#8 logaritmo
print(math.log(10))
