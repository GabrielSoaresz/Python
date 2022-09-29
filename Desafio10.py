"""Crie um programa que mostre quantos reais uma pessoa tem na carteira
e quantos dólares ela pode comprar
Considere US$1,00=R$3,27
"""

real = float(input("Valor na carteira: R$"))
dolar = real / 3.27

print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
