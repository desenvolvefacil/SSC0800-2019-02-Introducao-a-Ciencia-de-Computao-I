import pickle as pk

class Bebe(object):
    __dataNascimento:str
    __sexo:str
    __altura:float
    __peso:float
    __nome:str

    def __init__(self,dataNascimento,sexo,altura,peso,nome):
        self.__dataNascimento = dataNascimento
        self.__sexo = sexo
        self.__altura = float(altura)
        self.__peso = float(peso)
        self.__nome = nome

    def getSexo(self):
        return self.__sexo

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

'''
f = open("dados-bebes.bin","wb")

#registro 1
pk.dump('28-10-2016',f)
pk.dump('f',f)
pk.dump(0.80,f)
pk.dump(3.91,f)
pk.dump('Fernanda Lima',f)

#registro 2
pk.dump('27-06-2017',f)
pk.dump('m',f)
pk.dump(0.76,f)
pk.dump(3.11,f)
pk.dump('Joao Ferreira',f)

#registro 3
pk.dump('28-01-2015',f)
pk.dump('m',f)
pk.dump(0.63,f)
pk.dump(2.96,f)
pk.dump('Fernando Sales',f)

#registro 4
pk.dump('13-12-2016',f)
pk.dump('m',f)
pk.dump(0.85,f)
pk.dump(3.71,f)
pk.dump('Luis Ferro',f)

#registro 5
pk.dump('15-04-2018',f)
pk.dump('m',f)
pk.dump(0.48,f)
pk.dump(2.44,f)
pk.dump('Luan Ferreira',f)

#registro 6
pk.dump('28-10-2016',f)
pk.dump('m',f)
pk.dump(0.90,f)
pk.dump(3.71,f)
pk.dump('Juliano Cunha',f)


f.close()
'''

lista = []


#abre o arquivo texto
f = open("dados-bebes.txt","r")


#le o arquivo texto

for linha in f:

    dataNascimento,sexo,altura,peso,nome = linha.split("|")

    lista.append(Bebe(dataNascimento,sexo,altura,peso,nome))

f.close()


#abre o arquivo binario
f = open("dados-bebes.bin","rb")

#le o arquivo binario
for i in range(6):
    lista.append(Bebe(pk.load(f),pk.load(f),pk.load(f),pk.load(f),pk.load(f)))

f.close()


totalHomens = 0
totalMulheres = 0

mediaPesoHomens = 0.0
mediaPesoMulheres = 0.0

mediaAlturaHomens = 0.0
mediaAlturaMulheres = 0.0

for o in lista:
    if o.getSexo() == 'f':
        totalMulheres += 1
        mediaPesoMulheres += o.getPeso()
        mediaAlturaMulheres += o.getAltura()
    else:
        totalHomens += 1
        mediaPesoHomens += o.getPeso()
        mediaAlturaHomens += o.getAltura()

mediaPesoHomens /= totalHomens
mediaPesoMulheres /= totalMulheres

mediaAlturaHomens /= totalHomens
mediaAlturaMulheres /= totalMulheres

print("Dados dos Bebes Homens:");
print("Total:", totalHomens);
print("Media do Peso:", f'{mediaPesoHomens:.2f}');
print("Media da Altura:", f'{mediaAlturaHomens:.2f}');
print()
print("Dados dos Bebes Mulheres:");
print("Total:", totalMulheres);
print("Media do Peso:", f'{mediaPesoMulheres:.2f}');
print("Media da Altura:", f'{mediaAlturaMulheres:.2f}');
