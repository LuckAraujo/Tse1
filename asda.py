import tkinter as tk

def criar_borda_colorida(frame, cor, largura=1):
    # Top
    frame.create_line(0, 0, frame.winfo_width(), 0, fill=cor, width=largura)
    # Bottom
    frame.create_line(0, frame.winfo_height(), frame.winfo_width(), frame.winfo_height(), fill=cor, width=largura)
    # Left
    frame.create_line(0, 0, 0, frame.winfo_height(), fill=cor, width=largura)
    # Right
    frame.create_line(frame.winfo_width(), 0, frame.winfo_width(), frame.winfo_height(), fill=cor, width=largura)

root = tk.Tk()
root.title("Exemplo de Mudança de Cor de Borda em um Frame")

# Criar o frame
frame = tk.Canvas(root, width=200, height=200, bg='white')
frame.pack(padx=20, pady=20)

# Chamar a função para criar a borda colorida
criar_borda_colorida(frame, cor='blue', largura=5)

root.mainloop()