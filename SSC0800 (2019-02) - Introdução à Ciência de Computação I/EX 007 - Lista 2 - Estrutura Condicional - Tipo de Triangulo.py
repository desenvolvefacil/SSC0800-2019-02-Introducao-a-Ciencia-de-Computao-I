'''
Lista 2 - Estrutura Condicional - Tipo de Triangulo
Escreva um programa que recebe 3 lados de um triangulo e retorna se o triangulo é isósceles (dois lados iguais), escaleno (todos os lados diferentes) ou equilátero (todos os lados iguais).

Entrada: Três números reais

Saida: Uma mensagem de "isosceles", "escaleno" ou "equilatero".

Exemplos de Entrada e Saída

Entrada:

10 10 10
Saída:

equilatero

Entrada:

10 20 10

Saída:

isosceles

Entrada:

3.5 4.5 5.5

Saída:

escaleno

'''

lado1, lado2, lado3 = input().split(" ")


if ((lado1 == lado2) and (lado2 == lado3)):
    print('equilatero')
elif ((lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3)):
    print('escaleno')
else:
    print('isosceles')