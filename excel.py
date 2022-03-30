'''
Script referente a PARTE II do enunciado do Projecto 1 - UFCD10793
Faça um programa para traduzir as coordenadas "simbólicas" do Excel para coordenadas lineares.
Por exemplo, em Excel, internamente, a célula A1 corresponde à célula na linha 0 e coluna 0.

Projecto realizado por:
Adriana de Souza Gama
Carlo Braga
'''
while True:
	#Primeiro pedimos ao utilizador para nos indicar as coordenadas pretendidas
	raw = input("Indique as coordenadas: ")
	
	if raw.lower() == "sair": #Verifica se o utilizador quer continuar a usar o programa
		break
	
	dados = raw.split()
	colunaTemp = dados[0] #Primeiro a coluna é carregada (como letras)
	coluna = 0
	linha = int(dados[1]) - 1 #Os números das linhas começam no 0
	
	def converter(char): #Para facilitar o código, podemos definir uma função para converter letras em números
		letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		for i in range(len(letras)):
			if char.lower() == letras[i]:
				return i + 1 #O indice da letra vai ser igual à sua posição no alfabeto (a = 1, b = 2, c = 3, ...)
	
	for i in range(len(colunaTemp)):
		coluna += converter(colunaTemp[-i - 1]) * 26 ** i #O número é convertido da base 26 para a base 10 segundo esta fórmula
        
	coluna -= 1 #Os números das colunas começam no 0
	print("Linha:", linha, "Coluna:", coluna,"\n-------") #O resultado é apresentado
print("fim do programa")