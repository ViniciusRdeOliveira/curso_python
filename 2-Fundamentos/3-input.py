#Utilizando o input

name = input("Digite o nome do filme:\n") #\n é utilizado para pular linha
yearLauch = input("Digite o ano de lançamento do filme:\n")
noteMovie = input("Digite a nota do filme:\n")  

print(type(name))
print(type(yearLauch))
print(type(noteMovie))

#irá retornar string. Tudo que é digitado pelo input retorna string

#convertendo para o tipo correto
yearLauch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n")) 
print(type(yearLauch))
print(type(noteMovie))