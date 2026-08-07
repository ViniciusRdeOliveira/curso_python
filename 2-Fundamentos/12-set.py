filmsSet = {"Matrix", "Top Gun", "Avatar", "Interestelar", "Twistter"}
#print(type(filmsSet)) #retorna o tipo da variável, nesse caso um set

#buscar o tamanho do set
#print(len(filmsSet)) #retorna o tamanho do set

#True e valor 1 são considerados iguais, assim como False e 0

exampleSet = {"Inception", True, 1, 8.7}
#print(exampleSet) #retorna o set com os valores, mas não garante a ordem dos elementos

#adicionar um item de outro set
filmsSet.update(exampleSet)

print(filmsSet) #retorna o set atualizado com os valores do outro set

#remover um item no set

filmsSet.remove(True)
filmsSet.remove(8.7)

print(filmsSet) #retorna o set atualizado sem os valores removidos