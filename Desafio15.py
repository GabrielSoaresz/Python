"""Escreva um programa que leia a quantidade de Km percorrido por um carro alugado e
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 por km rodado"""

km = float(input('Km rodado: '))
dias = int(input('Dias alugado: '))

valor = (60 * dias) + (km * 0.15)

print('O carro foi alugado por {1} dia(s) e percorreu {0}Km'.format(km,dias))
print('O valor a pagar será de {:.2f}'.format(valor))