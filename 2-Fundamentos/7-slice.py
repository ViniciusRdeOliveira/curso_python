movieName = 'Top Gun'


#buscar toda a string apartir da primeira posição

print(movieName)
print(movieName[0:]) #como não foi delcarado o final da busca ele iráa retornar toda a string
print(movieName[:6]) #retorna toda a string menos a ultima letra
print(movieName[2:]) 

'''string[inicio:fim:passo]
indice começa na posição 0 | indice final -1
passo - determina o incremento. Pr padrão esse número é o 1.
'''

#buscar toda as string de 2 em 2 caracteres
print(movieName[::2]) #retorna toda a string de 2 em 2 caracteres

#buscar toda a string nos indices impares
print(movieName[1::2]) #retorna toda a string nos indices impares

#inverter uma string de tras para frente
print(movieName[::-1]) #retorna toda a string de tras para frente