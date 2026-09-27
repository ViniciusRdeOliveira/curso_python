import hashlib

# #1- Verificar algoritimos disponíveis
# print(hashlib.algorithms_available)

# #2- verificar algoritimos de acordo com o SO
# print(hashlib.algorithms_guaranteed)

#3 - Utilizando o sha256

algorithm = hashlib.sha256()
print(algorithm.digest())

mensagem = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(mensagem)
print(algorithm.hexdigest())

#4- utilizando o MD5 (usado para comprovar a integridade de dados)

md5= hashlib.md5()
md5.update(mensagem)

print(md5.hexdigest())