"""Crie um programa que leia as duas notas de um aluno
e mostre a média"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

med = (nota1+nota2)/2

print('A media é: {:.1f}'.format(med))