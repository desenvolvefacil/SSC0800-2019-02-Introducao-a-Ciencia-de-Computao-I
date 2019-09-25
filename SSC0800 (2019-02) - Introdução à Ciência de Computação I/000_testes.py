def fat(num):
    if num == 0:
        f = 1
    else:
        f = 1
        for i in range(1, num + 1):
            f = f * i
    return f

x = int(input())


entrada = []

for i in range(x):

    palavra = input()
    palavra = palavra.replace("\n","")
    palavra = palavra.replace("\r","")

    entrada.append(palavra)



for t in entrada:
    alfabeto = "qwertyuiopasdfghjklzxcvbnm"
    denominador = 1
    for w in alfabeto:
        denominador = denominador * fat(t.count(w))
    anagrama = int(fat(len(t)) / denominador)
    print(anagrama)