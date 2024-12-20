import os
import sqlite3 as con

# SQL para criar as tabelas
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
        valor_total_da_peca DECIMAL(10, 2) NOT NULL,
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

# Inserir usuário administrador
sql_Usuario_Padrao = """
    INSERT INTO Funcionario (nome, senha, salario, cargo) VALUES ('admin', '123456', 10000, 'Administrador');
"""

# Função para criar o banco de dados
def criar_banco():
    try:
        # Conectar ao banco de dados com configurações para evitar bloqueios
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()
        
        # Definir o modo de journal para WAL (Write-Ahead Logging)
        cur.execute("PRAGMA journal_mode=WAL;")
        
        # Configurar o tempo de espera do banco de dados (para caso de bloqueio)
        cur.execute("PRAGMA busy_timeout = 3000;")  # Esperar até 3 segundos

        # Criar as tabelas
        cur.execute(sql_Pecas)
        cur.execute(sql_Processos)
        cur.execute(sql_Funcionario)
        cur.execute(sql_historico)

        # Inserir o usuário administrador (verifique se já não existe para evitar erro)
        cur.execute("SELECT COUNT(*) FROM Funcionario WHERE cargo = 'Administrador';")
        if cur.fetchone()[0] == 0:  # Se não existir, insira o administrador
            cur.execute(sql_Usuario_Padrao)

        # Commit para confirmar as alterações
        conexao.commit()
        print("Banco de dados criado com sucesso e usuário administrador inserido.")
        
    except con.DatabaseError as erro:
        print("Erro ao criar o banco de dados:", erro)
    finally:
        if conexao:
            conexao.close()  # Garante que a conexão seja fechada corretamente

# Função para verificar as tabelas
def verificar_tabelas():
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()
        
        # Definir o modo de journal para WAL
        cur.execute("PRAGMA journal_mode=WAL;")
        
        # Configurar o tempo de espera do banco de dados
        cur.execute("PRAGMA busy_timeout = 3000;")

        # Verificar as tabelas no banco de dados
        res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(res.fetchall())
        
    except con.DatabaseError as erro:
        print("Erro ao verificar as tabelas:", erro)
    finally:
        if conexao:
            conexao.close()  # Garante que a conexão seja fechada corretamente

# Chama a função para criar o banco de dados e inserir o administrador
criar_banco()

# Chama a função para verificar as tabelas
verificar_tabelas()

# Verifica se o banco de dados existe
def verifica_banco(verifica):
    if verifica == False:
        criar_banco()

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
def inserir_peca(id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peca):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("INSERT INTO Pecas (id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peca) VALUES (?, ?, ?, ?, ?)", 
                    (id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peca))
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
def atualizar_peca(id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peca):
    try:
        conexao = con.connect(os.path.join(os.path.dirname(__file__), "Banco_Oficial.db"))
        cur = conexao.cursor()

        cur.execute("UPDATE Pecas SET id_processo = ?, tempo_gasto = ?, funcionario = ?, valor_total_da_peca = ? WHERE nome_processo = ?", 
                    (id_processo, tempo_gasto, funcionario, valor_total_da_peca, nome_processo))
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