class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
    #Self é uma referência para o objeto, ela é explicita, quando coloamos self, queremos dizer que essa é a instância 
    #do objeto que foi passada
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bi Bi!")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Zuuummmmm!")

    #Se o nome do método for igual ao atributo na hora de chamar em baixo da erro
    # def get_cor(self):
    #     return self.cor

    # valores que tem dentro da classe
    def __str__(self):
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha","caloi", 2024, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("amarela", "monark", 2000, 190)
print(b2)

b2.buzinar()  #Bicicleta.buzinar(b2)
print(b2.cor)