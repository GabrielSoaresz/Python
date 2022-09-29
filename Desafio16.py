"""Crie um programa que leia um número Real qualquer e
mostre na tela a sua porção inteira"""
from math import trunc
num = float(input('Digite um número: '))

print('O número real {} em sua parte inteira é {}'.format(num,trunc(num)))