"""Escreva um programa que converta uma temperatura ºC para ºF"""

C = float(input('Digite uma temperatura em ºC: '))
F = (C * 9/5) + 32

print('A temperatura de {}ºC corresponde a {}ºF.'.format(C,F))