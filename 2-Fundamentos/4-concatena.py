name = input("Digite o nome do filme:\n")
yearLauch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n")) 

#Alternativa 1

print("Dados do Filme:\n")
print("=================================")
print("Nome do Filme:", name)
print("Ano de Lançamento:", yearLauch)
print("Nota do Filme:",noteMovie)

#Alternativa 2
print("Nome do Filme:",name, "\nAno de Lançamento:", yearLauch, "\nNota do Filme:", noteMovie)

#alternativa 3
print(f"Nome do Filme: {name}\n"
      f"Ano de Lançamento: {yearLauch}\n"
      f"Nota do Filme: {noteMovie}"
      )