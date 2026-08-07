# print("="*20,"ATIVIDADE 1","="*20)

# primeiroNome = (input("digite seu primeiro nome: "))
# ultimoNome = (input("Digite seu último nome: "))

# print(f"{ultimoNome},{primeiroNome}\n")

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print("="*20,"ATIVIDADE 2","="*20)

# texto = "Python é muito interessante"
# palavras = texto.split()
# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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