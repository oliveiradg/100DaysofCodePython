<div align="center">
<a href="https://github.com/oliveiradg" target="_blank"><img align="right" height="100" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" /></a>




<h1>100 Days of Code: The Complete Python Pro Bootcamp</h1>

<h2>Estudo de Desenvolvimento em <br> Python</h2>

<p> Dominando o Python: E criando 100 projetos em 100 dias. 
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

## Dia 06:
<br>
Durante a criação deste programa, adquiri conhecimentos essenciais sobre o uso do banco de dados SQLite e sua integração com o Python. Através da biblioteca `sqlite3`, pude estabelecer uma conexão com o banco de dados, executar consultas e realizar operações de CRUD (Create, Read, Update, Delete) na tabela `mybookshelf`.

Ao estudar o SQLite, aprendi a importar o módulo `sqlite3` e a criar uma conexão utilizando a função `connect()`. Essa conexão permite interagir com o banco de dados, executar consultas e realizar transações.

Com base nessa conexão, implementei várias funções para realizar diferentes operações. A função `inserir_form(i)` permite inserir registros na tabela `mybookshelf`. Ela recebe uma lista `i` contendo os valores dos campos da tabela a serem inseridos. Utilizando o método `execute()`, foi possível executar a consulta SQL e adicionar os dados ao banco de dados.

Para visualizar os dados da tabela, criei a função `exibir_form()`, que retorna todos os registros presentes na tabela `mybookshelf`. Através de uma consulta SQL simples, utilizando o método `fetchall()`, recuperei os dados do banco de dados e os armazenei em uma lista.

A atualização dos registros é realizada pela função `atualizar_form(i)`, que recebe uma lista `i` contendo os novos valores dos campos da tabela, bem como o ID do registro a ser atualizado. Com uma consulta SQL de atualização, foi possível modificar os dados correspondentes ao ID fornecido.

A função `deletar_form(i)` permite excluir registros da tabela `mybookshelf`. Ela recebe o ID do registro a ser excluído e, utilizando uma consulta SQL de exclusão, remove o registro correspondente da tabela.

Além disso, implementei a função `exibir_form_individual(id)` para visualizar um registro específico da tabela `mybookshelf` com base no ID fornecido. Essa função executa uma consulta SQL utilizando uma cláusula `WHERE` para selecionar apenas o registro desejado.

No geral, o estudo realizado ao criar este programa me proporcionou conhecimentos valiosos sobre a integração do SQLite com o Python. Aprendi a estabelecer uma conexão com o banco de dados, executar consultas SQL, realizar operações de CRUD e manipular os dados presentes na tabela `mybookshelf`. Essas habilidades são fundamentais para o desenvolvimento de aplicações que necessitam armazenar e manipular dados persistentes em um banco de dados.






<br>
<br>

Durante a criação deste programa, aprendi a trabalhar com o banco de dados SQLite e implementei as operações básicas de CRUD (Create, Read, Update, Delete).

1. Importação do módulo SQLite: No início do programa, importei o módulo `sqlite3` com o alias `sql` para permitir a interação com o banco de dados SQLite.

2. Criação da conexão: Utilizei a função `connect()` do módulo `sql` para estabelecer uma conexão com o banco de dados. Nesse caso, o banco de dados foi denominado `my_book_shelf.db`.

3. Inserção de dados: Defini a função `inserir_form(i)` para inserir registros na tabela `mybookshelf` do banco de dados. A função recebe uma lista `i` contendo os valores a serem inseridos nas colunas da tabela.

4. Visualização de dados: Implementei a função `exibir_form()` para obter todos os registros da tabela `mybookshelf`. A função executa uma consulta SQL para selecionar todos os campos da tabela e retorna os resultados como uma lista de registros.

5. Atualização de dados: Criei a função `atualizar_form(i)` para atualizar registros na tabela `mybookshelf`. A função recebe uma lista `i` contendo os valores a serem atualizados, bem como o ID do registro a ser modificado.

6. Exclusão de dados: Defini a função `deletar_form(i)` para excluir registros da tabela `mybookshelf`. A função recebe o ID do registro a ser excluído e executa uma consulta SQL para remover o registro correspondente.

7. Visualização de dados individuais: Implementei a função `exibir_form_individual(id)` para obter um registro específico da tabela `mybookshelf` com base no ID fornecido. A função executa uma consulta SQL com uma cláusula `WHERE` para selecionar apenas o registro com o ID especificado.

Esses são os principais pontos relacionados à integração do banco de dados SQLite ao programa. Através do uso dessas funções, é possível realizar operações de inserção, visualização, atualização e exclusão de registros na tabela `mybookshelf`.







<br>
<br>
<br>
Feito com ❤ para os #100daysOfPython 
<br>
<br>

<a href="../readme.md">Página Inicial</a> 