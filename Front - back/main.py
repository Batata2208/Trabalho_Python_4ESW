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
        
    else:
        print("Login não realizado")
        

def main():
    print("Bem vindo a Fênix Confecção Processos!!\n\n")
    print("Selecione uma das opçoes!!\n\n")
    print("1 - Processos\n")
    print("2 - Pecas\n")
    print("3 - Funcionarios\n")
    print("4 - Historico\n")
    
    Choice = input()

    if Choice == 1:
        Sr.limpar_tela()
        Processos()
    elif Choice == 2:
        Sr.limpar_tela()
        #Pecas()
    elif Choice == 3:
        Sr.limpar_tela()
        #Funcionarios()
    elif Choice == 4:
        Sr.limpar_tela()
        #Historico()
    else:
        print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")


def Processos():
    print("1 - Cadastrar Processos\n")
    print("2 - Listar Processos\n")
    print("3 - Atualizar Processos\n")
    print("4 - Deletar Processos\n")

    choice = input()
    
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