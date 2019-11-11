class Pessoa(object):
    __nome:str
    __sexo:str
    __idade:int

    def __init__(self,nome,sexo,idade):
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = int(idade)

    def getNome(self):
        return self.__nome

    def getSexo(self):
        return self.__sexo

    def getIdade(self):
        return self.__idade


#lista de pessoas
pessoas = []

#abre o arquivo
arquivo = open("dados.txt", 'r');

#le as linhas do arquivo
for linha in arquivo:
    nome, sexo, idade = linha.split()
    pessoas.append(Pessoa(nome, sexo, idade))

#fecha o arquivo
arquivo.close();


totalHomens = 0
totalMulheres = 0
somaIdadeHomens = 0.0
somaidadeMulheres = 0.0

for p in pessoas:
    if(p.getSexo()=='m'):
        totalHomens += 1
        somaIdadeHomens += p.getIdade()
    else:
        totalMulheres += 1
        somaidadeMulheres += p.getIdade()


total = totalHomens + totalMulheres

mediaIdade = (somaIdadeHomens+somaidadeMulheres)/total

mediaIdadeHomens = somaIdadeHomens/totalHomens

mediIdadeMulheres = somaidadeMulheres/totalMulheres

print(total,totalHomens,totalMulheres,f'{mediaIdade:.2f}',f'{mediaIdadeHomens:.2f}',f'{mediIdadeMulheres:.2f}')