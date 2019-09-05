'''
Desenvolva um algoritmo que leia uma sentença e determine se a mesma é ou não é de um palíndromo. Palíndromo: palavras, frases, ou números que preservam seu valor independentemente de serem lidos da esquerda para direita ou da direita para a esquerda. Exemplos: ARARA, AMOR A ROMA, 12321 são palíndromos.

Obs: aqui, não diferenciamos caracteres maiúsculos e minúsculos; 'A' e 'a' são considerados o mesmo caractere.

Entrada: Uma string. A sentença para ser analisada.

Saida: O seu programa deve imprimir "SIM" (sem aspas) se a sentença for um palíndromo e "NAO" caso contrário.

Exemplos de Entrada e Saída

Entrada:

A grama e amarg a

Saída:

SIM

Entrada:

Sorvete no bandejao

Saída:

NAO

'''

#realiza a leitura
#elimina o \r, espacos em branco e tranforma tudo em maiusculas para poder
#comparar
frase = input().replace("\r","").replace(" ","").upper()

ehpalindromo = True

#pega o tamanho da frase (qtd de letras)
tamanho = len(frase)

#le até a metade e compara com seu espelho
for i in range(tamanho // 2):
    if frase[i] != frase[tamanho - i - 1]:
        ehpalindromo = False
        break

#imprime com if ternario
print(ehpalindromo == True and "SIM" or "NAO")