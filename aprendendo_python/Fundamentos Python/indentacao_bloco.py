
def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("Valor sacada!")
        print("Retire o seu dinheiro no caixa")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)

