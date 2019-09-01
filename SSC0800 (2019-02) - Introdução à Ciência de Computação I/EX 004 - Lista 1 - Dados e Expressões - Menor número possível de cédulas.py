'''
Combinando o menor número possível de cédulas
Escreva um programa que lê um valor em dinheiro e calcula qual o menor número possível de cédulas de 100.00, 50.00, 10.00, 5.00 e 1.00 em que o valor lido pode ser decomposto. O programa deve retornar o valor lido e a relação de notas necessárias.

Exemplos de Entrada e Saída

Entrada:

661

Saída:

6 de R$100,00
1 de R$50,00
1 de R$10,00
0 de R$5,00
1 de R$1,00
'''

valor = int(input())

notas100, resto = divmod(valor,100)

notas50 , resto = divmod(resto,50)

notas10 , resto = divmod(resto,10)

notas5 , resto = divmod(resto,5)

print(notas100 ,"de R$100,00")
print(notas50 ,"de R$50,00")
print(notas10 ,"de R$10,00")
print(notas5 ,"de R$5,00")
print(resto ,"de R$1,00")