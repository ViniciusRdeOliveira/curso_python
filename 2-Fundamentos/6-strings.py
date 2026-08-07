movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2) #python é case sensitive, ou seja, diferencia maiúsculas de minúsculas

movieDescription = """ #strings multilinhas
    top gun é um filme de ação e drama lançado em 1986, dirigido por Tony Scott e estrelado por Tom Cruise. 
    O filme segue a história de Pete "Maverick" Mitchell, 
    um talentoso piloto da Marinha dos Estados Unidos, enquanto ele 
    compete para se tornar o melhor piloto da escola de elite de aviação conhecida como "Top Gun". 
    O filme é conhecido por suas emocionantes cenas de voo, trilha sonora icônica e 
    pelo impacto cultural que teve na década de 1980.

"""
print(movieDescription)

#multiplicação de strings
line = "="
print(line*20)

#procurar uma palavra dentro de um texto
print("top gun" in movieDescription) #retorna True ou False