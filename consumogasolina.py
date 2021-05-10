# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Efetuar o calculo da quantidade de litros de combustivel gastos em uma viagem,
# sabendo-se que o carro faz 12 km/L. Deverão ser fornecidos o tempo gasto na
# viagem e a velocidade média.
#
# Utilize as seguintes formulas:
#
#   distancia = velocidade*tempo
#   litros usados = distancia/12   
#
# O algoritmo deverá apresentar os valores  da velocidade média, tempo gasto na
# viagem, distancia percorrida e quantidade de litros usados na viagem.

tempo = float(input("Entre com o tempo total da viajem = "))
vel = float(input("Qual a velocidade media "))

dist = vel*tempo
consumo = dist/12
print("Tempo gasto: %.1f h" %tempo)
print("Velocidade media: %.2f Km/h" %vel)
print("Distancia percorrida: %.1f Km" %dist)
print("Consumo: %.2f L" %consumo)
