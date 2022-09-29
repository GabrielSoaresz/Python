"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo."""
import math
angulo = int(input('Informe um ângulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo,sen,cos,tan))