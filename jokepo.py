import random
import time
# funcao paraa logicca do jokepo
def logica_jogo (player_pc ,player):
    if (player == 'papel' and player_pc == 'pedra') or \
         (player == 'pedra' and player_pc == 'tesoura') or \
         (player == 'tesoura' and player_pc == 'papel'):
         return 'VITORIA'
    if player==player_pc:
         return "EMPATE"
    else:
        return"DERROTA"

# lista e variáveis
lista=['papel','pedra','tesoura']
pc=[]
player=[]
vitoria=0
empate=0
derrota=0
contador=0
# loop pra jogar
while True:
    jogador=input("escolha:\n papel\n pedra\n tesoura \n ").replace(" ","").lower()
    if jogador not in lista:
        print('tente novamente')
        continue
    #  jogada do pcc
    jogada=random.choice(lista)
    resultado=logica_jogo(jogada,jogador)
    print("Pedra...")
    time.sleep(0.5) 
    print("Papel...")
    time.sleep(0.5)
    print("Tesoura!!!")
    time.sleep(0.3)
    print(jogada)
    # resultado da rodada
    if resultado == 'VITORIA':
        vitoria += 1
    elif resultado == 'EMPATE':
        empate += 1
    else:
        derrota += 1
    #historico dos playeres
    pc.append(jogada)
    player.append(jogador)
    contador+=1
    # sair do loop
    sair = input("Deseja sair? Digite 'sair' ou ENTER para continuar: ").lower()
    if sair == 'sair':
        break
#resultado final
print(pc)
print(player)
print(f'------{vitoria}------\n------{derrota}------\n------{empate}------')