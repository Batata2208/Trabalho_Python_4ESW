import os
import sqlite3 as con

sql_Processos = """
    CREATE TABLE IF NOT EXISTS processos (
        id_processo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_criacao DATE DEFAULT CURRENT_TIMESTAMP,
        funcionario TEXT NOT NULL,
        tempo_criacao INTEGER NOT NULL
    );
"""

sql_Pecas = """
    CREATE TABLE IF NOT EXISTS Pecas (
        id_peca INTEGER PRIMARY KEY AUTOINCREMENT,
        id_processo INTEGER,
        nome_processo TEXT NOT NULL,
        tempo_gasto INTEGER NOT NULL,
        data_criacao DATE DEFAULT CURRENT_TIMESTAMP,
        funcionario TEXT NOT NULL,
        valor_total_da_peça DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (id_processo) REFERENCES processos (id_processo)
    );
"""

sql_Funcionario = """
    CREATE TABLE IF NOT EXISTS Funcionario (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        data_admissao DATE DEFAULT CURRENT_TIMESTAMP,
        salario DECIMAL(10, 2) NOT NULL,
        cargo TEXT NOT NULL
    );
"""

sql_historico = """
    CREATE TABLE IF NOT EXISTS historico (
        id_historico INTEGER PRIMARY KEY AUTOINCREMENT,
        id_peca INTEGER,
        id_funcionario INTEGER,
        data DATE DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_funcionario) REFERENCES Funcionario (id_funcionario),
        FOREIGN KEY (id_peca) REFERENCES Pecas (id_peca)
    );
"""

sql_Usuario_Padrao = """
    INSERT INTO Funcionario (nome, senha, salario, cargo) VALUES ('admin', 'admin123', 1000, 'Administrador');
"""

#criar banco de dados e a conexão com o banco de dados
def criar_banco():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute(sql_Pecas)
        cur.execute(sql_Processos)
        cur.execute(sql_Funcionario)
        cur.execute(sql_historico)
        cur.execute(sql_Usuario_Padrao)
        
        conexao.commit()

    except con.DatabaseError as erro:
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


#Processos

#inserir dados na tabela processos
def inserir_processo(nome, funcionario, tempo_criacao):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO processos (nome, funcionario, tempo_criacao) VALUES (?, ?, ?)", (nome, funcionario, tempo_criacao))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao inserir processo:", erro)
    finally:
        if conexao:
            conexao.close()


#atualizar dados na tabela processos
def atualizar_processo(nome, funcionario, tempo_criacao):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("UPDATE processos SET funcionario = ?, tempo_criacao = ? WHERE nome = ?", (funcionario, tempo_criacao, nome))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao atualizar processo:", erro)
    finally:
        if conexao:
            conexao.close()


#deletar dados na tabela processos
def deletar_processo(nome):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("DELETE FROM processos WHERE nome = ?", (nome,))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao deletar processo:", erro)
    finally:
        if conexao:
            conexao.close()


#verificar se o processo existe
def verifica_processo(nome):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        # Consulta para verificar se o processo existe
        cur.execute("SELECT COUNT(*) FROM processos WHERE nome = ?", (nome))
        resultado = cur.fetchone()[0]

        return resultado > 0  # Retorna True se existir, False se não existir

    except con.DatabaseError as erro:
        print("Erro ao verificar processo:", erro)
        return False
    finally:
        if conexao:
            conexao.close()



#listar os processos
def Lista_Processos():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("SELECT * FROM processos")
        resultado = cur.fetchall()

        return resultado

    except con.DataBaseError as erro:
        print("Erro ao listar processos:", erro)
        return []
    finally:
        if conexao:
            conexao.close()


#Pecas

#inserir dados na tabela peca
def inserir_peca(id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peça):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO Pecas (id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peça) VALUES (?, ?, ?, ?, ?)", 
                    (id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peça))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao inserir peça:", erro)
    finally:
        if conexao:
            conexao.close()

#Verificar se a peça existe
def verifica_peca(nome_peca):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        # Consulta para verificar se a peça existe
        cur.execute("SELECT COUNT(*) FROM Pecas WHERE nome_processo = ?", (nome_peca))
        resultado = cur.fetchone()[0]

        return resultado > 0  # Retorna True se existir, False se não existir

    except con.DatabaseError as erro:
        print("Erro ao verificar peça:", erro)
        return False
    finally:
        if conexao:
            conexao.close()

#deletar peça 
def deletar_peca(nome_peca):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("DELETE FROM Pecas WHERE nome_processo = ?", (nome_peca,))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao deletar peça:", erro)
    finally:
        if conexao:
            conexao.close()

#atualizar peça
def atualizar_peca(id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peça):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("UPDATE Pecas SET id_processo = ?, tempo_gasto = ?, funcionario = ?, valor_total_da_peça = ? WHERE nome_processo = ?", 
                    (id_processo, tempo_gasto, funcionario, valor_total_da_peça, nome_processo))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao atualizar peça:", erro)
    finally:
        if conexao:
            conexao.close() 

#listar as peças
def Lista_Pecas():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("SELECT * FROM Pecas")
        resultado = cur.fetchall()

        return resultado

    except con.DataBaseError as erro:
        print("Erro ao listar peças:", erro)
        return []
    finally:
        if conexao:
            conexao.close()



#Funcionarios

#inserir funcionario novo
def inserir_funcionario(nome, senha, salario, cargo):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO Funcionario (nome, senha, salario, cargo) VALUES (?, ?, ?, ?)", (nome, senha, salario, cargo))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao inserir funcionário:", erro)
    finally:
        if conexao:
            conexao.close()

#Verifica se o funcionário existe
def verifica_funcionario(nome_funcionario, senha_funcionario):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        # Consulta para verificar se o funcionário existe
        cur.execute("SELECT COUNT(*) FROM Funcionario WHERE nome = ? AND senha = ?", (nome_funcionario,senha_funcionario))
        resultado = cur.fetchone()[0]

        return resultado > 0  # Retorna True se existir, False se não existir

    except con.DatabaseError as erro:
        print("Erro ao verificar funcionário:", erro)
        return False
    finally:
        if conexao:
            conexao.close()

#atualizar funcionário
def atualizar_funcionario(nome, senha, salario, cargo):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("UPDATE Funcionario SET senha = ?, salario = ?, cargo = ? WHERE nome = ?", (senha, salario, cargo, nome))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao atualizar funcionário:", erro)
    finally:
        if conexao:
            conexao.close()

#deletar funcionário
def deletar_funcionario(nome_funcionario):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("DELETE FROM Funcionario WHERE nome = ?", (nome_funcionario,))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao deletar funcionário:", erro)
    finally:
        if conexao:
            conexao.close()
            

#listar os funcionários
def Lista_Funcionarios():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("SELECT * FROM Funcionario")
        resultado = cur.fetchall()

        return resultado

    except con.DataBaseError as erro:
        print("Erro ao listar funcionários:", erro)
        return []
    finally:
        if conexao:
            conexao.close()



#hitórico

#inserir no Histórico
def inserir_historico(id_peca, id_funcionario):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO historico (id_peca, id_funcionario) VALUES (?, ?)", (id_peca, id_funcionario))
        conexao.commit()
    except con.DatabaseError as erro:
        print("Erro ao inserir histórico:", erro)
    finally:
        if conexao:
            conexao.close()

#listar o histórico
def Lista_Historico():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("SELECT * FROM historico")
        resultado = cur.fetchall()

        return resultado

    except con.DataBaseError as erro:
        print("Erro ao listar histórico:", erro)
        return []
    finally:
        if conexao:
            conexao.close()