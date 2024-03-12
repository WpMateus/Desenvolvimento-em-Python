# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

idade_dia = int(input())

#anos
ano = idade_dia // 365
idade_dia = idade_dia % 365

#mes
mes = idade_dia // 30
idade_dia = idade_dia % 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{idade_dia} dia(s)')


#CÓDIGO ABAIXO CALCULA CERTO, PORÉM NÃO DA A SAÍDA COM
#OS MESES CORRETOS. O CÓDIGO ACIMA FUNCIONA NORMALMENTE

# ano_mes = [365, 30, 1]

# for idade in ano_mes:
#     x = idade_dia // idade
#     print(f'{x} anos (s)')
#     idade_dia -= x*idade
