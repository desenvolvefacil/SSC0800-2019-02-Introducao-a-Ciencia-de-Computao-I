import pickle as pk

class Aluno (object):
    def __init__ (self, nome, idade, sexo, matricula):
        self.nome  = nome
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula

    def __str__ (self):
        return "Nome: "+self.nome+"\nIdade: "+self.idade+"\nSexo: "+self.sexo+"\nMatricula: "+self.matricula 

f = open("aaaa.bin","wb")

total = 8

pk.dump(total,f)

for i in range(total):
    a = Aluno("Aluno "+str(i),i,"m",i*9)

    pk.dump(a,f)

f.close()