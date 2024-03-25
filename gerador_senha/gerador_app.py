from random import random, choice
import string
import textwrap

valores = string.ascii_letters + string.digits + string.punctuation
valores_numeros = string.digits

def menu():
    menu = """\n
        =============== Bem-vindo ao GERADOR DE SENHA ===============
                              
        [sc]\tSenha completa -(Maiuscula, minuscula, especial e número)
        [sn]\tSenha números - (Apenas números)
        [e]\tSair
        
        => """
    return input(textwrap.dedent(menu))


def validar_tamanho_senha(tamanho_senha):
    while True:
        if 5 <= tamanho_senha <= 128:
            return tamanho_senha
        else:
            print("Tamanho da senha não aceito")
            tamanho_senha = int(input("Digite novamente o número de caracteres que deseja que a senha tenha: (Mín 5, Máx 128) => "))
    
def senha_compl(tamanho_senha):
    senha = ""
    for tam_senha_nrm in range(tamanho_senha):
        senha += choice(valores)
    return senha
        
def senha_nrm(tamanho_senha):
    senha = ""
    for tam_senha_nrm in range(tamanho_senha):
        senha += choice(valores_numeros)
    return senha

def main():
    while True:
        opcao = menu()

        if opcao == "sc":
            tamanho_senha = int(input("""\n
        =============== GERADOR DE SENHA ===============

        Digite o número de caracteres que deseja que a senha tenha: 
        (Mín 5, Máx 128)
                            
        => """))
            tamanho_senha = validar_tamanho_senha(tamanho_senha)
            senha = senha_compl(tamanho_senha)
            print(f'Sua senha é: {senha}')
        elif opcao == "sn":
            tamanho_senha = int(input("""\n
        =============== GERADOR DE SENHA ===============

        Digite o número de caracteres que deseja que a senha tenha: 
        (Mín 5, Máx 128)
                            
        => """))
            tamanho_senha = validar_tamanho_senha(tamanho_senha)
            senha_nrm(tamanho_senha)
            senha = senha_nrm(tamanho_senha)
            print(f'Sua senha é: {senha}')
        elif opcao == "e":
            print("Volte sempre!")
            break
        else:
            print("Opção inválida, tente novamente!")

main()