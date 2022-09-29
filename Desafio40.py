"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo co a média atingida:
Média abaixo de 5.0: Reprovado
Média entre 5.0 e 6.9: Recuperação
Média 7.0 ou superior: Aprovado"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2

if media < 5.0:
    print('Sua média foi {:.1f}. \033[1;31;40mAluno reprovado.\033[m'.format(media))
elif 7 > media >= 5:
    print('Sua média foi {:.1f}. \033[1;33;40mAluno em recuperação.\033[m'.format(media))
else:
    print('Sua média foi {:.1f}. \033[1;32;40mAluno aprovado!\033[m'.format(media))