import numpy as np

'''
[1,2],[3,2]
[2,3],[4,5]
'''

#Realiza a leitura da matriz como string
m1 = input()
m2 = input()

#transforma a string em matriz de valores
m1 = eval(m1.split()[0])
m2 = eval(m2.split()[0])

#tranforma em numpy array
m1 = np.array(m1)
m2 = np.array(m2)

print("M1 + M2")
print(m1 + m2)

print("M1 - M2")
print(m1 - m2)

print("M1 * M2")
print(m1 * m2)

print("M1 / M2")
print(m1 / m2)

print("M1 ** 2")
print(m1**2)

print("Raiz M2")
print(np.sqrt(m2))