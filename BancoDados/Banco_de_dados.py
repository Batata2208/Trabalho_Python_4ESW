import os
import sqlite3 as con

sql_Processos = """
    CREATE TABLE IF NOT EXISTS processos (
        id_processo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_criacao DATE DEFAULT CURRENT_TIMESTAMP,
        funcionario TEXT NOT NULL,
        tempo_criacao INTEGER NOT NULL,
    );
"""

sql_Pecas = """
    CREATE TABLE IF NOT EXISTS Pecas (
        id_processo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_processo INTEGER,
        nome_processo TEXT NOT NULL,
        tempo_gasto INTEGER NOT NULL,
        data_criacao DATE DEFAULT CURRENT_TIMESTAMP,
        funcionario TEXT NOT NULL
        FOREIGN KEY (id_processo) REFERENCES Processo (id_processo)
    );
"""

sql_historico = """
    CREATE TABLE IF NOT EXISTS historico (
        id_historico INTEGER PRIMARY KEY AUTOINCREMENT,
        
    );

"""

#criar banco de dados e a conexão com o banco de dados
def criar_banco():
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
def verificar_tabelas():
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


    
