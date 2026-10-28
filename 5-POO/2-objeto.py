class Game:
    name = ""
    yearLauch = 0
    multiplayer = False
    note = 0

# Primeiro Jogo
game1 = Game()
game1.name = "The Legend Of Zelda: Breath of The Wild"
game1.yearLauch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo Jogo
game2 = Game()
game2.name = "Fortinite"
game2.yearLauch = 2017
game2.multiplayer = True
game2.note = 8.0

# Terceiro Jogo
game3 = Game()
game3.name = "Resident Evil Requiem"
game3.yearLauch = 2026
game3.multiplayer = False
game3.note = 10

# Quarto Jogo
game4 = Game()
game4.name = "Minecraft"
game4.yearLauch = 2009
game4.multiplayer = False
game4.note = 9.3

print("###Dados do Jogo###")
print(f"Nome do Jogo : {game1.name}\nAno Lançamento: {game1.yearLauch}")
print(f"Nome do Jogo : {game2.name}\nAno Lançamento: {game2.yearLauch}")