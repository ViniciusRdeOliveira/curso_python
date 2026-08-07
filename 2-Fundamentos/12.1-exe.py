# Escreva um programa que:
# Leia cinco números inteiros (podendo haver repetidos).
# Armazene-os em um set para eliminar duplicatas.
# Imprima:
# O set resultante.
# A quantidade de elementos únicos.
# O maior elemento do set.

numeros = set()

numeros.add(int(input()))
numeros.add(int(input()))
numeros.add(int(input()))
numeros.add(int(input()))
numeros.add(int(input()))

print(numeros)
print(len(numeros))
print(max(numeros))