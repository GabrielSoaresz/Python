"""Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e raiz quadrada"""
import math

n1 = int(input('Digite um número: '))

d = n1*2
t = n1*3
r = n1 ** (1/2) # Ou math.sqrt(n1)  Ou pow(n1,(1/2))

print('O dobro do número é: {};\nO triplo do número é: {}; \nA raiz quadrada do número é: {:.2f}'.format(d,t,r))