from statistics import mean 

class Uspiano(object):
    __nome:str
    __numeroUsp:str

    def getNome(self):
        return self.__nome;

    def getNumeroUsp(self):
        return self.__numeroUsp

    def setNome(self, nome):
        self.__nome = nome

    def setNumeroUsp(self, numeroUsp):
        self.__numeroUsp = numeroUsp



class Aluno(Uspiano):
    __curso:str
    __medias = []

    def setCurso(self,curso):
        self.__curso = curso

    def setMedias(self,medias):
        self.__medias = medias

    def getCoef(self):
        return mean(self.__medias)
        
    def __str__(self):
        ret = "Aluno\n"
        ret += "Nome: {}\n".format(self.getNome())
        ret += "NumUSP: {}\n".format(self.getNumeroUsp())

        #faz o truncamento dos dados
        aux = str(self.getCoef())
        aux = aux[:5]

        ret += "Coef.Rend: {}\n".format(aux)

        return ret

class Professor(Uspiano):
    __departarmento:str
    __area:str
    __cargaMedia = []

    def setDepartamento(self, departamento):
        self.__departarmento = departamento

    def setArea(self, area):
        self.__area = area

    def setCargaMedia(self,cargaMedia):
        self.__cargaMedia = cargaMedia

    def __str__(self):
        ret = "Professor\n"
        ret += "Nome: {}\n".format(self.getNome())
        ret += "NumUSP: {}\n".format(self.getNumeroUsp())
        ret += "Departamento: {}\n".format(self.__departarmento)
        ret += "Ultima Carga Horária: {}\n".format(self.__cargaMedia[-1])
        return ret



n = int(input())
uspianos = []

for i in range(n):
    tipo = int(input())

    if tipo ==1:
        p = Professor()

        p.setNome(input())
        p.setNumeroUsp(input())
        p.setDepartamento(input())
        p.setArea(input())

        input() #não sei o objetivo deste dado
        
        p.setCargaMedia(list(map(float,input().split())))

        uspianos.append(p)

    else:
        a = Aluno()

        a.setNome(input())
        a.setNumeroUsp(input())

        a.setCurso(input())

        input() #não sei o objetivo deste dado

        a.setMedias(list(map(float,input().split())))

        uspianos.append(a)

for p in uspianos:
    if(p == uspianos[-1]):
        print(p, end="")
    else:
        print(p)