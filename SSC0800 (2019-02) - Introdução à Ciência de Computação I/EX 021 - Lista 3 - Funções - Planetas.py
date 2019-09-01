'''
Lista 3 - Funções - Ângulos do Triângulo
Desenvolva um programa onde o usuário fornece as medidas dos três ângulos de um triângulo e o tipo de triângulo (agudo, obtuso ou retângulo) é escrito na tela. Lembre-se, você deve verificar também o critério de formação de triângulo, onde a soma dos ângulos internos de um triângulo deve ser 180 graus. Logo, o programa deve ter duas funções: uma função angulotriangulo() que recebe os ângulos e imprime o tipo de triângulo e uma função Ehtriangulo() que recebe os ângulos e retorna 1 se for triangulo e 0, caso contrário.

Dica: Use os seguintes formatadores de print:

print("Triangulo retangulo")
print("Triangulo obtuso")
print("Triangulo agudo")
print ("Valores nao formam um triangulo")
Exemplo de Entrada e Saída
Entrada:

90
45
45

Saída:

Triangulo retangulo

'''

'''
Função que recebe o a entrada em segundos e o planeta que sera calculado o tempo
'''
def CalculaTempo(entrada,planeta):
    
    #total de segundos em um dia na terra
    diaTerra = 24 * 60 * 60
    
    #variaveis de retorno
    dia=0
    horas=0
    minutos=0
    segundos=0
    
	#Calcula o tempo para o Planeta Terra
    if(planeta=="Terra"):
        dia , resto = divmod(entrada,diaTerra)
        horas, resto = divmod(resto,3600)
        minutos, segundos = divmod(resto,60)
        
    #Calcula o tempo para o Planeta Mercurio
    elif(planeta=="Mercurio"):

        diaMercurio = 58 * diaTerra + 16 * 3600
        dia , resto = divmod(entrada ,diaMercurio)
        horas, resto = divmod(resto,3600)
        minutos, segundos = divmod(resto,60)

    #Calcula o tempo para o Planeta Jupiter
    elif(planeta=="Jupiter"):
        diaJupiter = 9*3600+ 56*60
        dia , resto = divmod(entrada ,diaJupiter)
        horas, resto = divmod(resto,3600)
        minutos, segundos = divmod(resto,60)
    
	#Calcula o tempo para o Planeta Vênus
    else:
        diaVenus = diaTerra * 243
        dia , resto = divmod(entrada ,diaVenus)
        horas, resto = divmod(resto,3600)
        minutos, segundos = divmod(resto,60)

	#Retorna os valores calculados
    return [dia,horas,minutos,segundos]
    
'''
Codigo Fonte
'''

#Lê as entradas
entrada,planeta = input().split(" ")

#converte a entrada para inteiro
entrada = int(entrada)

#chama a função e retorna os valores em suas respectivas variáveis
dia,horas,minutos,segundos = CalculaTempo(entrada,planeta)

#Mostra o Resultado em tela
print(f'{entrada} segundos no planeta {planeta} equivalem a:')
print(f'{dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos')

