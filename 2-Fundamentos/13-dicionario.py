
#Dicionario é muito parecido com JSON

filmInception = {
    "title": "Inception",
    "yearRealese": 2010,
    "imdbRating": 8.8,
    "genre": ['Action', 'Adventure', 'Sci-Fi']
}

print(filmInception) #retorna o dicionário com os valores
print(len(filmInception))
print(type(filmInception))

#recuperar/exibir um elemento do dicionario

print(filmInception["genre"])
print(filmInception.get("imdbRating"))

#buscar apenas as chaves do dicionário
print(filmInception.keys())

#buscar somente os valores
print(filmInception.values())


#buscar itens do dicionar com chave e valor
print(filmInception.items())

#adicionar um item ao dicionario
filmInception["director"] = "Cristopher Nolan"
print(filmInception)


#adicionando itens no dicionario
filmInception.update({"imdbRating": 8.7})
print(filmInception)

#removendo item no dicionario
filmInception.pop("director")
print(filmInception)