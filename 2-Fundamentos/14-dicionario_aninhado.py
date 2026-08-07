import pprint

filmsDict = {
    "inception":{
        "yearRealese": 2010,
        "imdbRating": 8.8,
        "genre": ['Action', 'Adventure', 'Sci-Fi']
    },
    "Interstelar":{
            "yearRealese": 2014,
            "imdbRating": 8.6,
            "genre": ['Drama', 'Sci-Fi']
    },
    "The Dark Knight":{
            "yearRealese": 2008,
            "imdbRating": 9.0,
            "genre": ['Ação']
    }
}

pp=pprint.PrettyPrinter(depth=4)

# pp.pprint(filmsDict)

#buscar uma informação dentro de um dicionario aninhado

print(filmsDict["Interstelar"]["genre"])

#adicionar um item
filmsDict["inception"]["director"] = "Cristopher Nolan"
print(filmsDict["inception"])

#excluir um dicionario
del filmsDict["The Dark Knight"]
pp.pprint(filmsDict)