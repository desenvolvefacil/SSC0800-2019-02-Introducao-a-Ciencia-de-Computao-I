import math
#ENTRADAS
num_palavras = int(input())
palavras = []
for i in range(num_palavras):

    cada_palavra = input()
    cada_palavra = cada_palavra.replace("\r","")
    cada_palavra = cada_palavra.replace("\n","")

    palavras.append(cada_palavra)

#TAMANHO DE CADA PALAVRA
    for j in palavras:
        cada_palavra = list(j)
        
        tamanho = len(cada_palavra)
        d = {}
        for letra in cada_palavra:
            if letra in d :
                d[letra] += 1
            else:
                d[letra] = 1
    divisor = 1
    for n in d.values() :
        divisor *= math.factorial(n)
    resposta = int(math.factorial(tamanho)/divisor)
    print(resposta)
        