
class Aluno (object):
    def __init__ (self, nome, idade, sexo, matricula):
        self.nome  = nome
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula

    def __str__ (self):
        return "Nome: "+self.nome+"\nIdade: "+self.idade+"\nSexo: "+self.sexo+"\nMatricula: "+self.matricula 

#abre o arquivo
arquivo = open("dados-alunos.bin", 'rb');




n = arquivo.read(4)

n = int.from_bytes(n, "little")

for i in range(n):
    
    nome = arquivo.read(16)

    idade = arquivo.read(28)
    idade = int.from_bytes(idade, "little")

    sexo = arquivo.read(1)

    aux = arquivo.read(7)
    aux = int.from_bytes(aux, "little")

    print(nome.decode("utf-8"), idade , sexo.decode("utf-8"), aux)

    #print(aux)

    #break
#fecha o arquivo
arquivo.close();
