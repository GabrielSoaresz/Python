"""Escreva um programa para aprovar um empréstimo bancário de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e, quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado"""

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos pretende pagar? '))

prestacao = casa / (anos * 12)
minimo = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa,anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')