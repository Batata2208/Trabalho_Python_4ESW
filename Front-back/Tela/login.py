import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import sys  # Importando sys para finalizar o programa
import Banco_de_dados as bd

DB_PATH = os.path.join(os.path.dirname(__file__), 'Banco_Oficial.db')
bd.verifica_banco(DB_PATH)
#caminho_relativo = 'logo.ico'
#caminho_absoluto = os.path.abspath(caminho_relativo).replace("\\", "/")
caminho_absoluto = "C:/Users/Usuário/Desktop/Python/Trabalho_Python_4ESW-main final/logo.ico"

def centralizar_janela(root):
    root.update_idletasks()  # Atualiza as informações da janela

    # Obter largura e altura da janela
    largura_janela = root.winfo_width()
    altura_janela = root.winfo_height()

    # Obter largura e altura da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular posição para centralizar
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Definir geometria
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

def configurar_fechar_janela(janela):
    janela.protocol("WM_DELETE_WINDOW", lambda: fechar_programa(janela))
    
# Função para fechar o programa
def fechar_programa(root):
    resposta = messagebox.askquestion("Confirmar", "Deseja realmente fechar o programa?")
    if resposta == "yes":
        root.destroy()  # Destroi a janela e libera os recursos
        sys.exit()  # Encerra o programa completamente
        
# Função para iniciar a tela de login
def iniciar_tela_login():
    login = tk.Tk()
    login.title("Tela de Login")
    login.geometry("400x300")  # Coloca a janela no modo maximizado
    login.iconbitmap(caminho_absoluto) #coloco a logo
    login.config(bg="#f4f4f4")
    login.after(10,lambda: centralizar_janela(login))

    tk.Label(login, text="Nome de Usuário:", font=("Arial", 14), bg="#f4f4f4").pack(pady=10)
    nome_usuario = tk.Entry(login, font=("Arial", 14))
    nome_usuario.pack(pady=10)

    tk.Label(login, text="Senha:", font=("Arial", 14), bg="#f4f4f4").pack(pady=10)
    senha_usuario = tk.Entry(login, show="*", font=("Arial", 14))
    senha_usuario.pack(pady=10)

    def verificar_login():
        nome = nome_usuario.get()
        senha = senha_usuario.get()

        # Conectar ao banco de dados
        conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
        cursor = conexao.cursor()

        try:
            # Verifica no banco de dados o nome e senha fornecidos
            cursor.execute("SELECT * FROM Funcionario WHERE nome = ? AND senha = ?", (nome, senha))
            resultado = cursor.fetchone()  # Retorna uma linha do banco ou None se não encontrar

            if resultado:
                # Verifica se o campo 'cargo' está presente e identifica o perfil
                cargo = resultado[5]  # Considerando que o cargo está na posição 5
                if cargo == "Administrador":
                    login.destroy()  # Fecha a tela de login
                    abrir_painel_administrador()  # Abre o painel do administrador
                elif cargo == "Funcionário":
                    login.destroy()  # Fecha a tela de login
                    abrir_painel_funcionario()  # Abre o painel do funcionário
                else:
                    # Exibe erro caso o cargo não seja reconhecido
                    messagebox.showerror("Erro", "Cargo desconhecido. Entre em contato com o administrador do sistema.")
            else:
                # Caso o usuário ou senha não sejam encontrados
                messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
        except sqlite3.OperationalError as erro:
            # Trata erros de operações no banco de dados (ex.: problema de conexão, tabela inexistente)
            messagebox.showerror("Erro", f"Erro na operação com o banco de dados: {erro}")
        except sqlite3.DatabaseError as erro:
            # Trata erros gerais do banco de dados
            messagebox.showerror("Erro", f"Erro no banco de dados: {erro}")
        finally:
            # Garante que a conexão com o banco será encerrada
            if conexao:
                conexao.close()

    tk.Button(login, text="Entrar", command=verificar_login, font=("Arial", 14), bg="#4CAF50", fg="white", width=20, height=2).pack(pady=20)

    # Configurar botão e funcionalidade de fechar
    configurar_fechar_janela(login)

    login.mainloop()

# Função para criar o painel do Administrador
def abrir_painel_administrador():
    painel_admin = tk.Tk()
    painel_admin.title("Painel do Administrador")
    painel_admin.geometry("800x600")  # Coloca a janela
    painel_admin.iconbitmap(caminho_absoluto) #coloco a logo  
    painel_admin.config(bg='#e0e0e0')  # Cor de fundo suave
    painel_admin.after(10,lambda: centralizar_janela(painel_admin))

    # Labels e botões com fonte maior
    tk.Label(painel_admin, text="Bem-vindo, Administrador!", font=("Arial", 24), bg='#e0e0e0').pack(pady=20)

    tk.Button(painel_admin, text="Cadastrar Funcionário", command=lambda: cadastrar_funcionario(painel_admin), font=("Arial", 18), bg="#2196F3", fg="white", width=20, height=2).pack(pady=20)
    tk.Button(painel_admin, text="Excluir Funcionário", command=lambda: excluir_funcionario(painel_admin), font=("Arial", 18), bg="#f44336", fg="white", width=20, height=2).pack(pady=20)
    tk.Button(painel_admin, text="Relatório", command=lambda: abrir_relatorio(painel_admin), font=("Arial", 18), bg="#8E44AD", fg="white", width=20, height=2).pack(pady=20)
    tk.Button(painel_admin, text="Logout", command=lambda: [painel_admin.destroy(), iniciar_tela_login()], font=("Arial", 18), bg="#f44336", fg="white", width=20, height=2).pack(pady=20)
    # Configurar botão e funcionalidade de fechar
    configurar_fechar_janela(painel_admin)

    painel_admin.mainloop()

# Função para cadastrar funcionário
def cadastrar_funcionario(painel_admin):
    painel_admin.withdraw()  # Esconde o painel de administrador
    
    cadastro = tk.Tk()
    cadastro.title("Cadastrar Funcionário")
    cadastro.geometry("800x600")  # Coloca a janela no modo maximizado
    cadastro.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    cadastro.config(bg='#f4f4f4')  # Cor de fundo suave
    cadastro.after(10,lambda: centralizar_janela(cadastro))

    # Campos de entrada para cadastro de funcionário
    tk.Label(cadastro, text="Nome:", font=("Arial", 18), bg='#f4f4f4').pack(pady=10)
    entrada_nome = tk.Entry(cadastro, font=("Arial", 16))
    entrada_nome.pack(pady=10)

    tk.Label(cadastro, text="Senha:", font=("Arial", 18), bg='#f4f4f4').pack(pady=10)
    entrada_senha = tk.Entry(cadastro, show="*", font=("Arial", 16))
    entrada_senha.pack(pady=10)

    tk.Label(cadastro, text="Cargo:", font=("Arial", 18), bg='#f4f4f4').pack(pady=10)
    var_cargo = tk.StringVar(cadastro)
    var_cargo.set("Funcionário")  # Default
    entrada_cargo = tk.OptionMenu(cadastro, var_cargo, "Administrador", "Funcionário")
    entrada_cargo.config(font=("Arial", 16))
    entrada_cargo.pack(pady=10)

    tk.Label(cadastro, text="Salário:", font=("Arial", 18), bg='#f4f4f4').pack(pady=10)
    entrada_salario = tk.Entry(cadastro, font=("Arial", 16))
    entrada_salario.pack(pady=10)

    def salvar_funcionario():
        nome = entrada_nome.get()
        senha = entrada_senha.get()
        cargo = var_cargo.get()
        salario = entrada_salario.get()

        if not nome or not senha or not salario:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        # Salvar no banco
        conexao = None
        try:
            conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Funcionario (nome, senha, cargo, salario) VALUES (?, ?, ?, ?)", 
                           (nome, senha, cargo, salario))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        
        except sqlite3.DatabaseError as erro:
            messagebox.showerror("Erro", f"Erro ao cadastrar funcionário: {erro}")
        finally:
            if conexao:
                conexao.close()
            
    # Botão para salvar o novo funcionário
    tk.Button(cadastro, text="Cadastrar", command=salvar_funcionario, font=("Arial", 18), bg="#4CAF50", fg="white", width=20, height=2).pack(pady=20)

    # Botão "Voltar" para voltar ao painel de administrador
    tk.Button(cadastro, text="Voltar", command=lambda: [cadastro.destroy(), abrir_painel_administrador()], font=("Arial", 16), bg="#FFC107", fg="white", width=20, height=2).pack(pady=10)

    configurar_fechar_janela(cadastro)

    cadastro.mainloop()

# Função para excluir funcionário
def excluir_funcionario(painel_admin):
    painel_admin.withdraw()  # Esconde o painel de administrador

    excluir = tk.Tk()
    excluir.title("Excluir Funcionário")
    excluir.geometry("800x600")  # Coloca a janela no modo maximizado
    excluir.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    excluir.config(bg='#f4f4f4')  # Cor de fundo suave
    excluir.after(10,lambda: centralizar_janela(excluir))

    # Consultar funcionários no banco
    conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM Funcionario")
    funcionarios = cursor.fetchall()

    tk.Label(excluir, text="Escolha um Funcionário para excluir:", font=("Arial", 16), bg='#f4f4f4').pack(pady=20)

    # Menu suspenso para escolher o funcionário
    var_funcionario = tk.StringVar(excluir)
    var_funcionario.set(funcionarios[0][0] if funcionarios else "")  # Definir um valor inicial se houver funcionários
    menu_funcionarios = tk.OptionMenu(excluir, var_funcionario, *[f[0] for f in funcionarios])
    menu_funcionarios.config(font=("Arial", 14))
    menu_funcionarios.pack(pady=20)

    def excluir_funcionario_do_banco():
        nome_funcionario = var_funcionario.get()

        if not nome_funcionario:
            messagebox.showerror("Erro", "Nenhum funcionário selecionado!")
            return

        cursor.execute("DELETE FROM Funcionario WHERE nome = ?", (nome_funcionario,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")        

    # Botão para excluir o funcionário
    tk.Button(excluir, text="Excluir Funcionário", command=excluir_funcionario_do_banco, font=("Arial", 18), bg="#f44336", fg="white", width=20, height=2).pack(pady=20)

    # Botão "Voltar"
    tk.Button(excluir, text="Voltar", command=lambda: [excluir.destroy(), abrir_painel_administrador()], font=("Arial", 16), bg="#FFC107", fg="white", width=20, height=2).pack(pady=10)

    configurar_fechar_janela(excluir)

# Painel Relatório
def abrir_relatorio(painel_admin):
    painel_admin.withdraw()  # Esconde o painel de administrador

    # Cria a nova janela para o relatório
    relatorio_window = tk.Tk()
    relatorio_window.title("Relatório de Peças e Processos")
    relatorio_window.geometry("1300x800")  # Coloca a janela no modo maximizado
    relatorio_window.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    relatorio_window.config(bg='#f4f4f4')
    relatorio_window.after(10,lambda: centralizar_janela(relatorio_window))

    # Conectar ao banco de dados para pegar os dados
    conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
    cursor = conexao.cursor()

    # SQL para buscar os dados do relatório
    sql = """
    SELECT 
        p.id_peca, p.id_processo, p.nome_processo, p.funcionario, 
        p.tempo_gasto, p.data_criacao, p.valor_total_da_peca
    FROM Pecas p
    JOIN processos pr ON p.id_processo = pr.id_processo
    """

    try:
        cursor.execute(sql)
        dados_relatorio = cursor.fetchall()

        # Criar o cabeçalho da tabela
        cabecalho = ["ID da Peça", "ID do Processo", "Nome do Processo", "Funcionário", "Tempo Gasto", "Data de Criação", "Valor Total"]
        for j, header in enumerate(cabecalho):
            tk.Label(relatorio_window, text=header, font=("Arial", 14, "bold"), relief="solid", width=20, height=2).grid(row=0, column=j, sticky="nsew")

        # Ajustar as colunas para garantir que todas tenham a mesma largura
        for col in range(len(cabecalho)):
            relatorio_window.grid_columnconfigure(col, weight=1, uniform="equal")

        # Criar as linhas da tabela com os dados
        for i, row in enumerate(dados_relatorio):
            for j, value in enumerate(row):
                tk.Label(relatorio_window, text=value, font=("Arial", 12), relief="solid", width=20, height=2).grid(row=i+1, column=j, sticky="nsew")

        # Configurar a linha da grade para o botão "Voltar" e posicioná-lo na parte inferior
        relatorio_window.grid_rowconfigure(len(dados_relatorio) + 1, weight=1)  # Para permitir que o botão fique na parte inferior
        relatorio_window.grid_rowconfigure(len(dados_relatorio) + 2, weight=0)  # A linha do botão
        relatorio_window.grid_columnconfigure(0, weight=1)  # Para centralizar o botão horizontalmente

        # Botão para voltar ao painel de administrador, posicionado na parte inferior
        tk.Button(relatorio_window, text="Voltar", command=lambda: [relatorio_window.destroy(), abrir_painel_administrador()], font=("Arial", 16), bg="#FFC107", fg="white", width=20, height=2).grid(row=len(dados_relatorio) + 2, column=0, columnspan=7, pady=20)

    except sqlite3.DatabaseError as erro:
        messagebox.showerror("Erro", f"Erro ao buscar dados: {erro}")
    finally:
        if conexao:
            conexao.close()



    configurar_fechar_janela(relatorio_window)
    relatorio_window.mainloop()

def abrir_painel_funcionario():
    # Criação da janela principal do painel
    painel_funcionario = tk.Tk()
    painel_funcionario.title("Painel do Funcionário")
    painel_funcionario.geometry("800x600")  # Coloca a janela no modo maximizado
    painel_funcionario.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    painel_funcionario.config(bg="#f4f4f4")  # Fundo da tela
    painel_funcionario.after(10,lambda: centralizar_janela(painel_funcionario))

    # Adicionar título ao painel
    titulo = tk.Label(
        painel_funcionario,
        text="Bem-vindo ao Painel do Funcionário",
        font=("Arial", 24, "bold"),
        bg="#f4f4f4",
        fg="#333"
    )
    titulo.pack(pady=50)

    # Botão para acessar o registro de processos
    tk.Button(
        painel_funcionario,
        text="Processo",
        command=lambda: [painel_funcionario.withdraw(), abrir_tela_processo(painel_funcionario)],
        font=("Arial", 18),
        bg="#4CAF50",
        fg="white",
        width=20,  # Define a largura do botão
        height=2    # Define a altura do botão
    ).pack(pady=20)

    # Botão para listar os processos
    tk.Button(
        painel_funcionario,
        text="Listar Processos",
        command=lambda: [painel_funcionario.withdraw(), abrir_lista_processos()],
        font=("Arial", 18),
        bg="#8E44AD",  # Cor roxa para o botão
        fg="white",
        width=20,  # Define a largura do botão
        height=2    # Define a altura do botão
    ).pack(pady=20)


    # Botão para registrar peças
    tk.Button(
        painel_funcionario,
        text="Peças",
        command=lambda: [painel_funcionario.destroy(), abrir_tela_pecas()],
        font=("Arial", 18),
        bg="#2196F3",
        fg="white",
        width=20,  # Define a largura do botão
        height=2    # Define a altura do botão
    ).pack(pady=20)

    tk.Button(painel_funcionario, text="Logout", command=lambda: [painel_funcionario.destroy(), iniciar_tela_login()], font=("Arial", 18), bg="#f44336", fg="white", width=20, height=2).pack(pady=20)

    configurar_fechar_janela(painel_funcionario)

# Função para abrir a tela de registro de processos
def abrir_tela_processo(painel_funcionario):
    tela_processo = tk.Tk()
    tela_processo.title("Registro de Processos")
    tela_processo.geometry("800x600")  # Coloca a janela no modo maximizado
    tela_processo.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    tela_processo.config(bg="#f4f4f4")  # Fundo da tela
    tela_processo.after(10,lambda: centralizar_janela(tela_processo))

    # Campos para registro do processo
    tk.Label(tela_processo, text="Descrição do processo:", font=("Arial", 18), bg="#f4f4f4").pack(pady=10)
    entrada_nome_processo = tk.Entry(tela_processo, font=("Arial", 16))
    entrada_nome_processo.pack(pady=10)

    tk.Label(tela_processo, text="Funcionário Responsável:", font=("Arial", 18), bg="#f4f4f4").pack(pady=10)
    entrada_funcionario = tk.Entry(tela_processo, font=("Arial", 16))
    entrada_funcionario.pack(pady=10)

    tk.Label(tela_processo, text="Tempo de Criação (em horas):", font=("Arial", 18), bg="#f4f4f4").pack(pady=10)
    entrada_tempo_criacao = tk.Entry(tela_processo, font=("Arial", 16))
    entrada_tempo_criacao.pack(pady=10)

    # Função para salvar o processo no banco de dados
    def salvar_processo():
        nome = entrada_nome_processo.get()
        funcionario = entrada_funcionario.get()
        tempo_criacao = entrada_tempo_criacao.get()

        if not nome or not funcionario or not tempo_criacao:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            tempo_criacao = int(tempo_criacao)  # Garantir que é um número
        except ValueError:
            messagebox.showerror("Erro", "O tempo de criação deve ser um número válido!")
            return

        # Salvar no banco de dados
        conexao = None
        try:
            conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO processos (nome, funcionario, tempo_criacao) VALUES (?, ?, ?)",
                (nome, funcionario, tempo_criacao)
            )
            conexao.commit()
            messagebox.showinfo("Sucesso", "Processo registrado com sucesso!")
        except sqlite3.DatabaseError as erro:
            messagebox.showerror("Erro", f"Erro ao registrar o processo: {erro}")
        finally:
            if conexao:
                conexao.close()

    # Botão para salvar
    tk.Button(
        tela_processo,
        text="Registrar Processo",
        command=salvar_processo,
        font=("Arial", 18),
        bg="#4CAF50",
        fg="white"
    ).pack(pady=20)

    # Botão "Voltar" para o painel do funcionário
    tk.Button(
        tela_processo,
        text="Voltar",
        command=lambda: [tela_processo.destroy(), abrir_painel_funcionario()],
        font=("Arial", 16),
        bg="#FFC107",
        fg="white"
    ).pack(pady=10)

    configurar_fechar_janela(tela_processo)
    tela_processo.mainloop()


    tk.Button(painel_funcionario, text="Logout", command=lambda: [painel_funcionario.destroy(), iniciar_tela_login()], font=("Arial", 18), bg="#f44336", fg="white").pack(pady=20)

    # Configurar botão e funcionalidade de fechar
    configurar_fechar_janela(painel_funcionario)

# Função para abrir a tela de registro de peças
def abrir_tela_pecas():
    tela_pecas = tk.Tk()
    tela_pecas.title("Registrar Peças")
    tela_pecas.geometry("700x700")  # Coloca a janela no modo maximizado
    tela_pecas.iconbitmap(caminho_absoluto) #coloco a logo  # Coloca a janela no modo maximizado
    tela_pecas.config(bg="#f4f4f4")  # Fundo da tela
    tela_pecas.after(10,lambda: centralizar_janela(tela_pecas))
    
    tk.Label(tela_pecas, text="Registro de Peças", font=("Arial", 24), bg="#f4f4f4").pack(pady=20)

    # Campos para o registro
    tk.Label(tela_pecas, text="ID do Processo:", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)
    entrada_id_processo = tk.Entry(tela_pecas, font=("Arial", 14))
    entrada_id_processo.pack(pady=10)

    tk.Label(tela_pecas, text="Nome do Processo:", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)
    entrada_nome_processo = tk.Entry(tela_pecas, font=("Arial", 14))
    entrada_nome_processo.pack(pady=10)

    tk.Label(tela_pecas, text="Tempo Gasto (horas):", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)
    entrada_tempo_gasto = tk.Entry(tela_pecas, font=("Arial", 14))
    entrada_tempo_gasto.pack(pady=10)

    tk.Label(tela_pecas, text="Funcionário Responsável:", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)
    entrada_funcionario = tk.Entry(tela_pecas, font=("Arial", 14))
    entrada_funcionario.pack(pady=10)

    tk.Label(tela_pecas, text="Valor Total da Peça (R$):", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)
    entrada_valor_total_da_peca = tk.Entry(tela_pecas, font=("Arial", 14))
    entrada_valor_total_da_peca.pack(pady=10)

    def salvar_peca():
        # Obtendo os valores dos campos
        id_processo = entrada_id_processo.get()
        nome_processo = entrada_nome_processo.get()
        tempo_gasto = entrada_tempo_gasto.get()
        funcionario = entrada_funcionario.get()
        valor_total = entrada_valor_total_da_peca.get()

        # Validação dos campos
        if not id_processo or not nome_processo or not tempo_gasto or not funcionario or not valor_total:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        # Conectar ao banco e salvar os dados
        try:
            conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
            cursor = conexao.cursor()

            # Verificar se o ID do processo existe
            cursor.execute("SELECT COUNT(*) FROM processos WHERE id_processo = ?", (id_processo,))
            processo_existe = cursor.fetchone()[0]

            if processo_existe == 0:
                messagebox.showerror("Erro", "ID do Processo não encontrado. Verifique o valor inserido.")
                return
            
             # Inserir os dados na tabela Pecas
            cursor.execute("""
            INSERT INTO Pecas (id_processo, nome_processo, tempo_gasto, funcionario, valor_total_da_peca)
            VALUES (?, ?, ?, ?, ?)
            """, (id_processo, nome_processo, tempo_gasto, funcionario, valor_total))

            conexao.commit()
            messagebox.showinfo("Sucesso", "Peça registrada com sucesso!")

        except sqlite3.DatabaseError as erro:
            messagebox.showerror("Erro", f"Erro ao registrar a peça: {erro}")
        finally:
            if conexao:
                conexao.close()

    # Botão para salvar a peça
    tk.Button(
        tela_pecas,
        text="Registrar",
        command=salvar_peca,
        font=("Arial", 18),
        bg="#4CAF50",
        fg="white"
    ).pack(pady=20)

    # Botão "Voltar" para retornar ao painel do funcionário
    tk.Button(
        tela_pecas,
        text="Voltar",
        command=lambda: [tela_pecas.destroy(), abrir_painel_funcionario()],
        font=("Arial", 16),
        bg="#FFC107",
        fg="white"
    ).pack(pady=10)

    configurar_fechar_janela(tela_pecas)
    tela_pecas.mainloop()

def abrir_lista_processos():
    # Criação da janela
    tela_lista = tk.Toplevel()  # Usando Toplevel para criar uma nova janela
    tela_lista.title("Lista de Processos")
    tela_lista.geometry("400x300")  # Coloca a janela no modo maximizado
    tela_lista.iconbitmap(caminho_absoluto) #coloco a logo  # Tela maximizada
    tela_lista.config(bg="#f4f4f4")  # Cor de fundo
    tela_lista.after(10,lambda: centralizar_janela(tela_lista))
    
    # Adicionando título
    tk.Label(
        tela_lista,
        text="Lista de Processos",
        font=("Arial", 24),
        bg="#f4f4f4"
    ).pack(pady=20)

    # Frame para a tabela
    frame_tabela = tk.Frame(tela_lista, bg="#f4f4f4")
    frame_tabela.pack(pady=20)

    # Cabeçalho da tabela
    tk.Label(
    frame_tabela,
    text="ID do Processo",
    font=("Arial", 14),
    width=20,
    borderwidth=1,
    relief="solid"
    ).grid(row=0, column=0, sticky="nsew")  # Use sticky para garantir que o texto ocupe toda a largura da célula

    tk.Label(
    frame_tabela,
    text="Nome do Processo",
    font=("Arial", 14),
    width=50,
    borderwidth=1,
    relief="solid"
).grid(row=0, column=1, sticky="nsew")  # Use sticky para garantir que o texto ocupe toda a largura da célula

# Ajuste a configuração da coluna para garantir que as células das colunas se ajustem corretamente
    frame_tabela.grid_columnconfigure(0, weight=1)  # Ajusta a coluna 0 (ID do Processo)
    frame_tabela.grid_columnconfigure(1, weight=3)  # Ajusta a coluna 1 (Nome do Processo) para ter mais largura

    # Conectar ao banco para buscar os processos
    try:
        conexao = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
        cursor = conexao.cursor()
        cursor.execute("SELECT id_processo, nome FROM processos")
        processos = cursor.fetchall()

        # Preencher a tabela com os processos
        for i, processo in enumerate(processos, start=1):
            tk.Label(
                frame_tabela,
                text=processo[0],
                font=("Arial", 12),
                width=20,
                borderwidth=1,
                relief="solid"
            ).grid(row=i, column=0, sticky="nsew")

            tk.Label(
                frame_tabela,
                text=processo[1],
                font=("Arial", 12),
                width=50,
                borderwidth=1,
                relief="solid"
            ).grid(row=i, column=1, sticky="nsew")

    except sqlite3.DatabaseError as erro:
        messagebox.showerror("Erro", f"Erro ao listar processos: {erro}")
    finally:
        if conexao:
            conexao.close()

    # Botão para fechar a janela e voltar ao painel do funcionário
    tk.Button(
        tela_lista,
        text="Voltar",
        command=lambda: [tela_lista.destroy(), abrir_painel_funcionario()],
        font=("Arial", 16),
        bg="#4CAF50",
        fg="white"
    ).pack(pady=20)

    configurar_fechar_janela(tela_lista)
    tela_lista.mainloop()


# Iniciar a tela de login ao rodar o programa
iniciar_tela_login()