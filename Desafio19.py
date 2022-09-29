"""Um professor quer sortear um dos alunos para apagar o quadro.
Faça um programa que leia o nome dos alunos e escreva o nome do escolhido"""

import random
n1 = 'Aluno1'
n2 = 'Aluno2'
n3 = 'Aluno3'
n4 = 'Aluno4'
n5 = 'Aluno5'
lista = [n1,n2,n3,n4,n5]
sorteado = random.choice(lista)
print('O aluno sorteado foi: '+sorteado)
