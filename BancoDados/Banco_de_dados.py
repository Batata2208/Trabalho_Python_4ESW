import os
import sqlite3 as con

sql_Pecas = """
    CREATE TABLE IF NOT EXISTS Pecas (
        id_peca INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_criacao DATE NOT NULL,
        data_finalizacao DATE
    );
"""

sql_Processos = """
    CREATE TABLE IF NOT EXISTS Processos (
        id_processo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_peca INTEGER,
        nome_processo TEXT NOT NULL,
        tempo_gasto INTEGER NOT NULL,
        data_processo DATE NOT NULL,
        FOREIGN KEY (id_peca) REFERENCES Pecas (id_peca)
    );
"""

#criar banco de dados e a conexão com o banco de dados
try:
    conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
    cur = conexao.cursor()
    
    cur.execute(sql_Pecas)
    cur.execute(sql_Processos)
    conexao.commit()

except con.DataBaseError as erro:
    print("Erro ao criar a tabela:", erro)
finally:
    if conexao:
        conexao.close()

#verifica a criação das tabelas
try:
    conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
    cur = conexao.cursor()

    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchall())
except con.DataBaseError as erro:
    print("Erro ao criar a tabela:", erro)
finally:
    if conexao:
        conexao.close()

#inserir dados na tabela peca
def inserir_peca(nome, data_criacao, data_finalizacao):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO Pecas (nome, data_criacao, data_finalizacao) VALUES (?, ?, ?)", (nome, data_criacao, data_finalizacao))
        conexao.commit()
    except con.DataBaseError as erro:
        print("Erro ao inserir peça:", erro)
    finally:
        if conexao:
            conexao.close()


    
