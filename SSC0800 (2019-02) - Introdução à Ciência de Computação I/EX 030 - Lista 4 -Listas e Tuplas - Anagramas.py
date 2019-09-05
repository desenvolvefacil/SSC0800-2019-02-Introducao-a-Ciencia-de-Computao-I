#https://mundoeducacao.bol.uol.com.br/matematica/anagrama.htm
'''
Dadas N strings, determinar quantos anagramas existem para cada uma.
Entrada: Um inteiro positivo N;
em seguida, N linhas, cada uma contendo uma string de carácteres alfabéticos minúsculos,
seguidas de uma quebra de linha (‘\n’) 
Saída: N linhas, cada uma contendo um inteiro que representa a quantidade de anagramas;
a i-ésima linha impressa é a resposta para a i-ésima string inserida, com i de 1 até n.

(numero de letras)! / (numero Repetições)! * (numero Repetições)!.....
'''

def fatorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

#le a qtd de palavras
n = int(input())

#realiza a leitura de cada palvra
for i in range(n):
    palavra = input()

    #remove os caracteres que \n e \r que vem na leitura do arquivo
    palavra = palavra.replace("\n","")
    palavra = palavra.replace("\r","")

    #cria o vetor para pegar as repetições
    repeticoes = {}

    for letra in palavra:
        
        #se a letra já é repetida, soma 1
        if letra in repeticoes:
            #pega o valor atual
            #total = repeticoes.get(palavra[j])
            #atualiza com +1
            repeticoes[letra] += 1
        else:
            #se não esta, adiciona
            repeticoes[letra] = 1
        

    #agora que sabemos o total de repeticoes vamos aplicar a formula
    '''
    (numero de letras)! / (numero Repetições)! * (numero Repetições)!.....
    '''
    ncaracteres = fatorial(len(palavra))

    divisor = 1
    #vamos pegar o valor, gerar seu fatorial e multiplcar
    for valor in repeticoes.values():
        divisor *= fatorial(valor)

    print(ncaracteres//divisor)
    #print(repeticoes)