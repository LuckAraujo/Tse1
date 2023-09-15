import tkinter as tk

# Função a ser executada quando o primeiro botão for pressionado
def botao1_click():
    print("Botão 1 foi pressionado")

# Função a ser executada quando o segundo botão for pressionado
def botao2_click():
    print("Botão 2 foi pressionado")

# Crie uma janela principal
janela = tk.Tk()
janela.title("Exemplo de Botões")

# Crie os botões
botao1 = tk.Button(janela, text="Botão 1", command=botao1_click)
botao2 = tk.Button(janela, text="Botão 2", command=botao2_click)
botao3 = tk.Button(janela, text="Botão 3", command=botao1_click)
botao4 = tk.Button(janela, text="Botão 3", command=botao1_click)
botao5 = tk.Button(janela, text="Botão 3", command=botao1_click)

# Use o método pack para colocar os botões na mesma linha
botao1.pack(side=tk.LEFT, anchor="nw")
botao2.pack(side=tk.RIGHT, anchor="ne")
botao3.pack()
botao4.pack()
botao5.pack()


# Inicie o loop principal da interface gráfica
janela.mainloop()