'''Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone.
Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe.
Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos,
sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

Entrada
Nome do usuário, número de telefone e plano.

Saída
Mensagem indicando que o usuário foi criado com sucesso.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. C
ertifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	            Saída
Ana                 Usuário Ana criado com sucesso.
(11) 91111-1111
Plano Essencial Fibra

Sofia
(22) 92222-2222
Plano Prata Fibra	 Usuário Sofia criado com sucesso.

Pedro
(33) 93333-3333
Plano Premium Fibra    Usuário Pedro criado com sucesso.'''


# TODO: Crie uma classe UsuarioTelefone.

class UsuarioTelefone:
    # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    # TODO: Defina um método especial `__init__`, que é o construtor da classe.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_plano(self):
        return self.__plano

    def set_plano(self, plano):
        self.__plano = plano


# Entrada:
nome = input()
numero = input()
plano = input()

# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)