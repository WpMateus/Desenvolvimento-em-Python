"""A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. 
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. 
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. 
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. 
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

Exemplo de Entrada	
3 2
1
2 3
1
3 1
2

Exemplo de Saída
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais"""


resultado_inter = 0
resultado_gremio = 0
contador_grenais = 0
empate = 0
resposta = '1'

while resposta == '1':
    inter, gremio = map(int, input().split(" "))
    resposta = input("Novo grenal (1-sim 2-nao)\n")
    contador_grenais += 1
    if inter > gremio:
        resultado_inter += 1
    elif inter < gremio:
        resultado_gremio += 1
    elif inter == gremio:
        empate += 1

print(f"{contador_grenais} grenais")
print(f"Inter:{resultado_inter}")
print(f"Gremio:{resultado_gremio}")
print(f"Empates:{empate}")
if resultado_inter > resultado_gremio:
    print("Inter venceu mais")
elif resultado_inter < resultado_gremio:
    print("Gremio venceu mais")
elif resultado_inter == resultado_gremio:
    print("Nao houve vencedor")