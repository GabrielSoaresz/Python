"""Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto"""

produto = float(input("Valor do produto: R$"))

"""Para calcular porcentagem de desconto basta pegar 
o valor sem desconto e multiplicar pela porcentagem dividido por 100.
Depois pegar o valor sem desconto e subtrair pelo resultado anterior"""
cal = (produto * 5) / 100  # Ou produto * 0.05
desconto = produto - cal

print('Valor do produto: ', produto)
print('Valor com desconto: ', desconto)
print('Valor descontado: ',cal)