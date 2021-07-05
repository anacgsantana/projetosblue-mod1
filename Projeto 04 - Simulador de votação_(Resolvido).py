def autorizavoto(y):
    from datetime import date #Economia de memória ao importar a biblioteca datetime dentro da função
    year_day = date.today().year
    idade = year_day - y
    
    if idade >= 16 and idade <= 63:
        return f'Com a idade de {idade} anos \33[1;32m[VOTO OBRIGATORIO]\33[m'
    elif idade >= 64:
        return f'Com a idade de {idade} anos \33[1;33m[VOTO OPCIONAL]\33[m'
    elif idade < 16:
        return f'Com a idade de {idade} anos \33[1;31m[VOTO NEGADO]\33[m'
      
    
#Programa principal
while True:
    nasc = int(input('Em que ano você nasceu?: '))
    print(autorizavoto(nasc))
    print()
    if autorizavoto == 'VOTO NEGADO':
        break
    totais = [0,0,0,0,0]
    
    candidatos =['Luciano Huck', 'Bolsonaro', 'Lula', 'Voto Nulo', 'Voto em Branco']
    print ('''-=-=-=-=-=-=-=-=-CANDIDATOS À PRESIDÊNCIA ELEIÇÕES 2021-=-=-=-=-=-=-=-=-
        1 - Luciano Huck
        2 - Bolsonaro
        3 - Lula
        4 - Voto Nulo
        5 - Voto em Branco
        0 - ENCERRAR
        ''')
    print()

    votacao = int(input('Digite o número do Candidato:  '))
    while votacao != 0:                                     
        totais[votacao-1] += 1
        totalvotos = sum(totais)                             
        vencedor = max(totais)   


        for i in range(len(totais)):
            perc = totais[i]/totalvotos * 100
            print('\nCandidato: {0}\nvotos: {1}\nPercentual:{2:.2f}%'.format(candidatos[i],totais[i], perc))
            if vencedor == totais[i]:
                v = i

        print('\n\nO candidato', candidatos[v], 'foi ELEITO')
        break