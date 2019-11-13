import pickle as pk

class Funcionario (object):
    def __init__(self, nome, idade, sexo, salario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario


f = open("dados-funcionario.bin","rb")

total = pk.load(f)


totalHomens = 0
totalMulheres = 0
somaSalarioHomens = 0.0
somaSalarioMulheres = 0.0

for i in range(total):
    p = pk.load(f)
    
    if(p.sexo == 'm'):
        totalHomens += 1
        somaSalarioHomens += p.salario
    else:
        totalMulheres += 1
        somaSalarioMulheres += p.salario

f.close()


mediaSalario = (somaSalarioHomens+somaSalarioMulheres)/total

mediaSalarioHomens = somaSalarioHomens/totalHomens

mediSalarioMulheres = somaSalarioMulheres/totalMulheres

print(total,totalHomens,totalMulheres,f'{mediaSalario:.2f}',f'{mediaSalarioHomens:.2f}',f'{mediSalarioMulheres:.2f}')
