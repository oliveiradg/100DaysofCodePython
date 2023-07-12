# importando sqlite
import sqlite3 as sql



### CRUD ###

# criando conexão

conexao = sql.connect('my_book_shelf.db')


# INSERINDO DADOS
def inserir_form(i):
    with conexao:
        controle = conexao.cursor()
        query = "INSERT INTO mybookshelf(titulo, genero, autor, ano, saga, editora, lido_monica, lido_joao, imagem) VALUES(?,?,?,?,?,?,?,?,?)"
        controle.execute(query, i)
     
       
 

# VER DADOS

def exibir_form():

    exibir_dados = []

    with conexao:
        controle = conexao.cursor()
        query =  "SELECT * FROM mybookshelf"
        controle.execute(query)



        linhas= controle.fetchall()
        for linhas in linhas:
            exibir_dados.append(linhas)
    return exibir_dados        

   




#ATUALIZAR DADOS


def atualizar_form(i):

    with conexao:
        controle = conexao.cursor()
        query =  "UPDATE mybookshelf SET titulo=?, genero=?, autor=?, saga=?, editora=?, lido_monica=?, lido_joao=?, imagem=? WHERE id=?"
        controle.execute(query,i )

   


# DELETAR DADOS

def deletar_form(i):

    with conexao:
        controle = conexao.cursor()
        query =  "DELETE FROM mybookshelf WHERE id=?"
        controle.execute(query, i)



# VER DADOS INDIVIDUAIS

def exibir_form_individual(id):
    exibir_dados_individuais = []

    with conexao:
        controle = conexao.cursor()
        query =  "SELECT * FROM mybookshelf WHERE id=? "
        controle.execute(query, id)



        linhas= controle.fetchall()
        for linhas in linhas:
            exibir_dados_individuais.append(linhas)