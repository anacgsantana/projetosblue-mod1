from random import randint
import emoji
denovo = 'S'
while denovo == "S":
    count = countComp = countJogador = countTotalJogador = countTotalComp = 0
    rodadas = int(input("Quantas partidas deseja jogar? "))
    while count < rodadas:
        count +=1
        print(f"Essa é a rodada número {count}\n")
        print('VAMOS JOGAR JOKENPO\nEscolha uma opção')
        jogador = int(input(emoji.emojize('1 - Pedra :raised_fist:\n2 - Papel :raised_hand:\n3 - Tesoura :victory_hand:\n', use_aliases=True)))
        comp = randint (1,3)
        if (jogador==2 and comp==1) or (jogador==3 and comp==2) or (jogador==1 and comp==3):
            print(f'O jogador escolheu {jogador} e o computador escolheu {comp}, VOCÊ GANHOU \N{grinning face}')
            countJogador += 1
            countTotalJogador += 1
        elif jogador==comp:
            print(f'Você escolheu {jogador} e o computador escolheu {comp}, EMPATE \N{slightly smiling face}')
        else:
            print(f'Você escolheu {jogador} e o computador escolheu {comp}, VOCÊ PERDEU \N{crying face}')
            countComp += 1
            countTotalComp += 1
    denovo = input("Deseja jogar novamente?[S/N]").upper()
    if denovo == "S": #O if é para validar se o jogo irá continuar ou não
        continue 
    else:
        print (f'FIM DE JOGO! Você ganhou {countJogador} vezes e perdeu {countComp} vezes.\n')  
        if countTotalJogador > countTotalComp: 
            print (f'Você foi o grande ganhador, com um total de {countTotalJogador} vitórias')
        else:
            print (f'O grande ganhador foi o computador, com um total de {countTotalComp} vitórias')
        
        break