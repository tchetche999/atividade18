# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
numero = int(input("insira um número:"))
numero2 = int(input("insira o segundo número:"))
if numero > numero2:
    print(f"o maio número é {numero}:")
else:
    print(f"o maior número é {numero2}:")