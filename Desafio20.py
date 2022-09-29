"""O mesmo professor do desafio anterior quer sortear a ordem de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random
n1 = 'Aluno1'
n2 = 'Aluno2'
n3 = 'Aluno3'
n4 = 'Aluno4'
n5 = 'Aluno5'
lista = [n1,n2,n3,n4,n5]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)