# PORTUGUESE VERSION (A versão em inglês está abaixo do jogo atual)
import random
from time import sleep
partida = {'jogador1':0, 'jogador2':0} # Guardar os resultados dos dados em um dicionário.
vitoriaJogadorUm = vitoriaJogadorDois = 0
contador = int(input('\nInforme quantas rodadas vai jogar: ')) # Pergunta quantas rodadas você quer fazer;
while True :
    for i in range(1, contador+1):
        input('Aperte ENTER')
        sleep(2)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        print(f'Rodada {i}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        jogador1 = [random.randint(1,2)]
        jogador2 = [random.randint(1,2)]
        print(f'Jogador 1 tirou {jogador1}\n') 
        print(f'Jogador 2 tirou {jogador2}\n')
        if jogador1 > jogador2: # Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
            vitoriaJogadorUm +=1
            partida['jogador1'] +=1
        elif jogador1 < jogador2:
            vitoriaJogadorDois +=1
            partida['jogador2'] +=1
        else:
            pass
        contador += 1

    print('O resultado foi: \n')  # Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.
    print(partida)
    print()
    if vitoriaJogadorUm > vitoriaJogadorDois:
        print(f'Vitoria do jogador 1')
        break
    elif vitoriaJogadorDois > vitoriaJogadorUm:
        print(f'Vitoria do jogador 2')
        print()
        break
    else: 
        print(f'EMPATE\n')
        break

#ENGLISH VERSION

import random
from time import sleep
game = {'player1':0, 'player2':0} # Save data results in a dictionary.
victoryPlayerOne = victoryPlayerTwo = 0
count = int(input('\nHow many times do you want to play? ')) # Ask how many rounds you want to do;
while True :
    for i in range(1, count+1):
        input('Press ENTER')
        sleep(2)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        print(f'Game {i}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        player1 = [random.randint(1,2)]
        player2 = [random.randint(1,2)]
        print(f'Player 1 got {player1}\n') 
        print(f'Player 2 got{player2}\n')
        if player1 > player2: # Sort this dictionary, knowing that the winner rolled the highest number on the dice.
            victoryPlayerOne +=1
            game['player1'] +=1
        elif player1 < player2:
            victoryPlayerTwo +=1
            game['player2'] +=1
        else:
            pass
        count += 1

    print('The result was: \n')  # Show at the end which player won the most rounds and was the great champion.
    print(game)
    print()
    if victoryPlayerOne > victoryPlayerTwo:
        print(f'Player 1 win')
        break
    elif victoryPlayerTwo > victoryPlayerOne:
        print(f'Player 2 win')
        print()
        break
    else: 
        print(f'Neither players scored and the match ended in a draw\n')
        break