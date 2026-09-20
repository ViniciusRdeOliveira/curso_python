import os

#1- Retornar a pasta atual

print(os.getcwd())

#2- listar arquivos e pastas

print(os.listdir())

#3 - verificar a versão do SO

os.system('ver')

#4- configurações da máquina

os.system('systeminfo')

#5- limpar a tela do terminal

os.system('cls')

#6 - DEsligar o computador

#os.system('shutdown /s') desliga após 60 segundos
#os.system('shutdown /a') cancela o desligamento
#os.system('shutdonw /s /t 0') desliga o computador imediantamente 

def turn_of_one_hour():
    os.system('shutdonw /s /t 3600')
