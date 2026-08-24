# 1- Fução para imprimir um nome completo

def full_name(first_name, last_name):
    print(f"Nome é {first_name} {last_name}")

full_name("Fulano","Sicrano")

# 2- Função para somar 2 numeros
def sum_numbers(a,b):
    return a+b

print(f"a Soma é {sum_numbers(2,5)}")

#3 - Função com paramentro default

def address(country="Brasil"):
    print(f"Eu moro em: {country}")

address()
address("Portugal")

def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nora para o filme:\n"))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"Media de avaliação do filme {movie_name} é : {average:.2f} ")

rate_movie(2, "Sonic")