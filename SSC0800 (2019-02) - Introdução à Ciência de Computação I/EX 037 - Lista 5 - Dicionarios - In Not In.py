'''
Joao,Marta,Lis,Hugo,Simoes,Paula,Viviane,Otto,Carlos,Raimundo
165,4562,8453,564,8455,5446,9867,558,5459,86101
Joao,Fernando,Paloma,Marta,Mariana
'''

indexs = list(map(str,input().split(",")))
valores = list(map(int,input().split(",")))
nomes = list(map(str,input().split(",")))

dic = {}

for i in range(len(indexs)):
    dic[indexs[i]]=valores[i]

for nome in nomes:
    print(dic.get(nome,"Nao Cadastrado"))
