# - ler 4 valores inteiros A,B,C,D
# - Se B for maior do que C e o D for maior do que o A e a soma do C + D for maior que a soma do A + B 
# - Se B for maior do que C e se D for maior do que A, 
# - Se soma de C com D for maior que a soma de A e B 
# - Se C e D, ambos, forem positivos 
# - Se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

A, B, C, D = map(int, input().split(' '))


if ((B > C and D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')