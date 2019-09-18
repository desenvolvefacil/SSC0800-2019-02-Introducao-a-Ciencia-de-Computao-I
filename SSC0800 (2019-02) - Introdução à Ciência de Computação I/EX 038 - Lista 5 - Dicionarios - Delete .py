'''
Joao,Marta,Lis,Hugo,Simoes,Paula,Viviane,Otto,Carlos,Raimundo
169865,4545462,8453,564544,844555,544546,9867,54558,5459,86101
Joao,Simoes,Paula,Carlos,Otto
'''

indexs = list(map(str,input().replace("\r","").split(",")))
valores = list(map(int,input().split(",")))
nomes = list(map(str,input().replace("\r","").split(",")))

dic = {}

for i in range(len(indexs)):
    dic[indexs[i]]=valores[i]

for nome in nomes:
    del dic[nome]

print(dic)