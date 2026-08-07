# Escreva um programa que:
# Leia o nome de três produtos e seus respectivos preços.
# Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).
# Imprima:
# O dicionário completo.
# O produto mais caro.
# A média dos preços.

produtos = {}

nome = input("Nome do Produto\n")
preco = float(input("Preço\n"))
produtos[nome] = preco

nome = input("Nome do Produto\n")
preco = float(input("Preço\n"))
produtos[nome] = preco

nome = input("Nome do Produto\n")
preco = float(input("Preço\n"))
produtos[nome] = preco

print(produtos)

produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro)

media = sum(produtos.values()) / len(produtos)
print(f"{media:.2f}")