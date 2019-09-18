'''
Joao,Maria,Ana
123,654,897
Pedro,Natalia,Fernanda
456,321,654
'''

indexs1 = list(map(str,input().replace("\r","").split(",")))
valores1 = list(map(int,input().split(",")))
indexs2 = list(map(str,input().replace("\r","").split(",")))
valores2 = list(map(int,input().split(",")))

dic1 = {}
dic2 = {}

for i in range(len(indexs1)):
    dic1[indexs1[i]]=valores1[i]
    dic2[indexs2[i]]=valores2[i]

print("Agenda 1")
print(dic1)

print("Agenda 2")
print(dic2)

print("Agenda Mesclada")
dic2.update(dic1)
print(dic2)