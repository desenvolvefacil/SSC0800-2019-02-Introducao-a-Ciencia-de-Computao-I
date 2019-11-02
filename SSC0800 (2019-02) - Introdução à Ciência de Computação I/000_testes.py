class Pessoa(object):
    def __init__(self,c,n,e):
        self.__codigo = c
        self.__nome = n
        self.__endereco = e
    
    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco
    
    def setCod(self,c):
        self.__codigo = c
    
    def setNome(self,n):
        self.__nome = n
    
    def setEndereco(self,e):
        self.__endereco = e

class Funcionario(Pessoa):
    def __init__(self,c,n,e,s):
        Pessoa.__init__(self,c,n,e)
        self.__salario_base = s
    
    def getSalBase(self):
        return self.__salario_base

    def setSalBase(self,s):
        self.__salario_base = s

    def get_total_recebido(self):
        return self.__salario_base + self.__transporte + self.__alimentacao

class Clt(Funcionario):
    def __init__(self,c,n,e,s,t,a):
        Funcionario.__init__(self,c,n,e,s)
        self.__transporte = t
        self.__alimentacao = a
    
    def get_total_recebido(self):
        return self.getSalBase + self.getValeTransporte + self.getValeAlimentacao
        
    def getValeTransporte(self):
        return self.__transporte
    
    def getValeAlimentacao(self):
        return self.__alimentacao
    
    def setValeTransporte(self, t):
        self.__transporte = t
    
    def setValeAlimentacao(self, a):
        self.__alimentacao = a

    def __str__(self):
        return 'Tipo: Clt\nNome: '+str(self.getNome())+'\nEndereco: '+str(self.getEndereco())+'\nSalario Base: '+\
        str(self.getSalBase())+'\nTransporte: '+str(self.getValeTransporte())+'\nAlimentacao: '+str(self.getValeAlimentacao())+\
        '\nTotal Recebido: '+str(float(self.getSalBase())+float(self.getValeTransporte())+float(self.getValeAlimentacao()))+'\n'


class Comissionado(Funcionario):
    def __init__(self,c,n,e,s,v,co):
        Funcionario.__init__(self,c,n,e,s)
        self.__vendas = v
        self.__comissao = co
    
    def get_total_recebido(self):
        return self.getSalBase + self.getVendas + self.getComissao
        
    def getVendas(self):
        return self.__vendas
    
    def getComissao(self):
        return self.__comissao
    
    def setVendas(self, v):
        self.__Vendas = v
    
    def setComissao(self, c):
        self.__comissao = c

    def __str__(self):
        return 'Tipo: Comissionado\nNome: '+str(self.getNome())+'\nEndereco: '+str(self.getEndereco())+'\nSalario Base: '+str(self.getSalBase())+\
        '\nVendas: '+str(self.getVendas())+'\nComissao: '+str(self.getComissao())+'\nTotal Recebido: '+\
        str(float(self.getSalBase())+int(self.getVendas())*float(self.getComissao()))+'\n'

'''
def pegaCod(lista):
    return lista[0]
'''

ls_fun = []

n = int(input())

for i in range(n):
    
    tipo = input()
    
    if tipo == "1":
        cod = int(input())
        nome = input()
        end = input()
        sal = float(input())
        trans = float(input())
        alim = float(input())
        tip = 1
        ls_fun.append([cod,nome,end,sal,trans,alim,tip])
        
    if tipo == "2":
        cod = int(input())
        nome = input()
        end = input()
        sal = float(input())
        ven = int(input())
        com = float(input())
        tip = 2
        ls_fun.append([cod,nome,end,sal,ven,com,tip])
    
ls_fun.sort(key = Pessoa.getCodigo)

for funcionario in ls_fun:
    if funcionario[6] == 1:
        print(Clt(funcionario[0],funcionario[1],funcionario[2],funcionario[3],funcionario[4],funcionario[5]))
        #c,n,e,s,t,a
    else:
        print(Comissionado(funcionario[0],funcionario[1],funcionario[2],funcionario[3],funcionario[4],funcionario[5]))
        #c,n,e,s,v,co
    