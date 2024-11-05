import os
from . import Banco_de_dados as bd
import sys

def limpar_tela():
    # Limpa a tela usando os comandos apropriados para cada sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def encerrar():
    print("\nAntes de encerrar o aplicativo, certifique-se de salvar as alteraçoes...\n\n")
    print("Selecione uma das opçoes!!\n\n")
    print("1 - Continuar\n")
    print("0 - Encerrar\n")

    receber_dados = input()

    if receber_dados == 1:
        return #chamar função login
    elif receber_dados == 0:
        print("\nEncerrando o programa...")
        sys.exit()

def validar_input(receber_dados):
    while True: 
        try:
            receber_dados = int(input())
            return receber_dados  
        except ValueError:
            print("Entrada inválida!\nPor favor, digite um número inteiro, sem espaços e sem caracteres!!\n")
