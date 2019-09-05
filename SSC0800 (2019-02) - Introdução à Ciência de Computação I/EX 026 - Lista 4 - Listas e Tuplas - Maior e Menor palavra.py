'''
Desenvolva um algoritmo que leia uma frase e encontre a maior e a menor palavra nessa frase. Imprima as palavras encontradas. Se houver mais de uma palavra com o menor ou maior tamanho, imprimir a primeira que aparece na frase.

Entrada: Uma frase

Saida: Duas linhas, a menor e a maior palavra, respectivamente

Exemplos de Entrada e Saída
Entrada:

Eu adoro ICC1 por isso programo muito para treinar
Saída:

Eu 
programo

Entrada:

Palavras maiores palavras menores devem imprimir todas
Saída:

devem
Palavras 
'''

#realiza a leitura
frase = input().split(" ")

#cria as variaveis maior e menor inicialmente com a primeira palavra
maior = frase[0]
menor = frase[0]

#para cada palavra na frase
for palavra in frase:
    #se o tamanho é maior
    if len(palavra) > len(maior):
        maior = palavra
    #se o tamanho é menor
    if len(palavra)<len(menor):
        menor = palavra

print(menor)
print(maior)