import tkinter as tk

def on_scroll(*args):
    scroll_y = float(args[0])
    text_widget.yview_moveto(scroll_y)

root = tk.Tk()
root.title("Scrollbar Color")

# Barra de rolagem vertical
scrollbar = tk.Scrollbar(root, command=on_scroll)
scrollbar.pack(side="right", fill="y")

# Widget de texto associado à barra de rolagem
text_widget = tk.Text(root, yscrollcommand=scrollbar.set)
text_widget.pack(fill="both", expand=True)

# Adicione algum texto de exemplo ao widget de texto
for i in range(100):
    text_widget.insert(tk.END, f"Line {i}\n")

root.mainloop()