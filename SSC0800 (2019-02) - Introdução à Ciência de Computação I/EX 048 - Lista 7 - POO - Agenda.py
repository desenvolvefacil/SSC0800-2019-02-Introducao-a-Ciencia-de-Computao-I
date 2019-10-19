#classe data
class Data(object):
    
    def getDia(self):
        return self.dia
    
    def setDia(self, dia):
        self.dia = dia

    def getMes(self):
        return self.mes
    
    def setMes(self, mes):
        self.mes = mes
    
    def getAno(self):
        return self.ano
    
    def setAno(self, ano):
        self.ano = ano

#classe Hora
class Hora(object):
    
    def getHora(self):
        return self.hora
    
    def setHora(self, hora):
        self.hora = hora

    def getMinuto(self):
        return self.minuto
    
    def setMinuto(self, minuto):
        self.minuto = minuto
    
    def getSegundo(self):
        return self.segundo
    
    def setSegundo(self, segundo):
        self.segundo = segundo

class Agenda(object):
    
    data = Data()
    hora = Hora()

    def getAtividade(self):
        return self.atividade
    
    def setAtividade(self, atividade):
        self.atividade = atividade

    def getHora(self):
        return self.hora

    def setHora(self,hora):
        self.hora = hora

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def __str__(self):
        return '{}/{}/{} - {}:{}:{}\n{}'.format(self.data.getDia(), self.data.getMes(), self.data.getAno(), self.hora.getHora(), self.hora.getMinuto(), self.hora.getSegundo(), self.atividade)

'''''''''
'''''''''

listaAgenda = []

n = int(input())

for i in range(n):

    ag = Agenda()

    ag.getData().setDia(input())
    ag.getData().setMes(input())
    ag.getData().setAno(input())
    
    ag.getHora().setHora(input())
    ag.getHora().setMinuto(input())
    ag.getHora().setSegundo(input())

    ag.setAtividade(input())

    print(ag)