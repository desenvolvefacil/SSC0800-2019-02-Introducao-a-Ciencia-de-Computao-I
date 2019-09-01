'''
Lista 2 - Estrutura Condicional - Bissexto
Desenvolva um algoritmo que leia um ano qualquer e calcule se o mesmo é bissexto. Dicas:

Anos múltiplos de 4 são bissextos;
Porém, anos múltiplos de 100 não são bissextos;
Por fim, anos múltiplos de 400 são bissextos;
As últimas regras prevalecem sobre as primeiras.

Saídas possíveis

sim

nao

Exemplo de Entrada e Saída

Entrada:

2016

Saída:

sim
'''

#le o ano inteiro
ano = int(input())

#veriica se é bissexto
if (((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 400) == 0)):
    print('sim')
else:
    print('nao')