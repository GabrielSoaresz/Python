#Mostre todos os tipos primitivos de uma variavel.
var = input("Digite algo: ")
print('Só tem espaços? ',var.isspace())
print('É um número? ',var.isnumeric())
print('É alfabético? ',var.isalpha())
print('É um alfanumérico? ',var.isalnum())
print('Está em maiúsculas? ',var.isupper())
print('Está em minúsculas? ',var.islower())
print('Está capitalizada? ',var.istitle())
