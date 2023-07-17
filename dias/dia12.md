
<div align="center">
<a href="https://github.com/oliveiradg" target="_blank"><img align="right" height="100" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" /></a>




<h1>100 Days of Code: The Complete Python Pro Bootcamp</h1>

<h2>Estudo de Desenvolvimento em <br> Python</h2>

<p> Dominando o Python em 100 dias. 
<br>
#100daysofcode

##### Contato: <a href="https://www.linkedin.com/in/joaooliveiradg/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="JBOliveira" height="20" width="20" /></a> 

  
</p>



           

<div align= "center">



<a href="https://github.com/oliveiradg" target="_blank"><img align="center" height="200" src="../images/100daysPython-removebg.png" /></a>
</div>
<br>

</div>
</div>

## Dia 12: 
<br>

<br>

####Programação Orientada a Objetos

<br>
Na lição de hoje, aprendi sobre a Programação Orientada a Objetos (POO) e como implementar objetos usando classes em Python.

Primeiro, entendi que a POO é uma abordagem de programação que visa modelar objetos do mundo real. Esses objetos têm atributos (coisas que eles têm) e métodos (coisas que eles podem fazer). Atributos são como variáveis associadas a um objeto específico, enquanto métodos são funções que um objeto específico pode executar.

Para ilustrar isso, usamos o exemplo de um restaurante virtual. Modelamos um objeto "Garçom" e identificamos seus atributos, como "segurando uma bandeja" e "responsável por determinadas mesas". Também identificamos seus métodos, como "enviar um pedido para a cozinha" e "receber pagamentos". A classe "Garçom" é o projeto que define esses atributos e métodos, e os objetos individuais gerados a partir dessa classe são as instâncias reais, como "Henry" ou "Betty".

Em seguida, aprendi como criar objetos a partir de classes em Python. Para isso, importamos o módulo contendo a classe desejada e usamos a sintaxe de construção para inicializar o objeto. Por exemplo, se tivermos uma classe chamada "Carro", poderíamos criar um objeto chamado "meu_carro" usando a linha de código: "meu_carro = Carro()".

Também explorei como acessar os atributos de um objeto, usando a notação de ponto para separar o objeto do atributo desejado. Por exemplo, se quisermos obter a velocidade de um objeto "carro", podemos usar "carro.velocidade".

Além disso, aprendi sobre os métodos de um objeto, que são funções associadas a ele. Novamente, usamos a notação de ponto para chamar um método em um objeto. Por exemplo, se tivermos um objeto "tartaruga" e quisermos fazê-lo avançar, podemos usar "tartaruga.avancar(distancia)".

Para aplicar esses conceitos, utilizei a biblioteca "turtle" em Python. Importei o módulo "turtle" e criei um objeto "timmy" a partir da classe "turtle.Turtle()". Em seguida, explorei alguns atributos e métodos disponíveis, como alterar a cor e a forma da tartaruga, movê-la pelo espaço e exibir a janela gráfica onde a tartaruga é desenhada.

No geral, aprendi que a POO permite modelar objetos do mundo real em código, combinando atributos e métodos em classes. Essas classes servem como projetos para gerar objetos reais. Utilizando esses objetos, podemos acessar seus atributos e chamar seus métodos para realizar várias ações.

<br>
Alguns exemplos práticos para ilustrar a implementação de objetos usando classes em Python.

Exemplo 1: Classe "Pessoa"
~~~python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
~~~
Neste exemplo, temos uma classe chamada "Pessoa" que possui os atributos "nome" e "idade". O método __init__ é o construtor da classe e é responsável por inicializar os atributos do objeto quando ele é criado. O método saudacao é um método simples que imprime uma saudação com o nome e idade da pessoa.

Agora, podemos criar objetos a partir dessa classe e acessar seus atributos e métodos:
~~~python
pessoa1 = Pessoa("João", 25)
pessoa1.saudacao()  # Saída: "Olá, meu nome é João e tenho 25 anos."

pessoa2 = Pessoa("Maria", 30)
pessoa2.saudacao()  # Saída: "Olá, meu nome é Maria e tenho 30 anos."
~~~
No exemplo acima, criamos dois objetos (pessoa1 e pessoa2) a partir da classe "Pessoa" e definimos valores diferentes para seus atributos. Em seguida, chamamos o método saudacao() para cada objeto, que imprime uma saudação personalizada.

Exemplo 2: Classe "Círculo"
~~~python
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
~~~
Neste exemplo, temos uma classe chamada "Circulo" que possui o atributo "raio". A classe também tem dois métodos: calcular_area() para calcular a área do círculo e calcular_perimetro() para calcular o perímetro do círculo usando a fórmula matemática adequada.

Podemos criar objetos a partir dessa classe e usar seus métodos para realizar cálculos:

~~~python
circulo1 = Circulo(5)
area = circulo1.calcular_area()
perimetro = circulo1.calcular_perimetro()
print(f"Área do círculo: {area:.2f}")  # Saída: "Área do círculo: 78.54"
print(f"Perímetro do círculo: {perimetro:.2f}")  # Saída: "Perímetro do círculo: 31.42"

circulo2 = Circulo(3)
area = circulo2.calcular_area()
perimetro = circulo2.calcular_perimetro()
print(f"Área do círculo: {area:.2f}")  # Saída: "Área do círculo: 28.27"
print(f"Perímetro do círculo: {perimetro:.2f}")  # Saída: "Perímetro do círculo: 18.85"
~~~
No exemplo acima, criamos dois objetos (circulo1 e circulo2) a partir da classe "Circulo" e definimos diferentes valores para o atributo "raio". Em seguida, chamamos os métodos calcular_area() e calcular_perimetro() para cada objeto, calculando a área e o perímetro dos círculos correspondentes.

Esses exemplos demonstram como criar objetos a partir de classes e como acessar seus atributos e métodos para realizar diferentes ações. Através da POO, podemos modelar e manipular objetos de forma eficiente e modular em nossos programas.



<br>
<br>
<br>
Feito com ❤ para os #100daysOfPython 
<br>
<br>

<a href="../readme.md">Página Inicial</a> 