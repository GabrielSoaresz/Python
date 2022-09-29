"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual o seu salário? '))

if salario > 1250.00:
    aumento = salario * 1.10
    print('Seu salário sofreu um aumento de 10% e foi de R${:.2f} para R${:.2f}'.format(salario,aumento))
else:
    aumento = salario * 1.15
    print('Seu salário sofreum um aumento de 15% e foi de R${:.2f} para R${:.2f}'.format(salario,aumento))