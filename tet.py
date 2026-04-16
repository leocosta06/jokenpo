import random
import time
lista=['papel','pedra','tesoura']
lista2=['sair', 'continua']
pc=[]
player=[]
vitoria=0
empate=0
derota=0
contador=0
while True:
    jogador=input("escolha:\n papel\n pedra\n tesoura \n ").replace(" ","").lower()
    if jogador not in lista:
        print('tente novamente')
        continue
    jogada=random.choice(lista)
    print("Pedra...")
    time.sleep(0.5) # Pausa de meio segundo
    print("Papel...")
    time.sleep(0.5)
    print("Tesoura!!!")
    time.sleep(0.3)
    print(jogada)
    if jogador==jogada:
        print("empate")
    elif jogador=='papel' and jogada=='pedra':
        print("ganhor")
    elif jogador=='papel' and jogada=='tesoura':
        print("perdeu")
    elif jogador=='pedra' and jogada=='tesoura':
        print("ganhor")
    elif jogador=='pedra' and jogada=='papel':
        print("perdeu")
    elif jogador=='tesoura' and jogada=='papel':
        print("ganhor")
    elif jogador=='tesoura' and jogada=='pedra':
        print("perdeu")
   
    pc.append(jogada)
    player.append(jogador)
    contador+=1
    if (jogador == 'papel' and jogada == 'pedra') or \
         (jogador == 'pedra' and jogada == 'tesoura') or \
         (jogador == 'tesoura' and jogada == 'papel'):
        vitoria+=1
    elif jogador==jogada:
        empate+1
    else:
        derota+=0
    sair=input("deseja sair digita SAIR \n ").replace(" ","").lower()
    if sair!='sair':
        print('tente novamente')
        continue
    elif sair=='sair':
        break

print(pc)
print(player)
print('------{vitoria}------\n------{derota}------\n------{empate}------')