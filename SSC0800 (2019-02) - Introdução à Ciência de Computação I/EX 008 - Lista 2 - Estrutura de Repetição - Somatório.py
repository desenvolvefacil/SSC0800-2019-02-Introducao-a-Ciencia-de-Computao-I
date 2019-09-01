'''
Lista 2 - Estrutura de Repetição - Somatório
Fazer um algoritmo para determinar e escrever o valor do seguinte somatório, em que o valor de X e a quantidade de parcelas devem ser fornecidos pelo usuário.

S= X - (X^2)/3! + (X^4)/5! - (X^6)/7! +....



Entrada: Um número real X e um número inteiro positivo N, respectivamente, o valor X e a quantidade de parcelas do somatório

Saída: O resultado do somatório.

Exemplos de Entrada e Saída

Entrada:

0.347 3

Saída:

0.327053

'''

'''
Função para calcular o fatorial
'''
def fatorial(x):
    #valor em float nao dar erro de estouro em valores muito grandes
    f=1.0
    for i in range(1,x+1):
        f=f*i
    return f


'''
Codigo Fonte
'''

#realiza a leitura
numero, repeticoes = input().split(" ")

#converte os valores para os tipos adequados
numero = float(numero)
repeticoes = int(repeticoes)

soma = numero

for i in range(1,repeticoes):
    # ((-1)**i) inverte o sinal de positivo para negativo
    soma += ((-1)**i) * ((numero**(2*i)) / fatorial(2*i+1))


print('%.6f' %soma)