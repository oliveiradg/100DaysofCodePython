# importando sqlite
import sqlite3 as sql

# criando conexão

conexao = sql.connect('my_book_shelf.db')

# criando tabela
with conexao:
    controle = conexao.cursor()
    controle.execute("CREATE TABLE mybookshelf(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, genero TEXT NOT NULL, autor TEXT NOT NULL, saga TEXT, editora TEXT NOT NULL, lido_monica TEXT NOT NULL, lido_joao TEXT NOT NULL, imagem TEXT NOT NULL)")



