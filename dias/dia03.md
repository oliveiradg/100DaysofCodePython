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

## Dia 03:

As declarações condicionais, também conhecidas como estruturas de controle de fluxo, permitem que um programa tome decisões com base em certas condições. Em Python, a estrutura mais comumente usada para implementar declarações condicionais é o "if/else".

A sintaxe básica do "if/else" em Python é a seguinte:

~~~python
if condição:
    # Bloco de código a ser executado se a condição for verdadeira
else:
    # Bloco de código a ser executado se a condição for falsa
~~~

A palavra-chave "if" é seguida pela condição que deve ser avaliada. Se a condição for avaliada como verdadeira, o bloco de código indentado abaixo do "if" será executado. Caso contrário, o bloco de código indentado abaixo do "else" será executado.

É importante observar que a indentação é crucial em Python, pois define a estrutura do código. Blocos de código indentados no mesmo nível são considerados parte do mesmo bloco lógico.

Além do "if/else", também podemos ter múltiplas condições utilizando a estrutura "if/elif/else". Isso permite verificar várias condições sequencialmente até encontrar uma que seja verdadeira. A sintaxe é a seguinte:

~~~python

if condição1:
    # Bloco de código a ser executado se condição1 for verdadeira
elif condição2:
    # Bloco de código a ser executado se condição2 for verdadeira
else:
    # Bloco de código a ser executado se nenhuma das condições anteriores for verdadeira

~~~

Nesse caso, o programa verifica a primeira condição. Se for verdadeira, executa o bloco de código associado a essa condição. Caso contrário, passa para a próxima condição e assim por diante. Se nenhuma das condições anteriores for verdadeira, o bloco de código associado ao "else" será executado.

Além dos operadores de comparação mencionados anteriormente (maior que, menor que, igual a, etc.), também podemos utilizar operadores lógicos, como "and" (e), "or" (ou) e "not" (não), para combinar condições em declarações condicionais mais complexas.

Por exemplo:

~~~python
if condição1 and condição2:
    # Bloco de código a ser executado se ambas as condições forem verdadeiras

~~~~

Nesse caso, o bloco de código só será executado se ambas as condições forem avaliadas como verdadeiras.

As declarações condicionais são fundamentais na programação, pois permitem que o programa tome decisões com base em diferentes cenários. Essa estrutura de controle de fluxo é amplamente utilizada para implementar lógica condicional em programas Python, possibilitando a execução de diferentes ações com base em diferentes condições.

Neste ponto, fizemos  uma revisão das declarações condicionais básicas em Python, onde usamos a palavra-chave "if" para verificar uma condição e executar um bloco de código se essa condição for verdadeira. Se a condição não for verdadeira, podemos utilizar a palavra-chave "else" para executar um bloco de código alternativo.

No entanto, nem sempre lidamos apenas com uma única condição em nossos programas. Às vezes, é necessário verificar várias condições diferentes e executar blocos de código diferentes com base nessas condições. É aí que entram as declarações "if/else" aninhadas e a declaração "elif" (que significa "else if" em inglês).

Com declarações "if/else" aninhadas, podemos ter uma condição "if" principal e, se essa condição for verdadeira, podemos ter outra declaração "if/else" aninhada dentro do bloco de código associado a essa condição "if". Isso nos permite verificar uma condição adicional e executar um bloco de código diferente com base nessa nova condição.

A declaração "elif" é usada quando queremos verificar uma condição adicional se a condição anterior do "if" ou "elif" for falsa. Assim, podemos encadear várias declarações "elif" para verificar diferentes condições. A primeira condição que for verdadeira terá seu bloco de código associado executado, e as condições subsequentes serão ignoradas.

No exemplo do texto, foi dado um exemplo de um programa que verifica a altura e a idade de uma pessoa para determinar o preço de um bilhete. Primeiro, é verificado se a altura é superior a 120 centímetros. Se essa condição for verdadeira, então é verificado se a idade é inferior a 18 anos. Se a idade for inferior a 18 anos, o preço do bilhete é definido como $7. Caso contrário, se a idade for maior ou igual a 18 anos, o preço do bilhete é definido como $12.

A introdução do "elif" pode ser útil quando há mais de duas condições possíveis a serem verificadas. Por exemplo, no mesmo programa do exemplo, poderíamos adicionar uma condição "elif" para verificar se a idade é menor que 12 anos e atribuir um preço de $5 para essa faixa etária específica.

É importante lembrar que a ordem das condições "if/elif/else" é significativa. As condições são verificadas na ordem em que aparecem no código, e a primeira condição que for verdadeira terá seu bloco de código executado. Portanto, é importante definir as condições na ordem correta para que o comportamento esperado seja alcançado.

Dominar as declarações condicionais aninhadas e o uso de "elif" nos permite criar lógicas mais complexas em nossos programas, com a capacidade de lidar com várias condições e tomar decisões com base nesses diferentes cenários.

Por último, foi abordado o tema de como verificar múltiplas condições em um código utilizando os conceitos de "if", "elif" e "else" em Python. O exemplo utilizado foi o de um parque de diversões que emite bilhetes para uma montanha-russa.

Inicialmente, o código verificava a altura dos usuários para determinar o preço do bilhete. Em seguida, foi adicionada a opção de perguntar aos usuários se desejam comprar um bilhete que inclua uma fotografia, independentemente de sua idade ou altura.

A implementação dessa funcionalidade foi realizada através de uma estrutura condicional "if" após a verificação da altura. Foi adicionado um input para perguntar aos usuários se desejam uma foto, e a resposta foi armazenada em uma variável chamada "wants_photo".

Em seguida, foi utilizado um bloco "if" para verificar se a resposta foi "Y" (sim). Se a resposta for verdadeira, um valor de $3 é adicionado à variável que armazena o preço do bilhete, denominada "Bill". Isso é feito utilizando o operador "+=" para adicionar o valor atual da conta à variável. Caso a resposta seja "N" (não), o código prossegue sem adicionar valor à conta.

No final, é exibido o valor total do bilhete, utilizando uma declaração impressa com f-strings para inserir o valor da variável "Bill" na mensagem.

Aqui está um exemplo de código baseado nas informações do texto:

~~~~python
height = float(input("Qual é a sua altura em centímetros? "))

if height > 120:
    age = int(input("Qual é a sua idade? "))
    if age < 12:
        Bill = 5
    elif age < 18:
        Bill = 7
    else:
        Bill = 12
    
    wants_photo = input("Deseja comprar um bilhete com foto? (Y/N) ")
    
    if wants_photo == "Y":
        Bill += 3
    
    print(f"O preço do seu bilhete é ${Bill}.")
else:
    print("Você não atende aos requisitos de altura para andar na montanha-russa.")
~~~

Este resumo abrange os conceitos principais do texto, explicando como verificar múltiplas condições em um código Python e implementar a funcionalidade de adicionar um valor extra à conta do bilhete com base na resposta do usuário.

<br>
<br>

<a href="../readme.md">Página Inicial</a> 