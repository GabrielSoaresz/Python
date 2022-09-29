"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    print('Você excedeu o limite de velocidade de 80km/h')
    multa = (vel - 80) * 7
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com cuidado.')