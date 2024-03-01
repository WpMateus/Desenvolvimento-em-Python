#Exemplo for
#texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")
	

#Exemplo range
for numero in range(0, 11):
 print(numero, end=" ")
#>>> 0 1 2 3 45 6 7 89 10
 
print()

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
 print(numero, end=" ")
#>>> 0 5 10 15 20 25 30 35 40 45 50