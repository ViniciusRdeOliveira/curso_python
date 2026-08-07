filmesTuple = ("Matrix", "Top Gun", "Avatar", "Interestelar", "Twistter")

print(type(filmesTuple)) #retorna o tipo da variável, nesse caso uma tupla

#buscar os dois primeiros itens da tupla
print(filmesTuple[0:2]) #retorna os dois primeiros itens da tupla

#buscar o ultimo item da tupla
print(filmesTuple[-1]) #retorna o ultimo item da tupla

#buscar filmes até uma determinada posição
print(filmesTuple[:3])

#buscar filmes de uma posição em diante
print(filmesTuple[2:])

#recuperar um item da tupla pelo nome
print(filmesTuple.index("Interestelar")) #retorna a posição do item na tupla