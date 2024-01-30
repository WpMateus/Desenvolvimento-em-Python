# Python

### Tipos de dados

Os tipos servem para definir as características e comportamentos de um valor (objeto) para o interpretador.

Os tipos built-in em Python:

- Números: int, float, complex
- Texto: str
- Sequências: list, tuple, range
- Mapeamentos: dict
- Conjuntos: set, frozenset
- Booleanos: bool
- Binário: bytes, bytearray, memoryview
- None

Números **inteiros** são representados pela classe `int`. Exemplos:

1, 10, 100, -1, -10, -100…99001823

Números de **ponto flutuante** são representados pela classe `float`. Exemplos de números de ponto flutuante incluem:

1.0, 3.14, -2.5, 0.5, -10.75, 2.71828

### Booleano em Python

O tipo de dado booleano em Python é representado pela classe `bool`. Ele possui apenas dois valores possíveis: `True` (verdadeiro) e `False` (falso). Os booleanos são frequentemente usados em expressões lógicas e condições de controle de fluxo.

Exemplo de uso do tipo booleano em Python:

```python
verdadeiro = True
falso = False

if verdadeiro:
    print("Esta condição é verdadeira!")

if not falso:
    print("Esta condição também é verdadeira!")

```

### Strings em Python

As strings em Python são representadas pela classe `str`. Elas são utilizadas para armazenar e manipular texto. Exemplos de strings em Python:

“Python”, ‘Python’

### Variáveis e constantes

## Variáveis

Em linguagens de programação, as variáveis são utilizadas para armazenar e manipular valores. Elas são como "caixas" onde podemos guardar dados que serão utilizados ao longo do programa. Em Python, podemos declarar uma variável atribuindo um valor a ela.

Exemplo de declaração de variável em Python:

```python
nome = "João"
idade = 25
altura = 1.75

```

## Constantes

As constantes são valores que não podem ser alterados durante a execução de um programa. Em Python, não há um tipo de dado específico para constantes, mas por convenção, os nomes das constantes são escritos em letras maiúsculas para indicar que seu valor não deve ser modificado.

Exemplo de uso de constantes em Python:

```python
PI = 3.14159
GRAVIDADE = 9.8
DIAS_SEMANA = 7

```

### Boas práticas

- O padrão de nomes deve ser snake case. Ex: preco_Total
- Escolher nomes sugestivos
- Nome de constantes todo em maiúsculo. Ex: PRECO_TOTAL

### Conversão de tipos

Python oferece funções embutidas para converter um tipo de dado em outro. Essas funções incluem:

- `int()`: converte um valor em um número inteiro.
- `float()`: converte um valor em um número de ponto flutuante.
- `str()`: converte um valor em uma string.
- `bool()`: converte um valor em um booleano.

Exemplo de conversão de tipos em Python:

```python
numero = "10"
inteiro = int(numero)
print(inteiro)  # Output: 10

valor = 3.14
texto = str(valor)
print(texto)  # Output: "3.14"

verdadeiro = bool(1)
falso = bool(0)
print(verdadeiro)  # Output: True
print(falso)  # Output: False

```

É importante ter cuidado ao realizar conversões de tipos, pois algumas conversões podem levar à perda de informações ou a resultados inesperados.

### Funções de entrada e saída

## Lendo valores com a função input

A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

## Função print

A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/02b9ee7a-2b6e-4708-ab7d-cf4faaaefb71/1971b993-e1e9-4fb5-b032-a7132c52933f/Untitled.png)

### Operadores aritméticos

Os operadores aritméticos em Python são utilizados para realizar operações matemáticas entre valores numéricos. Alguns dos operadores aritméticos mais comuns são:

- `+`: realiza a adição de dois valores.
- `-`: realiza a subtração de dois valores.
- `*`: realiza a multiplicação de dois valores.
- `/` : realiza a divisão de dois valores.
- `//`: realiza a divisão inteira de dois valores.
- `%`: retorna o resto da divisão entre dois valores.
- `**` : realiza a potenciação de um valor.

### Operadores de comparação

São operadores para comparar dois valores.

- Igualdade `==`
- Diferença `!=`
- Maior que / maior ou igual `> / >=`
- Menor que / menor ou igual `< / <=`

### Operadores de atribuição

São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável

- Atribuição simples `=`
- Atribuição com adição `+=`
- Atribuição com subtração `-=`
- Atribuição com multiplicação `*=`
- Atribuição com divisão `/=`
- Atribuição com divisão inteira `//=`
- Atribuição com módulo `%=`
- Atribuição com exponenciação `**=`

### Operadores lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.

# Operadores Lógicos

Em Python, os operadores lógicos são utilizados para combinar expressões lógicas e avaliar se uma determinada condição é verdadeira ou falsa. Os operadores lógicos mais comuns são:

- `and`: Retorna verdadeiro se todas as expressões forem verdadeiras.
- `or`: Retorna verdadeiro se pelo menos uma das expressões for verdadeira.
- `not`: Inverte o valor de uma expressão lógica.

Exemplo de uso dos operadores lógicos em Python:

```python
x = 5
y = 10
z = 15

# Operador "and"
if x < y and y < z:
    print("x é menor que y e y é menor que z")

# Operador "or"
if x > y or y > z:
    print("pelo menos uma das condições é verdadeira")

# Operador "not"
if not x > y:
    print("x não é maior que y")

```

É importante entender como os operadores lógicos funcionam para construir expressões lógicas corretas e obter resultados esperados em suas condições de controle de fluxo.

### Operadores de identidade

São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória. É utilizado o is.

```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

True

curso is not nome_curso
False

saldo is limite
True
```

### Operadores de associação

São operadores utilizados para verificar se um objeto está presente em uma sequência.

É utilizado o in

```python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maçã" not in frutas
>>> True

200 in saques
>>> False
```

### Indentação e blocos

### Indentar

Indentar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

### Bloco

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves:

```java
void sacar(double valor) { // inicio do bloco do método

if (this.saldo >= valor) { // início do bloco do if

this.saldo -= valor;

} // fim do bloco do if

// fim do bloco do método
```

### Utilizando espaço

Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

```python
def sacar(self, valor: float) -> None: # início do bloco do método

if self.saldo >= valor: # início do bloco do if

self.saldo -= valor

# fim do bloco do if

# fim do bloco do método
```

### Estruturas condicionais

### if / if-else / elif

A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

### If

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando ira testar a expressao logica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

Ex:

```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
print("Realizando saque!")

if saldo <= saque:
print("Saldo insuficiente!")
```

### If-else

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário, o bloco de código do else será executado.

Ex:

```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
print("Realizando saque!")
else:
print("Saldo insuficiente!")
```

### Elif

Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

Ex:

```python
opcao = int(input("Informe uma opçao: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
valor = float(input("Informe a quantia para o saque: "))
#
elif opcao == 2:
print("Exibindo o extrato ... ")
else:
sys.exit("Opção inválida")
```

### If aninhado

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

```python
if conta_normal:
		if saldo >= saque:
				print("Saque realizado com sucesso!")
		elif saque <= (saldo + cheque_especial):
				print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
		if saldo >= saque:
				print("Saque realizado com sucesso!")
		else:
				print("Saldo insuficiente!")
```

### If ternário

O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

```python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
```

### Estruturas de repetição

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado por meio de uma expressão lógica.

### FOR

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
		if letra.upper() in VOGAIS:
				print(letra, end="")

print() # adiciona uma quebra de linha
```

### Função range

Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: i, i+1, i+2, i+3, ... , j-1.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

```python
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
>>> [0, 1, 2, 3]
```

Utilizando range com for

```python
for numero in range(0, 11):
print(numero, end=" ")

>>> 0 1 2 3 45 6 7 89 10

4

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
print(numero, end=" ")

>>> 0 5 10 15 20 25 30 35 40 45 50
```

### While

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

```python
opcao = -1

while opcao != 0:
		opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

		if opcao == 1:
			print("Sacando ... ")
		elif opcao == 2:
			print("Exibindo o extrato ... ")
```

### Métodos úteis da classe string

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.

Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

Maiúscula, minúscula e título

```python
curso = "pYtHon"

print(curso.upper())
PYTHON

print(curso.lower())
python

print(curso.title())
Python
```

Eliminando espações em branco da string

```python
curso = "   Python "

print(curso.strip())
"Python"

print(curso.lstrip())
"Python "

print(curso.rstrip())
"  Python"

```

Junções e centralização

```python
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
```

### Interpolação de variáveis

Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings.

A primeira forma não e atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

### Old style %

```python
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e
estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como
Progamador e utilizo e estou matriculado no curso de Python.
```

### Método format

```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e
estou matriculado no curso de {}.".format(nome, idade, profissao,
linguagem) )

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e
estou matriculado no curso de {0}.".format(linguagem, profissao, idade,
nome) )

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como
{profissao} e estou matriculado no curso de
{linguagem}. ". format(nome=nome, idade=idade, profissao=profissao,
linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como
{profissao} e estou matriculado no curso de
{linguagem}.".format( ** pessoa))

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como
Progamador e utilizo e estou matriculado no curso de Python.
```

### f-string

```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho
como {profissao} e estou matriculado no curso de {linguagem}.")

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como
Progamador e utilizo e estou matriculado no curso de Python.
```

### Formatar strings com f-string

```python
PI = 3.14159

print(f"Valor de PI: {PI :. 2f}")
>>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}")
>>> "Valor de PI:

3.14"
```

### Fatiamento de string

Fatiamento de strings e uma técnica utilizada para retornar
substrings (partes da string original), informando inicio (start),
fim (stop) e passo (step): [start: stop[, step]].

```python
nome = "Guilherme Arthur de Carvalho"

nome[0]
"G"

nome[:9]
>>> "Guilherme"

nome[10:]
>>> "Arthur de Carvalho"

nome[10:16]
00 "Arthur"

nome[10:16:2]
>> "Atu"

nome[:]
>>> "Guilherme Arthur de Carvalho"

nome[ ::- 1]
>>> "ohlavraC ed ruhtrA emrehliuG"
```

### String múltiplas linhas

Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

```python
nome = "Guilherme"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python

>>>

Olá meu nome é Guilherme,
Eu estou aprendendo Python
```

### Listas: Criação e acesso aos dados

Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

```python
frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
```

### Acesso direto

A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

```python
frutas = ["maçã", "laranja", "uva", "pera"]
frutas[0] # maçã
frutas[2] # uva
```

### Índices negativos

Sequências suportam indexação negativa. A contagem começa em -1.

```python
frutas = ["maçã", "laranja", "uva", "pera"]
frutas[-1] # pera
frutas[-3] # laranja
```

### Listas aninhadas

Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

```python
matriz = [
	[1, "a", 2],
	["b", 3, 4],
	[6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"
```

### Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

```python
lista=["p","y","t","h","o","n"]

lista[2:] #["t","h","o","n"]
lista[:2] #["p","y"]
lista[1:3] #["y","t"]
lista[0:3:2] #["p","t"]
lista[ :: ] #["p","y","t","h","o","n"]
lista[ ::- 1] #["n","o","h","t","y","p"]
```

### Iterar listas

A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for**

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
	print(carro)
```

### Função enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

```python
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")
```

### Compreensão de listas

A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

### Filtro versão 1

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
	if numero % 2 == 0:
			pares. append (numero)
```

### Filtro versão 2

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
```

### Modificando valores versão 1

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
quadrado.append (numero **

2)
```

### Modificando valores versão 2

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
```

### Métodos da classe list

### [].append

```python
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]
```

### [].clear

```python
lista = [1, "Python", [40, 30, 20]]

print(lista) # [1, "Python , [40, 30, 20]]

lista.clear()

print(lista) # []
```

### [].copy

```python
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)

# [1, "Python", [40, 30, 20]]
```

### [].count

```python
cores = ["vermelho", "azul", "verde", "azul"]

cores. count("vermelho") # 1
cores.count("azul") # 2
cores. count("verde") # 1
```

### [].extend

```python
linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]
```

### [].index

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3
linguagens. index("python") # 0
```

### [].pop

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens. pop() # csharp
linguagens. pop() # java
linguagens . pop () # C
linguagens. pop(0) # python
```

### [].remove

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ["python", "js", "java", "csharp"]
```

### [].reverse

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens. reverse()

print(linguagens) # ["csharp", "java", "c", "js", "python"]
```

### [].sort

```python
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens. sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp",
"java", "js", "c"]
```

### len

```python
linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) #5
```

### sorted
