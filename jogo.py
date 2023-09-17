import re
import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, messagebox
from jogo_da_forca import Forca
from o_proibido import Exodia

class Tela():
    def __init__(self, master):
        self.janela = master

        self.telaInicial()

    def telaInicial(self):
        self.janela.geometry('800x600')
        self.janela.title('Tela De Play')
        self.janela.configure(bg='#3D89E1')

        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", "Logo.png")
        imgLogo = PhotoImage(file=img_path)
        l_logo = tk.Label(self.janela, image=imgLogo, background="#3D89E1")
        l_logo.image = imgLogo
        l_logo.pack(pady=(40, 0), padx=(20,0))

        img_path2 = os.path.join(pastaAPP, "imagem", "adas.png")
        self.b_volta = PhotoImage(file=img_path2)

        img_path3 = os.path.join(pastaAPP, "imagem", "asdasda.png")
        self.apontaD = PhotoImage(file=img_path3)

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
        for widget in self.janela.winfo_children():
                 widget.destroy()
                
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Escolha um Tema')
        self.janela.configure(bg='#3D89E1')

        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        cursor.execute("SELECT jog_nome,jog_pontuacao FROM jogadores WHERE id_jogador = ?", (self.id,))
        res=cursor.fetchall()
        con.close()

        botV = tk.Button(self.janela, image=self.b_volta, command= self.tem_certeza, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
                
        l_nome = tk.Label(self.janela, text=res[0][0],font=("Arial Black", 15), height=1 ,width=10,
        bg="#FFFF33", relief="raised",activebackground= "#FFFF33")

        b_ranque = tk.Button(self.janela, text= "Ranking",height=2 ,width=20, font=("Arial Black", 10),
        bg="#FFFF66", activebackground="#FFFF66",command=self.ranking)

        l_tema = tk.Label(self.janela, image= self.apontaD, bg='#3D89E1')

        b_cores = tk.Button(self.janela, text="Cores", font=("Arial Black", 10), height=2 ,width=20, 
        command=lambda: self.J_conta("Cores"), bg="#FF9933", activebackground="#FF9933")

        b_animais = tk.Button(self.janela, text="Animais", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.J_conta('Animais'), bg="#FF9933", activebackground="#FF9933")

        b_objetos = tk.Button(self.janela, text="Objetos", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.J_conta('Objetos'), bg="#FF9933", activebackground="#FF9933")

        b_paises = tk.Button(self.janela, text="Paises", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.J_conta('Paises'), bg="#FF9933", activebackground="#FF9933")
            
        b_programasTv = tk.Button(self.janela, text= "Programas De TV", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.J_conta("Programas De TV"),    bg="#FF9933", activebackground="#FF9933")

        l_pontu = tk.Label(self.janela, text=res[0][1], font=("Arial Black", 15), bg="#FF3333", 
        borderwidth=2, relief="solid")

        botV.pack(padx= 5, pady= 5, side=tk.LEFT, anchor="nw")
        l_pontu.pack(pady= 5, padx= 5,side=tk.RIGHT, anchor="ne")        
        l_nome.pack(pady= 5)
        b_ranque.pack(pady= (5, 30))
        b_cores.pack(pady=5)
        b_animais.pack(pady=5)
        b_objetos.pack(pady=5)
        b_paises.pack(pady=5)
        b_programasTv.pack(pady= 5)
        l_tema.pack(anchor="s", side= tk.BOTTOM)
    
    def ranking(self):
        for widget in self.janela.winfo_children():
             widget.destroy()
                
        self.janela.geometry('600x458')
        self.janela.title('Ranking')
        self.janela.configure(bg='#3D89E1')

        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        cursor.execute("SELECT jog_nome, jog_pontuacao FROM jogadores ORDER BY jog_pontuacao DESC;")
        res = cursor.fetchall()
        con.close()

        botV = tk.Button(self.janela, image=self.b_volta, command= self.abrir_categorias, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.pack(padx= (5,0), pady= 5, side=tk.LEFT, anchor="nw")

        styli =  ttk.Style()
        styli.configure("Treeview", font=("Arial Black", 10), rowheight = 25)
        
        styli.configure("Treeview",background="#FFB266")
        
        styli.map("Treeview", background=[('selected', '#B2FF66')], foreground=[('selected', 'black')])

        frame = tk.Frame(self.janela)

        treeview = ttk.Treeview(frame, columns=("Position", "Name", "Score"), show="headings")
        treeview.heading("Position", text="Posição")
        treeview.heading("Name", text="Nome")
        treeview.heading("Score", text="Pontuação")

        self.scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=self.scrollbar.set)
        
        self.atualizar_button = tk.Button(self.janela, text="Atualizar", command=self.atualizar_treeview,
        bg="#FFFF66", activebackground="#FFFF66", font=("Arial Black", 10), height=2 ,width=20)
        
        treeview.column('Position', width=75, anchor=tk.CENTER)
        treeview.column('Name', width=100, anchor=tk.CENTER)
        treeview.column('Score', width=100, anchor=tk.CENTER)
        treeview.configure(style="Treeview")

        styli.configure("Treeview.Heading", font=("Arial Black", 10))

        # Chama a função para preencher o TreeView
        self.preencher_treeview(treeview, res)

        frame.pack(pady=(50,15), side= tk.TOP)
        treeview.grid(row=0, column=0, )
        self.scrollbar.grid(row = 0, column=1, sticky=(tk.N, tk.S))
        self.atualizar_button.pack(padx= 5, pady=5)

    def atualizar_treeviewV(self):
        self.rankingV()
    
    def atualizar_treeview(self):
        self.ranking()
    
    def preencher_treeview(self, treeview, data):
        for position, (name, score) in enumerate(data, start=1):
            treeview.insert("", "end", values=(position, name, score))

    def J_conta(self, temas):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Escolha uma Dificuldade')
        self.janela.configure(bg='#3D89E1')

        botV = tk.Button(self.janela, image=self.b_volta, command= self.abrir_categorias, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.pack(padx= 5, pady= 5, anchor= tk.W)
            
        b_facil = tk.Button(self.janela, text= "Fácil", font=("Arial Black", 10), height=2 ,width=20,command=lambda: self.dificuldadeF(temas, "faz o L"),
        bg="#FF9933", activebackground="#FF9933")
        b_facil.pack(padx= 5, pady= 5)

        b_medio = tk.Button(self.janela, text= "Médio", font=("Arial Black", 10), height=2 ,width=20,command=lambda: self.dificuldadeM(temas,"faz o L"),
        bg="#FF9933", activebackground="#FF9933")
        b_medio.pack(padx= 5, pady= 5)

        b_dificil = tk.Button(self.janela, text= "Difícil", font=("Arial Black", 10), height=2 ,width=20,command=lambda: self.dificuldadeD(temas, "faz o L"),
        bg="#FF9933", activebackground="#FF9933")
        b_dificil.pack(padx= 5, pady= 5)

    
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
            bg="#FF9933", activebackground="#FF9933", command=self.logar)
            b_entrar.pack(padx= 5, pady= 5)

    def logar(self):
        email =self.e_email.get()
        senha=self.e_senha.get()
        self.id = 0
        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        cursor.execute("SELECT jog_email, jog_senha,id_jogador FROM jogadores")
        res=cursor.fetchall()
        con.close()
        senhaV = False
        emailV = False

        for x in res:
            if x[0] == email and x[1] == senha:
                emailV = True
                senhaV = True
                self.id=x[2]


        for row in res:
                if emailV and senhaV:  # Supondo que o email está na terceira coluna e a senha na quarta coluna
                    emailV = False
                    senhaV = False
                    self.abrir_categorias()
                return 
        messagebox.showinfo('Aviso', 'O Email ou Senha Estão Incorretos')
    

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
            bg="#FF9933", activebackground="#FF9933",command=self.confirmar)
            b_entrar.pack(padx= 5, pady= 5)

    def confirmar(self):
        nome=self.nome.get()
        email=self.e_email.get()
        senha=self.e_senha.get()
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        pont=0
        existe = False

        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        cursor.execute("SELECT jog_email FROM jogadores")
        res=cursor.fetchall()
        con.close()
        
        for x in res:
            if x[0] == email:
                existe = True

        if nome == '' or senha == '' or email == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.janela)
        elif not re.match(padrao_email, email): 
            messagebox.showerror(title= "Email Invalido", message="E-mail não segue o formato padrão")
        elif existe:
            messagebox.showerror(title= "Existe", message="E-mail já existe")
            existe = False
        else:
             con = sqlite3.connect('banco7.db')
             cursor = con.cursor()
             cursor.execute(f"INSERT INTO jogadores VALUES (NULL,'{nome}','{email}','{senha}','{pont}')")
             con.commit()
             con.close()
             messagebox.showinfo('Aviso','Sua Conta foi cadastrada',parent=self.janela)
    
    def visitante(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Visitante')
        self.janela.configure(bg='#3D89E1')

        botV = tk.Button(self.janela, image=self.b_volta, command= self.volta, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)

        b_ranque = tk.Button(self.janela, text= "Ranking",height=2 ,width=20, font=("Arial Black", 10),
        bg="#FFFF66", activebackground="#FFFF66",command=self.rankingV)
        
        b_cores = tk.Button(self.janela, text="Cores", font=("Arial Black", 10),height=2 ,width=20, 
        command=lambda: self.forcaVisitante("Cores"), bg="#FF9933", activebackground="#FF9933")

        b_animais = tk.Button(self.janela, text="Animais", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.forcaVisitante('Animais'), bg="#FF9933", activebackground="#FF9933")

        b_objetos = tk.Button(self.janela, text="Objetos", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.forcaVisitante('Objetos'), bg="#FF9933", activebackground="#FF9933")

        b_paises = tk.Button(self.janela, text="Paises", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.forcaVisitante('Paises'), bg="#FF9933", activebackground="#FF9933")
        
        b_programasTv = tk.Button(self.janela, text= "Programas De TV", font=("Arial Black", 10),height=2 ,width=20,
        command=lambda: self.forcaVisitante("Programas De TV"), bg="#FF9933", activebackground="#FF9933")

        l_tema = tk.Label(self.janela, image= self.apontaD, bg='#3D89E1')

        l_pontu = tk.Label(self.janela, text="Luck", fg='#3D89E1', bg="#3D89E1")

        botV.pack(padx= (5,0), pady= 5, side=tk.LEFT, anchor="nw")
        l_pontu.pack(pady= 5, padx= 5,side=tk.RIGHT, anchor="ne")
        b_ranque.pack(pady= (35,5))        
        b_cores.pack(pady=(30,5))
        b_animais.pack(pady=5)
        b_objetos.pack(pady=5)
        b_paises.pack(pady=5)
        b_programasTv.pack(pady= 5)
        l_tema.pack(side= tk.BOTTOM, anchor="s", pady=(5,0))
    
    def forcaVisitante(self,tex):
        tema = tex
        if tema == "Cores" or tema == "Animais" or tema == "Objetos" or tema == "Paises" or tema == "Programas De TV":
            self.pegar(tema)
    
    def pegar(self, tema):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Escolha uma Dificuldade')
        self.janela.configure(bg='#3D89E1')
        
        botV = tk.Button(self.janela, image=self.b_volta,command= self.visitante, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.pack(padx= 5, pady= 5, anchor= tk.W)
            
        b_facil = tk.Button(self.janela, text= "Fácil", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.dificuldadeF(tema, "Visitante"), bg="#FF9933", activebackground="#FF9933")
        b_facil.pack(padx= 5, pady= 5)

        b_medio = tk.Button(self.janela, text= "Médio", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.dificuldadeM(tema, "Visitante"), bg="#FF9933", activebackground="#FF9933")
        b_medio.pack(padx= 5, pady= 5)

        b_dificil = tk.Button(self.janela, text= "Difícil", font=("Arial Black", 10), height=2 ,width=20,
        command=lambda: self.dificuldadeD(tema,"Visitante"), bg="#FF9933", activebackground="#FF9933")
        b_dificil.pack(padx= 5, pady= 5)

    def rankingV(self):
        for widget in self.janela.winfo_children():
             widget.destroy()
                
        self.janela.geometry('600x458')
        self.janela.title('Ranking')
        self.janela.configure(bg='#3D89E1')

        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        cursor.execute("SELECT jog_nome, jog_pontuacao FROM jogadores ORDER BY jog_pontuacao DESC;")
        res = cursor.fetchall()
        con.close()

        botV = tk.Button(self.janela, image=self.b_volta, command= self.visitante, 
        background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
        botV.pack(padx= (5,0), pady= 5, side=tk.LEFT, anchor="nw")

        styli =  ttk.Style()
        styli.configure("Treeview", font=("Arial Black", 10), rowheight = 25)
        
        styli.configure("Treeview",background="#FFB266")
        
        styli.map("Treeview", background=[('selected', '#B2FF66')], foreground=[('selected', 'black')])

        frame = tk.Frame(self.janela)

        treeview = ttk.Treeview(frame, columns=("Position", "Name", "Score"), show="headings")
        treeview.heading("Position", text="Posição")
        treeview.heading("Name", text="Nome")
        treeview.heading("Score", text="Pontuação")

        self.scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=self.scrollbar.set)
        
        self.atualizar_button = tk.Button(self.janela, text="Atualizar", command=self.atualizar_treeviewV,
        bg="#FFFF66", activebackground="#FFFF66", font=("Arial Black", 10), height=2 ,width=20)
        
        treeview.column('Position', width=75, anchor=tk.CENTER)
        treeview.column('Name', width=100, anchor=tk.CENTER)
        treeview.column('Score', width=100, anchor=tk.CENTER)
        treeview.configure(style="Treeview")

        styli.configure("Treeview.Heading", font=("Arial Black", 10))

        # Chama a função para preencher o TreeView
        self.preencher_treeview(treeview, res)

        frame.pack(pady=(50,15), side= tk.TOP)
        treeview.grid(row=0, column=0, )
        self.scrollbar.grid(row = 0, column=1, sticky=(tk.N, tk.S))
        self.atualizar_button.pack(padx= 5, pady=5)

    
    def dificuldadeF(self, tema, T_conta):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Fácil')
        self.janela.configure(bg='#3D89E1')

        if T_conta == "Visitante":
            botV = tk.Button(self.janela, image=self.b_volta, command=self.visitante,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1',  highlightbackground='#3D89E1')
            exodia = Exodia(frame, 6)
            forca = Forca(self.janela, "Facil", tema, exodia, 0)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
            
        else:
            botV = tk.Button(self.janela, image=self.b_volta, command=self.abrir_categorias,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1',  highlightbackground='#3D89E1')
            exodia = Exodia(frame,6)
            forca = Forca(self.janela, "Facil", tema, exodia, self.id)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
    
    def dificuldadeM(self,tema, T_conta):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Médio')
        self.janela.configure(bg='#3D89E1')
        
        if T_conta == "Visitante":
            botV = tk.Button(self.janela, image=self.b_volta, command=self.visitante,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1', highlightbackground='#3D89E1')
            exodia = Exodia(frame,6)
            forca = Forca(self.janela, "Media", tema, exodia, 0)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
            
        else:
            botV = tk.Button(self.janela, image=self.b_volta, command=self.abrir_categorias,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1', highlightbackground='#3D89E1')
            exodia = Exodia(frame,6)
            forca = Forca(self.janela, "Media", tema, exodia, self.id)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
    
    def dificuldadeD(self, tema, T_conta):
        for widget in self.janela.winfo_children():
                widget.destroy()
            
        self.janela = self.janela
        self.janela.geometry('800x600')
        self.janela.title('Forca Difícil')
        self.janela.configure(bg='#3D89E1')
        
        if T_conta == "Visitante":
            botV = tk.Button(self.janela, image=self.b_volta, command=self.visitante,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1',  highlightbackground='#3D89E1')
            exodia = Exodia(frame,6)
            forca = Forca(self.janela, "Dificil", tema, exodia, 0)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
            
        else:
            botV = tk.Button(self.janela, image=self.b_volta, command=self.abrir_categorias,
            background="#3D89E1", activebackground="#3D89E1", borderwidth=0)
            
            frame = tk.Frame(self.janela, bg='#3D89E1',  highlightbackground='#3D89E1')
            exodia = Exodia(frame,6)
            forca = Forca(self.janela, "Dificil", tema, exodia, self.id)
            
            botV.pack(side= tk.LEFT, anchor="nw", pady=5, padx=5)
            forca.pack(side= tk.LEFT, anchor="w")
            frame.pack(side= tk.RIGHT, padx= 30)
           
    def tem_certeza(self):
        vai = messagebox.askokcancel(title= "Tem certeza?", message = "Quer mesmo sair de sua conta?", icon=messagebox.WARNING)
        if vai:
            for widget in self.janela.winfo_children():
                widget.destroy()
        
            self.telaInicial()  

    def volta(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
        
        self.telaInicial()  
       
app = tk.Tk()
Tela(app)
app.mainloop()