from BancoDados import Banco_de_dados as bd
import Serviços as Sr

bd.criar_banco()
bd.verificar_tabelas()

print("Bem vindo a Fênix Confecção Processos!!\n\n")

def opcoes(receber_dados):
    print("Selecione uma das opçoes!!\n\n")
    print("1 - Fazer o Login\n")
    print("0 - Sair do aplicativo\n")
    
    Sr.validar_input(receber_dados)

    if receber_dados == 1:
        Sr.limpar_tela()
        return 
    elif receber_dados == 0:
        Sr.limpar_tela()
        return Sr.encerrar()
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")

def login():

    print("Digite nome do funcionario:\n")
    funcionario = input()
    print("\nDigite sua senha:\n")
    senha = input()
    
    if bd.verifica_funcionario(funcionario, senha) == True:
        print("Login feito com sucesso")
        main()
    else:
        print("Login não realizado")
        

def main():
    print("Bem vindo a Fênix Confecção Processos!!\n\n")
    print("Selecione uma das opçoes!!\n\n")
    print("1 - Processos\n")
    print("2 - Pecas\n")
    print("3 - Funcionarios\n")
    print("4 - Historico\n")
    
    choice = int(input())

    if choice == 1:
        Sr.limpar_tela()
        Processos()
    elif choice == 2:
        Sr.limpar_tela()
        Pecas()
    elif choice == 3:
        Sr.limpar_tela()
        Funcionarios()
    elif choice == 4:
        Sr.limpar_tela()
        Historico()
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")

def Processos():
    print("1 - Cadastrar Processos\n")
    print("2 - Listar Processos\n")
    print("3 - Atualizar Processos\n")
    print("4 - Deletar Processos\n")

    choice = int(input())
    
    if choice == 1:
        print("Digite o nome do processo:\n")
        nome = input()
        print("\nDigite o nome do funcionario:\n")
        funcionario = input()
        print("\nDigite o tempo de criação:\n")
        tempo_criacao = input()
        
        bd.inserir_processo(nome, funcionario, tempo_criacao)
   
    elif choice == 2:
        print("Listando processos...\n")
        processos = bd.listar_processos()
        for processo in processos:
            print(processo)
        
    elif choice == 3:
        print("Atualizar processo\n")
        try:
            print("Digite o novo nome do processo:\n")
            nome = input()
            print("Digite o novo nome do funcionario:\n")
            funcionario = input()
            print("Digite o novo tempo de criação:\n")
            tempo_criacao = input()

            bd.atualizar_processo(nome, funcionario, tempo_criacao)
        except:
            print("Erro ao atualizar processo")
    
    elif choice == 4:
        print("Deletando processo...\n")
        print("Digite o nome do processo:\n")
        nome = input()
        
        bd.deletar_processo(nome)
        
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")

def Pecas():
    print("1 - Cadastrar Pecas\n")
    print("2 - Listar Pecas\n")
    print("3 - Atualizar Pecas\n")
    print("4 - Deletar Pecas\n")

    choice = int(input())
    
    if choice == 1:
        print("Digite o nome da peça:\n")
        nome = input()
        print("\nDigite a quantidade:\n")
        quantidade = input()
        
        bd.inserir_peca(nome, quantidade)
   
    elif choice == 2:
        print("Listando peças...\n")
        pecas = bd.listar_pecas()
        for peca in pecas:
            print(peca)
        
    elif choice == 3:
        print("Atualizar peça\n")
        try:
            print("Digite o novo nome da peça:\n")
            nome = input()
            print("Digite a nova quantidade:\n")
            quantidade = input()

            bd.atualizar_peca(nome, quantidade)
        except:
            print("Erro ao atualizar peça")
    
    elif choice == 4:
        print("Deletando peça...\n")
        print("Digite o nome da peça:\n")
        nome = input()
        
        bd.deletar_peca(nome)
        
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")

def Funcionarios():
    print("1 - Cadastrar Funcionarios\n")
    print("2 - Listar Funcionarios\n")
    print("3 - Atualizar Funcionarios\n")
    print("4 - Deletar Funcionarios\n")

    choice = int(input())
    
    if choice == 1:
        print("Digite o nome do funcionario:\n")
        nome = input()
        print("\nDigite a senha:\n")
        senha = input()
        
        bd.inserir_funcionario(nome, senha)
   
    elif choice == 2:
        print("Listando funcionarios...\n")
        funcionarios = bd.listar_funcionarios()
        for funcionario in funcionarios:
            print(funcionario)
        
    elif choice == 3:
        print("Atualizar funcionario\n")
        try:
            print("Digite o novo nome do funcionario:\n")
            nome = input()
            print("Digite a nova senha:\n")
            senha = input()

            bd.atualizar_funcionario(nome, senha)
        except:
            print("Erro ao atualizar funcionario")
    
    elif choice == 4:
        print("Deletando funcionario...\n")
        print("Digite o nome do funcionario:\n")
        nome = input()
        
        bd.deletar_funcionario(nome)
        
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")

def Historico():
    print("Listando historico...\n")
    historico = bd.listar_historico()
    for item in historico:
        print(item)