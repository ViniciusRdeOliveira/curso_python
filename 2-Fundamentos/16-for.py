moviesList = ["Titanic", "The Godfather","Inception", "Jurassic Park"]

 # 1 -Interando valores de uma lista

# for movie in moviesList:
#     print(movie)

# 2 -Quando a condição for atendida, o Loop será encerrado.

# for movie in moviesList:
#     if movie == "Inception":
#         break   #encerra o laço
#     print(movie)

# 3 - Quando a coindição for atendida, o Loop vai para a próxima interação

# for movie in moviesList:
#     if movie == "Inception":
#         continue   #pula para a proxima interação
#     print(movie)

# 4- Avaliaçãod o filme

movieName = input("Digite o nome do filme\n")
movieRating = int(input("Digite quantas avaliações deseja fazer\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme\n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average =0

print(f"Media de avaliação do filme {movieName} é {average:.2f}")