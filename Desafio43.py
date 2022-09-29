"""Desenvolva um programa que leia o peso e a altura de uma pessoa e calcule seu IMC
de acordo com a tabela abaixo:
Abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
acima de 40: obesidade mórbida
"""
from math import pow

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = 0
imc = peso / pow(altura, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 25 > imc >= 18.5:
    print('Peso ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 > imc >= 30:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print('IMC: {:.1f}'.format(imc))