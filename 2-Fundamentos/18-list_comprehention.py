# 1 Listar valores de 0 1 10  que sejammenores que 4.

listNumbers = [ i for i in range(10)if i <4]
print (listNumbers)

#lista de filmes
moviesList = ["Titanic", "The Godfather","Inception", "Jurassic Park"]

# 2-  Filmes que possuem a letra 'e' no titulo

moviesWithE = [movie for movie in moviesList if 'e' in movie.lower()] #passando para lower poisa inicial de cada filme está com letra maíuscula.
print(moviesWithE)

# 3- Filmes que eu assisti

moviesWatched = [movie for movie in moviesList if movie != "Jurassic Park"]
print (moviesWatched)

# 4 encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("Programa Encerrado")
        break

    foundMovie = [movie for movie in moviesList if searchName.lower() in movie.lower()] #se a busca estiver dentro da lista ele printa
    if foundMovie:
        print(f"Filme(s) encontrado s com o nome : {searchName}:")
        for foundMovie in foundMovie:
            print (foundMovie)

    else:
        print(f"Nenhum filme com o nome {searchName} foi encontrado")