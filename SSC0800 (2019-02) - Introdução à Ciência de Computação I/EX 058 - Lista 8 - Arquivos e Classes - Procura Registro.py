import pickle as pk

class Aluno (object):
    def __init__ (self, nome, idade, sexo, matricula):
        self.nome  = nome
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula

    def __str__ (self):
        return "Nome: "+self.nome+"\nIdade: "+str(self.idade)+"\nSexo: "+self.sexo+"\nMatricula: "+str(self.matricula)


#abre o arquivo
f = open("dados-alunos.bin","rb")

#le o total de registros
total = pk.load(f)

#le o codivo digitado
cod = int(input())

#busca o codigo no arquivo
for i in range(total):
    o = pk.load(f)
    if o.matricula == cod:
        print(o)
        break

f.close()
