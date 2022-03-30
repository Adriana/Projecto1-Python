'''
Script referente a PARTE I do enunciado do Projevto 1 - UFCD
O script seve ser invocado na linha na linha de comandos da seguinte forma
$python 3 efeitos.py -i 0.5 2 [PALAVRA]

Projecto realizado por:
Adriana de Souza Gama
Carlo Braga
'''

#Libraries a importar
import time
import sys
import os

#Primeiro o programa recebe os argumentos da linha de comandos para depois ser juntado numa única variavel string
if sys.argv[1] == "-i":
    try:
        tempo = float(sys.argv[2])
        intervalo = float(sys.argv[3])#Tempo de mudança de um Efeito para o outro
    except:
        pass

texto = sys.argv[4] + " " + sys.argv[5] 

#Limpamos a janela de comandos
os.system("cls")

#Efeito1-Diagonal Esquerda
for i in range(len(texto)):
    print(" " * i + texto[i])

time.sleep(intervalo)
os.system("cls")

#Efeito2-Diagonal Esquerda -->Invertida
for i in range(len(texto)):
    print(" " * i + texto[-(i + 1)])

time.sleep(intervalo)
os.system("cls")

#Efeito3-Diagonais Cruzadas

marcador = len(texto)//2 #Para ser mais rápido, o programa calcula este valor uma unica vez

for i in range(marcador): #Ao chegar a metade da diagonal, o programa tem de saber o que tem de fazer a seguir
    print(" " * i + texto[i] + " " * (len(texto) - 2*i) + texto[i])

if len(texto) % 2 == 0: #Se o numero de caracteres for par, o programa fará a cruz de uma forma
    print(" " * marcador + texto[marcador] * 2)
else: #Se for impar, o programa irá escrever apenas uma vez o caracter do meio
    print(" " * marcador + texto[marcador])

#Agora a cruz continua no sentido inverso

for i in range(marcador - 1):
    print(" " * (marcador - 1 - i) + texto[marcador + 1 + i] + " " * 2*(i + 1) + texto[marcador + 1 + i])

time.sleep(intervalo)
os.system("cls")

#Efeito4-Diagonal Direita-->Inversa
for i in range(len(texto)):
    print(" " * (len(texto) - i) + texto[-(i + 1)])

time.sleep(intervalo)
os.system("cls")

#Efeito5-Texto Deslizante em Ciclo

novoTexto = texto + " " * (40 - len(texto))

iteracao = 0 #Esta variavel ira contar quantas iterações passaram no efeito 5

while True:
    os.system("cls")
    output = ""
    
    i = 0 #O i é apenas um contador
    while len(output) < 40:
        output += novoTexto[-iteracao + i]
        i += 1
    iteracao += 1
    print(output)
    if iteracao == 41:
        iteracao = 0
    time.sleep(tempo)