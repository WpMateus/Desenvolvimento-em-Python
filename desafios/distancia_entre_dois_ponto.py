# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia =

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

x1, y1 = input().split(" ")
x2, y2 = input().split(" ")

X1 = float(x1)
Y1 = float(y1)
X2 = float(x2)
Y2= float(y2)

distancia = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

print(f'{distancia:.4f}')