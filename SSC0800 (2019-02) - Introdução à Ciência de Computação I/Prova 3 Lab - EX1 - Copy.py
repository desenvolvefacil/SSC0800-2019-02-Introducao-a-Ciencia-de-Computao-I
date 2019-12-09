import pickle as pk
from statistics import mean

#classe alunos
class Aluno(object):
    #atributos da classe

    #matricula inteiro
    __matricula:int
    #nome string
    __nome:str
    #idade do aluno inteiro
    __idade:int
    #sexo do aluno char 'f' ou 'm'
    __sexo:str
    #notas vetor com 5 notas
    __notas:[]

    #construtor da classe
    def __init__(self, matricula, nome, idade, sexo, notas):
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__notas = notas

    #pega o número da matricula
    def get_matricula(self):
        return self.__matricula

    #pega o nome do aluno
    def get_nome(self):
        return self.__nome

    '''
    retorna a média das notas
    '''
    def get_media(self):
        #façam a mágica acontecer aqui
        return mean(self.__notas)

'''
#Gerar Arquivo Binario de Registros

f = open("alunos.bin","wb")

a = Aluno(101,'Luana Maria',30,'m',[5,7,8,5,3])
pk.dump(a,f)

a = Aluno(102,'Mariana Reis',31,'f',[3,10,3,10,3])
pk.dump(a,f)

a = Aluno(103,'Rafaela Toti',20,'f',[4,6,10,0,1])
pk.dump(a,f)

a = Aluno(104,'Cludio Lopez',25,'m',[8,5,7,6,6])
pk.dump(a,f)

a = Aluno(105,'Ricardo Borsato',26,'m',[1,2,3,1,2])
pk.dump(a,f)

f.close()
'''


#realiza a leitua dos alunos
f = open("alunos.bin","rb")

lista_alunos = []
lista_matriculas = []

for i in range(5):
        lista_alunos.append(pk.load(f))

f.close()

#realiza a leitura dos codigos
f = open("alunos.txt","r")

for matricula in f:
    lista_matriculas.append(int(matricula))

f.close()

for matricula in lista_matriculas:
    #busca na lista de alunos
    for aluno in lista_alunos:
        if aluno.get_matricula() == matricula:
            print(aluno.get_nome())

            if(aluno.get_media() >= 5.0):
                print("Aprovado", f'{aluno.get_media():.1f}')
            else:
                print("Reprovado", f'{aluno.get_media():.1f}')
            print()

