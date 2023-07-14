# importando sqlite
import sqlite3 as sql

# criando conexão

conexao = sql.connect('my_book_shelf.db')

# criando tabela
with conexao:
    controle = conexao.cursor()
    controle.execute("CREATE TABLE mybookshelf(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT , genero TEXT , autor TEXT , saga TEXT, ano DATE, editora TEXT , lido_monica TEXT, lido_joao TEXT , imagem TEXT) ")
