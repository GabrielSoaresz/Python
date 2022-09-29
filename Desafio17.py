"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa"""
from math import pow, sqrt

co = int(input('Comprimento do cateto oposto: '))
ca = int(input('Comprimento do cateto adjacente: '))

h2 = pow(co, 2) + pow(ca, 2)
h = sqrt(h2)

print('O comprimento da hipotenusa é: {:.2f}'.format(h))


'''Método do professor: '''
from math import hypot
hi = hypot(co,ca) #---> calcula a hipotenusa automaticamente
print(hi)
