"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
o nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome"""

nome = str('Gabriel Soares Pereira').strip()

print('Seu nome em maíusculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))