"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e último nome separadamente"""

nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print('Seu nome completo:',nome)
print('Seu primeiro nome é {} e o seu último nome é {}'.format(dividido[0],dividido[len(dividido)-1]))