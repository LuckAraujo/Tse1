import re
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox
from jogo_da_forca import Forca

class Tela():
    def __init__(self, master):
        self.janela = master

        self.telaInicial()

    def telaInicial(self):
        self.janela.geometry('800x600')
        self.janela.title('Tela De Play')
        self.janela.configure(bg='#3D89E1')
        self.janela.title('Tela De Play')

        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", "Logo.png")
        imgLogo = PhotoImage(file=img_path)
        l_logo = tk.Label(self.janela, image=imgLogo, background="#3D89E1")
        l_logo.image = imgLogo
        l_logo.pack(pady=(40, 0), padx=(20,0))

        img_path2 = os.path.join(pastaAPP, "imagem", "adas.png")
        self.b_volta = PhotoImage(file=img_path2)

        btn1 = tk.Button(self.janela, text="Entrar",  height=2 ,width=20,  command=self.entrar,
        bg="#FF8000", activebackground="#FF8000", font=("Arial Black", 10))
        
        btn1.pack(padx= 20, pady=20)
        
        btn2 = tk.Button(self.janela, text="Cadastrar", height=2 ,width=20, command=self.cadastrar,
        bg="#FF9933", activebackground="#FF9933", font=("Arial Black", 10))
        
        btn2.pack(padx= 20, pady=20)
        
        btn3 = tk.Button(self.janela, text="Visitante", height=2 ,width=20, command=self.visitante, 
        bg="#FFB266", activebackground="#FFB266",font=("Arial Black", 10))
        
        btn3.pack(padx= 20, pady=20)

    def abrir_categorias(self):
            email= self.e_email.get()
            padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            #aqui tbm vai ficar a parte onde vamos validar o email se ele é o do cara mesmo pode ser os da senha tbm
            if not re.match(padrao_email, email): 
                messagebox.showerror(title= "Email Invalido", message="E-mail não segue o formato padrão")

            else:
                for widget in self.janela.winfo_children():
                    widget.destroy()
                
                self.janela = self.janela
                self.janela.geometry('800x600')
                self.janela.title('Escolha uma Categoria')
                self.janela.configure(bg='#3D89E1')
                
                letraA = tk.Button(self.janela, text="FDS")
                letraA.pack()

    
    def entrar(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('400x250')
            self.janela.title('Entrar')
            self.janela.configure(bg='#3D89E1')

            botV = tk.Button(self.janela, image=self.b_volta, command= self.volta, 
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            botV.pack(padx= 5, pady= 5, anchor= tk.W)

            l_email = tk.Label(self.janela, text="Email", font=("Arial Black", 10), background="#3D89E1")
            l_email.pack(padx= 5, pady= 5)
            self.e_email = tk.Entry(self.janela, width= 30)
            self.e_email.pack(padx= 5,pady= (0, 5))

            l_senha = tk.Label(self.janela, text="Senha",font=("Arial Black", 10), background="#3D89E1")
            l_senha.pack(padx= 5, pady= 5)
            self.e_senha = tk.Entry(self.janela, width= 30, show="*")
            self.e_senha.pack(padx= 5, pady= (0, 5))

            b_entrar = tk.Button(self.janela, text= "Logar", font=("Arial Black", 10), 
            bg="#FF9933", activebackground="#FF9933", command= self.abrir_categorias)
            b_entrar.pack(padx= 5, pady= 5)

    
    def cadastrar(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('400x300')
            self.janela.title("Cadastrar")
            self.janela.configure(bg='#3D89E1')

            botV = tk.Button(self.janela, image=self.b_volta, command= self.volta, 
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            botV.pack(padx= 5, pady= 5, anchor= tk.W)

            l_nome = tk.Label(self.janela, text="Nome", font=("Arial Black", 10), background="#3D89E1")
            l_nome.pack(padx= 5, pady= 5)
            self.nome = tk.Entry(self.janela, width= 30)
            self.nome.pack(padx= 5,pady= (0, 5))

            l_email = tk.Label(self.janela, text="Email", font=("Arial Black", 10), background="#3D89E1")
            l_email.pack(padx= 5, pady= 5)
            self.e_email = tk.Entry(self.janela, width= 30)
            self.e_email.pack(padx= 5,pady= (0, 5))

            l_senha = tk.Label(self.janela, text="Senha",font=("Arial Black", 10), background="#3D89E1")
            l_senha.pack(padx= 5, pady= 5)
            self.e_senha = tk.Entry(self.janela, width= 30, show="*")
            self.e_senha.pack(padx= 5, pady= (0, 5))

            b_entrar = tk.Button(self.janela, text= "Criar Conta", font=("Arial Black", 10), 
            bg="#FF9933", activebackground="#FF9933")
            b_entrar.pack(padx= 5, pady= 5)

    
    def visitante(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title('Visitante')
            self.janela.configure(bg='#3D89E1')

    
            botV = tk.Button(self.janela, image=self.b_volta, command= self.volta, 
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            botV.pack(padx= 5, pady= 5, anchor= tk.W)

            b_ranque = tk.Button(self.janela, text= "Ranque", font=("Arial Black", 10),
            bg="#FF9933", activebackground="#FF9933")
            b_ranque.pack(padx= 5, pady= 5)
            
            b_facil = tk.Button(self.janela, text= "Fácil", font=("Arial Black", 10), command= self.dificuldadeF,
            bg="#FF9933", activebackground="#FF9933")
            b_facil.pack(padx= 5, pady= 5)

            b_medio = tk.Button(self.janela, text= "Médio", font=("Arial Black", 10), command= self.dificuldadeM,
            bg="#FF9933", activebackground="#FF9933")
            b_medio.pack(padx= 5, pady= 5)

            b_dificil = tk.Button(self.janela, text= "difícil", font=("Arial Black", 10), command= self.dificuldadeD,
            bg="#FF9933", activebackground="#FF9933")
            b_dificil.pack(padx= 5, pady= 5)
    
    def dificuldadeF(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Fácil')
        self.janela.configure(bg='#3D89E1')
        
        botV = tk.Button(self.janela, image=self.b_volta, command= self.visitante, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.grid(row=0, column=0, padx= 5, pady= 5, sticky="W")

        forca = Forca(self.janela, "Facil")
        forca.grid(row=1, column=0)
    
    def dificuldadeM(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Médio')
        self.janela.configure(bg='#3D89E1')
        
        botV = tk.Button(self.janela, image=self.b_volta, command= self.visitante, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.grid(row=0, column=0, padx= 5, pady= 5, sticky="W")

        forca = Forca(self.janela, "Medio")
        forca.grid(row=1, column=0)

    
    def dificuldadeD(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Difícil')
        self.janela.configure(bg='#3D89E1')
        
        botV = tk.Button(self.janela, image=self.b_volta, command= self.visitante, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.grid(row=0, column=0, padx= 5, pady= 5, sticky="W")

        forca = Forca(self.janela, "Dificil")
        forca.grid(row=1, column=0)

    def volta(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
        
        self.telaInicial()
    

       
app = tk.Tk()
Tela(app)
app.mainloop()