import random
from time import sleep
partida = {'jogador1':0, 'jogador2':0} # Guardar os resultados dos dados em um dicionário.
vitoriaJogadorUm = vitoriaJogadorDois = 0
contador = int(input('Informe quantas rodadas vai jogar: ')) # Pergunta quantas rodadas você quer fazer;
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
        print(f'EMPATE')
        break