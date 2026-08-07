filmesList = ["Matrix", "Top Gun", "Avatar", "Interestelar", "Twistter"]

#tamanho da lista
print(len(filmesList)) #retorna o tamanho da lista

#recuperar item da lista pelo nome
print(filmesList.index('Interestelar')) #retorna o primeiro item da lista

#adicionar filme a lista

filmesList.append("O Poderoso Chefão") #adiciona um item ao final da lista
print(filmesList)

#ordernar lista

filmesList.sort() #ordena a lista em ordem alfabética  
print(filmesList)

#copiar intens de uma lista para outra
filmesCopy = filmesList.copy() #copia os itens da lista para outra lista

filmesCopy.remove("Top Gun") #remove um item da lista
print(filmesCopy) #imprime a lista copiada sem o item removido

filmesList.clear() #limpa a lista
print(filmesList) #imprime a lista vazia

