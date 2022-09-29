"""Crie um prograsma que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas."""

km = int(input('Qual a distância da viagem? '))
passagem = 0
if km <= 200:
    passagem = km * 0.50
    print('A distância é de {}Km e o valor da passagem é de R${:.2f}'.format(km,passagem))
else:
    passagem = km * 0.45
    print('A distância é de {}Km e o valor da passagem é de {:.2f}'.format(km, passagem))
