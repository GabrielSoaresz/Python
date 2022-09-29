"""Faça um algoritmo que leia o salario de um funcionario e
mostre seu novo salario, com 15% de aumento"""

salario = float(input("Digite o salário: "))

cal = salario * 0.15
aumento = salario + cal

print("O salário normal: R${:.2f}".format(salario))
print("Salário com 15% de aumento: R${:.2f}".format(aumento))
