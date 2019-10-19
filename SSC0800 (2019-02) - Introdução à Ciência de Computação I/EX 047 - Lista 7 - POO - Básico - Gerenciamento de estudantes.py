class Aluno(object):

    #set's
    def setNumUsp(self, numUSP):
        self.numUSP = numUSP

    def setNome(self, nome):
        self.nome = nome

    def setCurso(self, curso):
        self.curso = curso

    def setIdade(self, idade):
        self.idade = idade

    #get's
    def getNumUsp(self):
        return self.numUSP

    def getNome(self):
        return self.nome 

    def getCurso(self):
        return self.curso

    def getIdade(self):
        return idade

    #sobrescrita do metodo str
    def __str__(self):
        return 'Nome: ' + self.nome + '\n' + 'Curso: ' + self.curso + '\n' + 'N USP: ' + str(self.numUSP) + '\n' + 'IDADE: ' + str(self.idade) + '\n'
    
'''
Inicio do Main
'''

#vetor de alunos
alunos = []

numUsp = int(input())

#popular alunos
while(numUsp != -1):
    #cria um novo objeto aluno
    
    al = Aluno()
    al.setNumUsp(numUsp)

    al.setNome(input())

    al.setCurso(input())
    al.setIdade(int(input()))

    #adiciona o aluno a lista
    alunos.append(al)

    #le novamente
    numUsp = int(input())

#chamar menu principal
opc = int(input())

while(opc!=-1):
    #busco por numero usp
    if(opc==1):
        #numero usp a ser procurado
        numUsp = int(input())

        #procura o aluno na lista
        for al in alunos:
            if(al.getNumUsp()==numUsp):
                print(al)
                break

    #busca por curso
    elif(opc==2):
        cur = input()

        #procura o aluno na lista
        for al in alunos:
            if(al.getCurso()==cur):
                print(al)
    
    #imprimir tudo
    else:
        for al in alunos:
            print(al)

    #le novamente a opcao
    opc = int(input())
