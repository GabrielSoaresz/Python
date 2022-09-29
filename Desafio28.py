"""Escreva um programa que faça o computador escolher um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""

import random,emoji
from time import sleep
n = int(input('Adivinhe o número: ')) #Jogador tenta adivinhar
num = random.randint(0,5) #Computador "PENSA" em um número

print('O computador pensou no número {}'.format(num))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print(emoji.emojize('Parabéns! Você acertou! :beaming_face_with_smiling_eyes:'))
else:
    print(emoji.emojize('Você errou.:confused_face:'))