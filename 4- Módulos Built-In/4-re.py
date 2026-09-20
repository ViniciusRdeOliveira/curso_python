import re

text = "Udemy - uma plataforma com muitos cursos"

#1- Indice inicial e indice final de palavras
# 0 r significa uma raw string(string bruta)

match = re.search(r'muitos cursos', text) #o que deve procurar e onde

print(f"Indice inicial:\n{match.start()}")
print(f"Indice final:\n{match.end()}")

#2- Buscando o indice que possui o ponto

site = 'https://udemy.com'
match = re.search(r'\.', site)

print(match)

#3- buscar uma lista de caracteres dentro de uma frase

pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

#4- verificando o inicio de uma string

rule = r'^A'
phrases = ['A casa está suja','O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        (print(f"Não corresponde: {f}"))

#5- VErificando o final de uma string

rule_end = r'!$'
phrase2 = 'O dia está lindo!'
match = re.search(rule_end, phrase2)
if match:
    print(f"Sim, corresponde")
else:
    print(f"Não corresponde")