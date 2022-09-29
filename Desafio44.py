"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format('LOJAS XERÉU'))

valor = float(input('Valor do produto: R$'))
print("""Selecione a forma de pagamento:
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros""")

opcao = int(input('Opção escolhida: '))

if opcao == 1:
    valorfinal = valor - valor * 0.10
    print('Opção 1: À vista dinheiro/cheque com 10% de desconto')
    print('O valor do produto é R${:.2f} e o valor a pagar será R${:.2f}'.format(valor, valorfinal))
elif opcao == 2:
    valorfinal = valor - valor * (5/100)
    print('Opção 2: À vista no cartão com 5% de desconto')
    print('O valor do produto é R${:.2f} e o valor a pagar será R${:.2f}'.format(valor, valorfinal))
elif opcao == 3:
    valorfinal = valor
    parcela = valorfinal / 2
    print('Opção 3: Até 2x no cartão: preço normal')
    print('O valor do produto é R${:.2f} e o valor a pagar será 2x de R${:.2f} sem juros.'.format(valorfinal, parcela))
elif opcao == 4:
    valorfinal = valor + (valor * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = valorfinal / totalparc
    print('Opção 4: 3x ou mais no cartão com 20% de juros')
    print('O valor do produto é R${:.2f} e o valor a pagar será {}x de R${:.2f} com juros'.format(valor,totalparc,parcela))
    print('O valor total será de R${:.2f} no final.'.format(valorfinal))
else:
    print('\033[1;31;40mOpção inválida!\033[m')
