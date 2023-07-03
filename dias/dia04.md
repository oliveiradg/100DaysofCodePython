<div align="center">
<a href="https://github.com/oliveiradg" target="_blank"><img align="right" height="100" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" /></a>




<h1>100 Days of Code: The Complete Python Pro Bootcamp</h1>

<h2>Estudo de Desenvolvimento em <br> Python</h2>

<p>Dominando o Python: E criando 100 projetos em 100 dias. 
<br>
#100daysofcode

##### Contato: <a href="https://www.linkedin.com/in/joaooliveiradg/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="JBOliveira" height="20" width="20" /></a> 

  
</p>




<div align= "center">



<a href="https://github.com/oliveiradg" target="_blank"><img align="center" height="200" src="../images/100daysPython-removebg.png" /></a>
</div>
<br>

</div>
</div>

## Dia 04:

Abordamos hoje o conceito de randomização e sua importância na criação de programas de computador, especialmente em jogos. Explica que os computadores são deterministas por natureza, ou seja, realizam ações previsíveis, mas é possível criar números aleatórios usando geradores de números pseudoaleatórios. No caso do Python, é utilizado o gerador Mersenne Twister. O texto recomenda um vídeo da Khan Academy para aprender mais sobre geradores de números pseudoaleatórios.

Em seguida, o texto introduz o módulo random do Python, que facilita a geração de números aleatórios. Mostra como importar o módulo e utilizar a função randint para gerar números inteiros aleatórios em um determinado intervalo. Também menciona que os módulos são usados para dividir o código em partes separadas, cada uma responsável por uma funcionalidade específica.

O texto continua demonstrando como gerar números de ponto flutuante aleatórios usando a função random do módulo random. Explica que essa função gera números entre 0 e 1, excluindo 1, e mostra como multiplicar esse número pelo intervalo desejado para obter números aleatórios em um intervalo maior.

Por fim, foi visto o uso de números aleatórios em diferentes contextos, como calcular uma "pontuação de amor" aleatória ou simular o lançamento de um dado ou moeda.

<br>
<br>

Nesta lição, aprendemos sobre o conceito de listas em Python, que são estruturas de dados usadas para armazenar e organizar múltiplos itens relacionados. As listas são delimitadas por colchetes retos e os itens são separados por vírgulas. Podemos armazenar diferentes tipos de dados em uma lista, inclusive misturá-los. A ordem dos itens em uma lista é preservada.

Acessar itens em uma lista é feito utilizando índices. Os índices começam em 0, então o primeiro item da lista tem índice 0, o segundo tem índice 1 e assim por diante. Também é possível utilizar índices negativos para acessar itens a partir do final da lista.

Podemos modificar os itens de uma lista atribuindo um novo valor a um índice específico. Além disso, podemos adicionar itens a uma lista usando a função append() para adicionar um item ao final da lista.

Existem várias outras funções e métodos disponíveis para trabalhar com listas, como a função len() para obter o tamanho da lista, a função extend() para adicionar múltiplos itens ao final da lista e a função insert() para inserir um item em uma posição específica.

Exemplo:
Vamos criar um exemplo para ilustrar o uso de listas em Python. Neste caso, vamos criar uma lista de compras contendo diferentes itens.

<br>

~~~python

# Criando a lista de compras
lista_de_compras = ["maçã", "banana", "pão", "leite"]

# Acessando um item da lista
print(lista_de_compras[0])  # Saída: maçã

# Modificando um item da lista
lista_de_compras[2] = "queijo"

# Adicionando um item à lista
lista_de_compras.append("ovos")

# Imprimindo a lista de compras
print(lista_de_compras)
# Saída: ['maçã', 'banana', 'queijo', 'leite', 'ovos']

~~~

Neste exemplo, criamos uma lista de compras inicial contendo maçã, banana, pão e leite. Em seguida, acessamos o primeiro item da lista utilizando o índice 0 e imprimimos o resultado. Depois, modificamos o terceiro item da lista para "queijo" e adicionamos "ovos" ao final da lista usando append(). Por fim, imprimimos a lista atualizada.

<br>

Durante essa lição, discutimos sobre erros de índice e listas aninhadas em Python. Aqui está um resumo do que foi estudado:

Erros de índice: Ocorrem quando tentamos acessar um índice que está além dos limites da lista. Isso geralmente acontece quando o índice é maior do que o tamanho da lista ou menor do que zero. Para corrigir esse erro, é necessário ajustar o índice dentro dos limites válidos da lista.
Exemplo:

<br>
~~~python
# Criando uma lista
lista = ["maçã", "banana", "pão", "leite"]
# Acessando um item da lista
print(lista[4])
# Saída: IndexError: list index out of range
~~~
<br>
Listas aninhadas: São listas que contêm outras listas. Para acessar um item de uma lista aninhada, é necessário utilizar dois índices. O primeiro índice acessa a lista e o segundo acessa o item dentro da
lista.
Exemplo:

~~~python

frutas = ["maçã", "banana", "laranja"]
legumes = ["cenoura", "abobrinha", "brócolis"]
dirty_dozen = [frutas, legumes]

~~~

Neste exemplo, a lista dirty_dozen contém as listas frutas e legumes. Portanto, temos uma lista aninhada. Podemos acessar os elementos das listas aninhadas da seguinte maneira:

~~~python

print(dirty_dozen[0])  # Acessando a lista de frutas
print(dirty_dozen[1])  # Acessando a lista de legumes

~~~


<br>

~~~python
lista = [1, 2, 3, 4, 5]
# Tentando acessar o índice 10, que está além do tamanho da lista
elemento = lista[10]  # Isso resultará em um erro de índice

~~~

Listas aninhadas: São listas que contêm outras listas como elementos. Isso permite a organização de dados relacionados em uma estrutura hierárquica.
Exemplo:



<br>

Neste exemplo, a lista dirty_dozen contém as listas frutas e legumes. Portanto, temos uma lista aninhada. Podemos acessar os elementos das listas aninhadas da seguinte maneira:


# exemplo 2
~~~python
# Criando uma lista aninhada
lista_aninhada = [["maçã", "banana", "pão"], ["leite", "café", "chocolate"]]
# Acessando um item da lista aninhada
print(lista_aninhada[0][2])
# Saída: pão
~~~
<br>
<br>
## Exercícios
1. Crie uma lista de compras com os seguintes itens: maçã, banana, pão, leite e café.
2. Adicione um novo item à lista de compras chamado "arroz".
3. Imprima a lista de compras.
4. Adicione um novo item à lista de compras chamado "ovo".
5. Imprima a lista de compras.
6. Adicione um novo item à lista de compras chamado "ovo" na posição 2.
7. Imprima a lista de compras.
8. Adicione um novo item à lista de compras chamado "ovo" na posição 0.
9. Imprima a lista de compras.
10. Adicione um novo item à lista de compras chamado "ovo" na posição 4.
11. Imprima a lista de compras.

<br>
<br>
## Solução
~~~python
# Criando uma lista de compras
lista_compras = ["maçã", "banana", "pão", "leite", "café"]
# Adicionando um novo item à lista de compras
lista_compras.append("arroz")
# Imprimindo a lista de compras
print(lista_compras)
# Adicionando um novo item à lista de compras
lista_compras.append("ovo")
# Imprimindo a lista de compras
print(lista_compras)
# Adicionando um novo item à lista de compras
lista_compras.insert(2, "ovo")
# Imprimindo a lista de compras
print(lista_compras)
# Adicionando um novo item à lista de compras
lista_compras.insert(0, "ovo")
# Imprimindo a lista de compras
print(lista_compras)
# Adicionando um novo item à lista de compras
lista_compras.insert(4, "ovo")
# Imprimindo a lista de compras
print(lista_compras)
~~~
<br>
<br>


Resumo do Módulo sobre Erros de Índice e Listas Aninhadas em Python:

Neste módulo, exploramos dois conceitos importantes em Python: erros de índice e listas aninhadas. Aqui está um resumo do que aprendemos:

1. Erros de Índice:
- Erros de índice ocorrem quando tentamos acessar um índice inválido em uma lista.
- Esses erros podem acontecer quando o índice está além dos limites da lista (maior que o tamanho da lista ou menor que zero).
- Para corrigir um erro de índice, devemos ajustar o índice para que esteja dentro dos limites válidos da lista.

2. Listas Aninhadas:
- Listas aninhadas são estruturas de dados em que uma lista contém outras listas como elementos.
- Elas são úteis para organizar dados relacionados em uma estrutura hierárquica.
- Podemos acessar os elementos das listas aninhadas usando a notação de índice múltiplo, ou seja, fornecendo o índice da lista externa e, em seguida, o índice da lista interna.

Durante a exploração desses conceitos, usamos exemplos práticos para ilustrar seu funcionamento e como aplicá-los. Compreender os erros de índice e a utilização de listas aninhadas é fundamental para lidar com dados estruturados e escrever código Python eficiente.

 



<br>
<br>

<a href="../readme.md">Página Inicial</a> 


