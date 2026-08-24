# função de potencia de um número

power = lambda num: num **2
print(power(5))
print(power(9))

#função que verifica se o numerp é par
is_even = lambda x: x %2 ==0

print(is_even(27))
print(is_even(30))

#função que divide um numero por outro

div_num = lambda x,y: x/y
print (div_num(10,2))
print (div_num(6,2))

#função que inverte uma sttring

rever_string = lambda s: s[::-1]
print(rever_string("python"))
print(rever_string("javascript"))

#funcionalidades relacionadas ao filmes
movie_list = ["Titanic", "The Godfather", "Inception",  "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic":[8.5, 9.0, 7.5],
    "The Godfather":[9.5, 8.9, 8.0],
    "Inception":[8.0, 7.0, 8.5],
    "Jurassic Park":[7.5, 5.0, 3.5],
    "The Matrix":[9.5, 9.0, 9.5],
}

#função para calcular a média de avaliações de um filme

average_rating = lambda movie_name: sum(ratings[movie_name])/ len(ratings[movie_name])
print (f"Média de Avaliação do filme The Matrix: {average_rating("The Matrix")}")

#função que verifica se um filme está na lista

check_movie = lambda movie_name:  movie_name in movie_list
print(f"INception está na lista?{check_movie("Inception")}")

#Fução para recomendar um filme com base na avaliação média

recomend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"
print(f"{recomend_movie("Titanic")}")