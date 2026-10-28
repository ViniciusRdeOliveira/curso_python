class Game:
    def __init__(self, name="", yearLauch = 0 , multiplayer = 0, note = 0): #construtor
        self.name = name
        self.yearLauch = yearLauch
        self.multiplayer = multiplayer
        self.note = note


    def __str__(self): #sobrescreve o valor quando instanciado na classe. Self ffaz referencia aos atributos da classe
        return f"Game: {self.name}" #quando estanciado a classe, traz o nome do jogo.

game1 = Game("The legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
# game1.name = "Super Mario Odissey"
# print(game1)

print("###Dados do Jogo###")
print(f"Nome do Jogo : {game1.name}\nAno Lançamento: {game1.yearLauch}")
print(f"Nome do Jogo : {game2.name}\nAno Lançamento: {game2.yearLauch}")