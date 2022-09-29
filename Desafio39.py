"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é hora de alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar quanto tempo falta ou que passou do prazo"""

from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade < 18:
    tempo = 18 - idade
    ano = atual + tempo
    print('Ainda vai se alistar ao serviço militar.')
    print('Faltam \033[4;32m{}\033[m ano(s).'.format(tempo))
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('É hora de se alistar!')
else:
    tempo = idade - 18
    ano = atual - tempo
    print('Já passou do tempo de alistamento.')
    print('Passou do prazo a \033[4;31m{}\033[m anos'.format(tempo))
    print('Seu alistamento foi em {}'.format(ano))