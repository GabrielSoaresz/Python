from random import randint

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('-=' * 20)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-=' * 20)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')