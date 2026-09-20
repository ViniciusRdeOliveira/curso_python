import statistics

#1 aplicando média
print(statistics.mean([3,2,3,8,9]))

#2 aplicando mediada
print(statistics.median([1,2,4,8,9]))
print(statistics.median([1,2,3,7,8,9]))

#3- Aplicando a Moda (numero que mais se repete)
print(statistics.mode([2,5,3,2,8,3,9,4,2,6,5]))

#4- desvio padrão
"""quanto mais próximo for de 0 o desvio padrão, significa que os dados do conjunto estão menos dispersos
"""

print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5]))