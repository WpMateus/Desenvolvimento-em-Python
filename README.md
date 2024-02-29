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

Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

 
Exemplo de Entrada	Exemplo de Saída
4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554

encaixa
nao encaixa
encaixa
nao encaixa

N = int(input())

while(N > 0):
    a, b = input().split()
    N = N - 1

    if len(a) >= len(b):

      if (a[(len(a) - len(b)):]) == b:

          print("encaixa")

      else:

          print("nao encaixa")

    else:
     print("nao encaixa")

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

Fatiamento de strings e uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[, step]].

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
quadrado.append (numero ** 2)
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

DESAFIO
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

Exemplo de Entrada	Exemplo de Saída
RT @TheEllenShow:   TWEET
If only Bradley's 
arm was longer. 
Best photo ever. 
#oscars pic.twitter.com/C9U5NOtGap

T = input()
 
if len(T) > 140:
  print("MUTE")
else:
    print("TWEET")
```

### sorted

```python
linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python",
"csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp",
"java", "js", "c"]
```

### Tuplas

Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses.

```python
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)
```

### Acesso direto

A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

```python
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[0] # maçã
frutas[2] # uva
```

```python
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[-1] # pera
frutas[-3] # laranja
```

### Tuplas aninhadas

Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e
acessar informando os índices de linha e coluna.

```python
matriz = (
	(1,"a", 2),
	("b", 3, 4),
	(6, 5, "c"),

)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"
```

### Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

```python
tupla=("p","y","t","h","o","n",)

tupla[2:] #("t","h","o","n")
tupla[:2] #("p","y")
tupla[1:3] #("y","t")
tupla[0:3:2] #("p","t")
tupla[ :: ] #("p","y","t","h","o","n")
tupla[ ::- 1] #("n","o","h","t","y","p")
```

Percorrer elemento por elemento

```python
carros = ("gol", "celta", "palio",)

for carro in carros:
	print(carro)
```

### Função enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

```python
carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
		print(f"{indice}: {carro}")
```

### Métodos da classe tuple

### ().count

```python
cores = ("vermelho", "azul", "verde", "azul",)

cores. count("vermelho") # 1
cores. count("azul") # 2
cores.count("verde") # 1
```

### ().index

```python
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens. index("java") # 3
linguagens.index("python") # 0
```

### len

```python
linguagens = ("python", "js", "c", "java", "csharp",)

len(linguagens) # 5
```

### Conjuntos

### Criando sets

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

```python
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
```

### Acessando os dados

Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

```python
numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]
```

### Iterar conjuntos

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando **for**

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
		print(carro)
```

### Função enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço **for**. Para isso podemos usar a função **enumerate**.

```python
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
		print(f"{indice}: {carro}")
```

### Métodos da classe set

### {}.union

```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
```

### {}.intersection

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}
```

{}.difference

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}
```

### {}.symmetric_difference

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
```

### {}.issubset

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
```

{}.issuperset

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
```

### {}.isdisjoint

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False
```

{}.add

```python
sorteio = {1, 23}

sorteio. add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}
```

{}.clear

```python
sorteio = (1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}
```

{}.copy

```python
sorteio = (1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}
```

{}.discard

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```

{}.pop

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros. pop(} # 0
numeros . pop () # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}
```

{}.remove

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros. remove(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

{}.len

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10
```

### in

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False
```

### Dicionários

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.

```python
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"]= "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
```

### Acesso aos dados

Os dados são acessados e modificados através da chave.

```python
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"]= "9988-1781"

dados # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
```

### Dicionários aninhados

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números).

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
	"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"
```

### Iterar dicionários

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.

```python
for chave in contatos:
		print(chave, contatos[chave])

for chave, valor in contatos.items():
		print(chave, valor)

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
# melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
```

### Métodos da classe dict

### {}.clear

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
	"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

contatos.clear().
contatos # {}
```

### {}.copy

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

copia = contatos. copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone":
"3333-2221"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}
```

### {}.fromkeys

```python
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict. fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone":
"vazio"}
```

### {}.get

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome":"Guilherme", "telefone": "3333-2221"}
```

### {}.items

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

contatos.items() # dict_items([(*guilherme@gmail.com', {'nome': 'Guilherme','telefone': '3333-2221'})])
```

### {}.keys

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

contatos.keys() # dict_keys(['guilherme@gmail.com'])

Desafio
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

 
Exemplo de Entrada	Exemplo de Saída
4                   April

months_dict = {
  1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'
}

month = int(input())

if month in months_dict.keys():
    print(months_dict[month])
```

### {}.pop

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone':
'3333-2221'}
contatos.pop("guilherme@gmail.com", {}) # {}
```

### {}.popitem

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos. popitem() # KeyError
```

### {}.setdefault

```python
contato

contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna") # "Guilherme"
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # 28
contato # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
```

### {}.update

```python

contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos. update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3322-8181"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
```

### {}.values

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
	"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

contatos.values() # dict_values([{'nome': 'Guilherme', 'telefone':'3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie','telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])
```

### {}.in

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
	"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False
"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True
```

### {}.del

```python
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
	"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com'{'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome':'Melaine', 'telefone': '3333-7766'}}
```

### Funções

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.

```python
def exibir_mensagem():
		print("Olá mundo!")

def exibir_mensagem_2(nome) :
		print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
		print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
```

### Retornando valores

Para retornar um valor, utilizamos a palavra reservada return. Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

```python
def calcular_total(numeros) :
		return sum(numeros)

def retorna_antecessor_e_sucessor(numero) :
		antecessor = numero - 1
		sucessor = numero + 1

		return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
retorna_antecessor_e_sucessor(10) # (9, 11)

```

### Argumentos nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

```python
def salvar_carro(marca, modelo, ano, placa):
		# salva carro no banco de dados ...
		print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro( ** {"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa":
"ABC-1234"})

# Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
```

### Args e kwargs

Podemos combinar parametros obrigatorios com args e kwargs. Quando esses são definidos (*args e ** kwargs), o metodo recebe os valores como tupla e dicionário respectivamente.

```python
def exibir_poema(data_extenso, *args, ** kwargs):
		texto = "\n". join(args)
		meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
		mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
		print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim
Peters", ano=1999)
```

### Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados
por posição, por posição e nome, ou por nome.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/02b9ee7a-2b6e-4708-ab7d-cf4faaaefb71/a6ba9ac3-bde6-4181-b0c4-c54932e10379/Untitled.png)

### Positional only

```python
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # inválido
```

### Keyword only

```python
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel) :
		print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # inválido
```

### Keyword and positional only

```python
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # inválido
```

### Objetos de primeira classe

Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).

```python
def somar(a, b):
		return a + b

def exibir_resultado(a, b, funcao):
		resultado = funcao(a, b)
		print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20
```

### Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser evitada.

```python
salario = 2000

def salario_bonus(bonus) :
		global salario
		salario += bonus
		return salario

salario_bonus(500) # 2500
```

---

## Programação Orientada a Objetos (POO) Python

### O que é Orientação a Objetos (OO)? Classes e Objetos

Um paradigma de programação é um estilo e programação. Não é uma linguagem (Python, Java, C, etc), e sim a forma como você soluciona os problemas através do código.

**Exemplo:**

Problema: Beber água

Solução 1: Usar um copo para beber água.

Solução 2: Usar uma garrafa para beber água.

**Alguns paradigmas**

- Imperativo ou procedural
- Funcional
- Orientado a eventos

O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: **classes e objetos**.

---

### Classes e Objetos

Uma classe define as caracteristicas e comportamentos de um objeto, porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

### Classe

```python
class Cachorro:
	def _init_(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado

	def latir(self):
		print("Auau")

	def dormir(self):
		self.acordado = False
			print("Zzzzz ... ")
```

essa é a classe não posso utilizar a classe

### Objeto

```python
cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
```

Primeiro Programa em POO

João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

### Construtores e destrutores

Conhecendo os métodos __init__ e __del__

### Método construtor

O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um metodo com o nome __init__

```python
class Cachorro:
		def __init__(self, nome, cor, acordado=True):
				self.nome = nome
				self.cor = cor
				self.acordado = acordado
```

### Método destrutor

O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessarios quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um metodo com o nome __del__

```python
class Cachorro:
		def __del__(self):
				print("Destruindo a instância")

C = Cachorro()
del c

```
