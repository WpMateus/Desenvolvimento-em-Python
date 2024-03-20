import textwrap

def menu():
    menu = """\n
    ================ OPERAÇÃO ================
    [a]\tAdição
    [s]\tSubtração
    [m]\tMultiplicação
    [d]\tDivisão
    [p]\tPotência
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def adicao(numero1, numero2):
    resultado_adicao = numero1 + numero2
    print(resultado_adicao)
    return resultado_adicao

def subtracao(numero1, numero2):
    resultado_subtracao = numero1 - numero2
    print(resultado_subtracao)
    return resultado_subtracao

def multiplicacao(numero1, numero2):
    resultado_multiplicacao = numero1 * numero2
    print(resultado_multiplicacao)
    return resultado_multiplicacao

def divisao(numero1, numero2):
    resultado_divisao = numero1 / numero2
    print(resultado_divisao)
    return resultado_divisao

def potencia(numero1, numero2):
    resultado_potencia = numero1 ** numero2
    print(resultado_potencia)
    return resultado_potencia



def main():

    while True:
        opcao = menu()

        if opcao == "a":
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))

            resultado = adicao(numero1, numero2)

        elif opcao == "s":
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))

            resultado = subtracao(numero1, numero2)

        elif opcao == "m":
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))

            resultado = multiplicacao(numero1, numero2)

        elif opcao == "d":
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))

            resultado = divisao(numero1, numero2)
            
        elif opcao == "p":
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))

            resultado = potencia(numero1, numero2)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
