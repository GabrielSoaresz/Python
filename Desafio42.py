"""Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
Equilátero: todos os lados iguais
Isóceles: dois lados iguais
Escaleno: todos os lados diferentes"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('Triângulo equilátero!')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
        print('Triângulo Isóceles!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Triângulo Escaleno!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
