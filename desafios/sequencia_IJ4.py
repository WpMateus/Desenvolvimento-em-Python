# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.

# Exemplo de Saída
# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?

I = 0
J = 1

while I <= 2:
    
    for sequencia in range(3):

        if I != int(I):
            print(f'I={I:.1f} J={J:.1f}')
        else:
            print(f'I={I:.0f} J={J:.0f}')
        J += 1

    I = round( I + 0.2, 1)
    J = round( J - 2.8, 1)