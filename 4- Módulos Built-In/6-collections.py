from collections import Counter, namedtuple, deque
from operator import itemgetter

#1- Lista de frutas (contagem)

fruits = ["Maçã", "Banana", "Uva", "Banana", "Pêra", "Maçã", "Laranja", "Banana"]

print(fruits)
print(Counter(fruits))

#2- Utilizando uma tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("residet Evil", 109.90, 9.5)
g3 = game("Teste", 200, 10)

print(g1)
print(g2)
print(g3)

#3 - Ordenando dicionários

students = {"Pedro": 23, "Ana":22, "Ronaldo":26, "Janaina":20}

a = sorted(students.items(), key = itemgetter(0)) #ao mudar o indice para 1, ele ordena por idade

print(a)

#4- Utilizando uma fila em ambas as extermidades

deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)

deq.append(90)
deq.popleft()
deq.pop

print(deq)