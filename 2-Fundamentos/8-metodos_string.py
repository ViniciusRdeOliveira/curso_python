movieName = 'Top Gun'
movieDescription = """ #strings multilinhas
    top gun é um filme de ação e drama lançado em 1986, dirigido por Tony Scott e estrelado por Tom Cruise. 
    O filme segue a história de Pete "Maverick" Mitchell, 
    um talentoso piloto da Marinha dos Estados Unidos, enquanto ele 
    compete para se tornar o melhor piloto da escola de elite de aviação conhecida como "Top Gun". 
    O filme é conhecido por suas emocionantes cenas de voo, trilha sonora icônica e 
    pelo impacto cultural que teve na década de 1980.

"""

print(movieName.upper()) #retorna a string em maiúsculo
print(movieName.lower()) #retorna a string em minúsculo
print(movieName.capitalize()) #retorna a string com a primeira letra em maiúsculo
print(movieName.title()) #retorna a string com a primeira letra de cada palavra em maiúsculo
print(movieName.center(10, '-')) #retorna a string centralizada com o caractere '-' preenchendo os espaços
print(movieName.find("u")) #retorna o índice da primeira ocorrência da letra 'u'
print(movieName.replace("Top", "Matrix")) #substitui a palavra 'Top' por 'Matrix'
print(movieDescription.split(',')) #divide a string em uma lista de palavras