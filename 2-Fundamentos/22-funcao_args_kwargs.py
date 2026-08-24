"""
*args Utilizamos ele quando não temos certeza de quantos argumentos queremos ter em uma função
- Os argumentos são passados com uma tupla
**kwargs Além de valores podemos passar também as respecitas chaves para cada argumento
- Os valores são passados com oum dicionário
"""

#1 Soma de numeros
def sum(*num): #ASTERÍSCO REFERE-SE AO ARGS
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é {sum_total}")

sum(7)
sum(7,9)
sum(7,9,10,11)


def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos:")
presentation(name="Python", category = "Backend", level = "Iniciante")
presentation(name="Visão computacional", category = "IA", level = "Avançado")
presentation(name="Dashboard com Dash", category = "Data Science", level = "Intermediário")