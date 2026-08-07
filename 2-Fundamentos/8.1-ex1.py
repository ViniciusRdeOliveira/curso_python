#Escreva um programa que le dois nomes e retorne uma string 
# formatada no seguinte formato: "último_nome, primeiro_nome".

print("="*20,"ATIVIDADE 1","="*20)

primeiroNome = (input("digite seu primeiro nome: "))
ultimoNome = (input("Digite seu último nome: "))

print(f"{ultimoNome},{primeiroNome}\n")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Inverta a ordem das palavras em uma string fornecida

print("="*20,"ATIVIDADE 2","="*20)

texto = "Python é muito interessante"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Verifique se uma string fornecida é um palíndromo 
# (uma palavra que é a mesma quando lida de trás para frente).

print("="*20,"ATIVIDADE 3","="*20)

texto1 = "arara"
texto2 = "python"

#remove espaços e coloca tudo em minúsculo
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

#verifica se o texto original é seu reverso
palidromo1 = texto1_format == texto1_format[::-1]
palidromo2 = texto2_format == texto2_format[::-1]

print(f"O texto '{texto1}' é um palíndromo? {palidromo1}")
print(f"O texto '{texto2}' é um palíndromo? {palidromo2}")


# Escreva um programa que leia uma palavra e um número inteiro n.
# O programa deve:
# Imprimir a palavra duas vezes concatenada (sem espaço).
# Imprimir a palavra repetida n vezes (usando multiplicação de string).

palavra = input()
n = int(input())

print(f"{palavra}{palavra}")
print(palavra*n)