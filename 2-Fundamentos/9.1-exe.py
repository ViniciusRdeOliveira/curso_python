# Escreva um programa que:
# Leia 3 números inteiros.
# Armazene esses números em uma lista.
# Imprima:
# A lista completa.
# O primeiro elemento da lista.
# A soma de todos os elementos da lista.

lista = []

num1 = int(input())
num2 = int(input())
num3 = int(input())

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(lista)
print(lista[0])
print(sum(lista))
