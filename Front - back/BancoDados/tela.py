import tkinter as tk
from tkinter import messagebox

# Função que será executada quando o botão for clicado
def on_button_click():
    messagebox.showinfo("Informação", "Você clicou no botão!")

# Criando a janela principal
root = tk.Tk()
root.title("Minha Primeira Tela")
root.geometry("300x200")  # Largura x Altura

# Criando um rótulo (texto)
label = tk.Label(root, text="Olá, Mundo!")
label.pack(pady=20)

# Criando um botão
button = tk.Button(root, text="Clique Aqui", command=on_button_click)
button.pack(pady=10)

# Rodando o loop da interface gráfica   
root.mainloop()