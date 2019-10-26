'''

#caso 1
###################################################
2
1
985
Gabriel Eduardo
Rua 9
900.50
50.20
130.4
2
895
Diane Giovanni
Avenida Principal
600.94
30
12.50
###################################################

#caso 2
###################################################
5
1
1022
OG Loc
Rua Perdizes
600.59
80.20
200.47
2
6
Cesar Vialpando
Avenida 704
600.94
512
1.50
1
59
Raider
Rua Logo Ali
1024.85
200.52
50.21
2
52
Big Smoke
Avenida 18 Alameda 6
200.94
950
2.3
1
1
Carl Lohnson
Rua dos Pombos
400.36
544.12
985.52
###################################################

#caso 3

###################################################
10
2
110
Mario
Terraco Sempre Vermelho
678.54
855
15.3
2
305
Luigi
Terraco Sempre Verde
600.95
950
14.71
1
952
Peach
Castelo Reino do Cogumelo
2024.51
205.50
301.54
1
852
Toad
Arredores do Castelo
985.54
640.93
785.59
1
051
Yoshi
Ilha dos Yoshis
750.34
512.01
1022.51
2
095
Rosalina
Lumas Galaxy
200.94
352
10.3
2
784
Daisy
Sarasaland
200.94
250
4.32
1
1065
Toadette
Arredores do Castelo
900.38
144.12
385.52
2
696
Mallow
Lagoa dos Girinos
504.54
984
1.94
1
666
Geno
Estrada Estelar
1025.31
250.17
1546.57
###################################################




Tipo: Clt
Endereco: {Rua}
Salario Base: {salario_base}
Transporte: {vale_transporte | vendas} 
Alimentacao: {vale_alimentacao | comissao}
Total Recebido: {total_recebido}


Tipo: Comissionado
Endereco: {Rua}
Salario Base: {salario_base}
Vendas no Mes: {vendas} 
Comissao: {comissao}
Total Recebido: {total_recebido}


'''

class Pessoa(object):
    __codigo:int
    __nome:str
    __endereco:str

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

class Funcionario(Pessoa):
    __salario_base:float

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    def get_total_recebido(self):
        pass

class Clt(Funcionario):
    __vale_transporte:float
    __vale_alimentacao:float

    def get_vale_transporte(self):
        return self.__vale_transporte

    def set_vale_transporte(self, vale_transporte):
        self.__vale_transporte = vale_transporte

    def get_vale_alimentacao(self):
        return self.__vale_alimentacao

    def set_vale_alimentacao(self, vale_alimentacao):
        self.__vale_alimentacao = vale_alimentacao

    def get_total_recebido(self):
        return self.get_salario_base() + self.__vale_alimentacao + self.__vale_transporte

    def __str__(self):
        retorno =  'Tipo: Clt'
        retorno +=  '\nNome: ' + self.get_nome()
        retorno +=  '\nEndereco: ' + self.get_endereco()
        retorno +=  '\nSalario Base: ' + str(self.get_salario_base())
        retorno +=  '\nTransporte: ' + str(self.get_vale_transporte())
        retorno +=  '\nAlimentacao: ' + str(self.get_vale_alimentacao())
        retorno +=  '\nTotal Recebido: ' + str(self.get_total_recebido()) +'\n'
        
        return retorno

class Comissionado(Funcionario):
    __vendas:int
    __comissao:float

    def get_vendas(self):
        return self.__vendas

    def set_vendas(self, vendas):
        self.__vendas = vendas
    
    def get_comissao(self):
        return self.__comissao

    def set_comissao(self, comissao):
        self.__comissao = comissao

    def get_total_recebido(self):
        return self.get_salario_base()   + self.__vendas * self.__comissao

    def __str__(self):
        retorno =  'Tipo: Comissionado'
        retorno +=  '\nNome: ' + self.get_nome()
        retorno +=  '\nEndereco: ' + self.get_endereco()
        retorno +=  '\nSalario Base: ' + str(self.get_salario_base())
        retorno +=  '\nVendas: ' + str(self.get_vendas())
        retorno +=  '\nComissao: ' + str(self.get_comissao())
        retorno +=  '\nTotal Recebido: ' + str(self.get_total_recebido()) +'\n'
        
        return retorno



n = int(input())

funcionarios = []

for i in range(n):
    
    tipo = int(input())



    if(tipo == 1):
        p = Clt()

        p.set_codigo(int(input()))
        p.set_nome(input())
        p.set_endereco(input())
        p.set_salario_base(float(input()))
        p.set_vale_transporte(float(input()))
        p.set_vale_alimentacao(float(input()))

        funcionarios.append(p)

    else:
        p = Comissionado()

        p.set_codigo(int(input()))
        p.set_nome(input())
        p.set_endereco(input())
        p.set_salario_base(float(input()))
        p.set_vendas(int(input()))
        p.set_comissao(float(input()))

        funcionarios.append(p)


#ordena a lista pelo codigo

#ordena a lista pelo codigo
funcionarios = sorted(funcionarios, key = Pessoa.get_codigo)


for p in  funcionarios:
    print(p)

