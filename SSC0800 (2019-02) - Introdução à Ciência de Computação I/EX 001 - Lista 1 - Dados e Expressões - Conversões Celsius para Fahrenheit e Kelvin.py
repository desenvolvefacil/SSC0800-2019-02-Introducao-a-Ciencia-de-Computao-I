'''
Celsius para Farenheit e Kelvin
Desenvolva um algoritmo que leia um número, representando uma temperatura na escala Celsius, calcule e escreva.

(a) Seu correspondente em Farenheit: F = 9*C/5 + 32
(b) Seu correspondente em Kelvin: K = C + 273

Imprima com duas casas decimais!

Exemplos de Entrada e Saída

Entrada:

36

Saída:

96.80 F 
309.00 K
'''

# Entrando com o valor da temperatura em Celsius:
Celsius = float(input())

#converte em Farenheit
Farenheit = round((9 * Celsius / 5.0 + 32.0), 2)

#converte em Kelvin
Kelvin = round((Celsius + 273.0), 2)

#imprime os resultados
print(Farenheit, "F")
print(Kelvin, "K")