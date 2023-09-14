from tkinter import *
from tkinter import messagebox
import random
import sqlite3
from sqlite3 import Error

class Forca(Frame):
    def __init__(self, master, dificuldade):
        Frame.__init__(self, master)
        # inicializa variáveis
        self.temas = ['Cores', 'Animais', 'Objetos', 'Paises', 'Programas De TV']
        self.cores_padrao_botoes = ["#F0F0F0"]
        self.palavra = None
        self.letras_digitadas = None
        self.palavra_secreta = None
        self.contador = None
        self.dificuldade = dificuldade

        # inicializa widgets do jogo
        self.create_widgets()
        # re-inicializa variáveis do jogo
        self.inicio_jogo() 

    def reset_cores_botoes(self):
        self.letraA.configure(background=self.cores_padrao_botoes[0])
        self.letraB.configure(background=self.cores_padrao_botoes[0])
        self.letraC.configure(background=self.cores_padrao_botoes[0])
        self.letraD.configure(background=self.cores_padrao_botoes[0])
        self.letraE.configure(background=self.cores_padrao_botoes[0])
        self.letraF.configure(background=self.cores_padrao_botoes[0])
        self.letraG.configure(background=self.cores_padrao_botoes[0])
        self.letraH.configure(background=self.cores_padrao_botoes[0])
        self.letraI.configure(background=self.cores_padrao_botoes[0])
        self.letraJ.configure(background=self.cores_padrao_botoes[0])
        self.letraK.configure(background=self.cores_padrao_botoes[0])
        self.letraL.configure(background=self.cores_padrao_botoes[0])
        self.letraM.configure(background=self.cores_padrao_botoes[0])
        self.letraN.configure(background=self.cores_padrao_botoes[0])
        self.letraO.configure(background=self.cores_padrao_botoes[0])
        self.letraP.configure(background=self.cores_padrao_botoes[0])
        self.letraQ.configure(background=self.cores_padrao_botoes[0])
        self.letraR.configure(background=self.cores_padrao_botoes[0])
        self.letraS.configure(background=self.cores_padrao_botoes[0])
        self.letraT.configure(background=self.cores_padrao_botoes[0])
        self.letraU.configure(background=self.cores_padrao_botoes[0])
        self.letraV.configure(background=self.cores_padrao_botoes[0])
        self.letraW.configure(background=self.cores_padrao_botoes[0])
        self.letraX.configure(background=self.cores_padrao_botoes[0])
        self.letraY.configure(background=self.cores_padrao_botoes[0])
        self.letraZ.configure(background=self.cores_padrao_botoes[0])
        self.reiniciar.configure(background=self.cores_padrao_botoes[0])

    def inicio_jogo(self):
        
        self.reset_cores_botoes()
        self.letras_digitadas = []
        self.palavra_secreta = []
        self.contador = 10
        self.label_contador['text'] = self.contador
        self.tema_id = random.randint(1, len(self.temas))
        self.tema_atual = self.temas[self.tema_id - 1]
        self.tema_atual_label['text'] = self.tema_atual
        self.palavra_secreta_label['text'] = ""
        self.dificuldade = self.dificuldade 
                
        self.modo_de_jogo()
        
    def set_letras_digitadas(self, letras):
        chute = False
        for i in range(0, len(self.palavra)):
            for letra in letras:
                if letra == self.palavra[i]:
                    self.palavra_secreta[i] = letra
                    chute = True
                    if letra == "A" or letra == "Á" or letra == "Â" or letra == "Ã":
                        l = letra
                        self.letraA.configure(background="Green", activebackground="Green")
                    if letra == "B":
                        self.letraB.configure(background="Green", activebackground="Green")
                    if letra == "C" or letra == "Ç":
                        self.letraC.configure(background="Green", activebackground="Green")
                    if letra == "D":
                        self.letraD.configure(background="Green", activebackground="Green")
                    if letra == "E" or letra == "É" or letra == "Ê":
                        self.letraE.configure(background="Green", activebackground="Green")
                    if letra == "F":
                        self.letraF.configure(background="Green", activebackground="Green")
                    if letra == "G":
                        self.letraG.configure(background="Green", activebackground="Green")
                    if letra == "H":
                        self.letraH.configure(background="Green", activebackground="Green")
                    if letra == "I" or letra == "Í":
                        self.letraI.configure(background="Green", activebackground="Green")
                    if letra == "J":
                        self.letraJ.configure(background="Green", activebackground="Green")
                    if letra == "K":
                        self.letraK.configure(background="Green", activebackground="Green")
                    if letra == "L":
                        self.letraL.configure(background="Green", activebackground="Green")
                    if letra == "M":
                        self.letraM.configure(background="Green", activebackground="Green")
                    if letra == "N":
                        self.letraN.configure(background="Green", activebackground="Green")
                    if letra == "O" or letra == "Ó" or letra == "Ô":
                        self.letraO.configure(background="Green", activebackground="Green")
                    if letra == "P":
                        self.letraP.configure(background="Green", activebackground="Green")
                    if letra == "Q":
                        self.letraQ.configure(background="Green", activebackground="Green")
                    if letra == "R":
                        self.letraR.configure(background="Green", activebackground="Green")
                    if letra == "S":
                        self.letraS.configure(background="Green", activebackground="Green")
                    if letra == "T":
                        self.letraT.configure(background="Green", activebackground="Green")
                    if letra == "U" or letra == "Ú":
                        self.letraU.configure(background="Green", activebackground="Green")
                    if letra == "V":
                        self.letraV.configure(background="Green", activebackground="Green")
                    if letra == "W" :
                        self.letraW.configure(background="Green", activebackground="Green")
                    if letra == "X":
                        self.letraX.configure(background="Green", activebackground="Green")
                    if letra == "Y":
                        self.letraY.configure(background="Green", activebackground="Green")
                    if letra == "Z":
                        self.letraZ.configure(background="Green", activebackground="Green")

                if letra not in self.letras_digitadas:
                    l = letra
                    self.letras_digitadas.append(letra)
                
        if chute == False:
            try: 
                if l in self.letras_digitadas:    
                    self.contador -= 1            
                    self.label_contador['text'] = self.contador
                    
                    if l == "A" or l == "Á" or l == "Â" or l == "Ã":
                        l = letra
                        self.letraA.configure(background="#737991", activebackground="#737991")
                    if l == "B":
                        self.letraB.configure(background="#737991", activebackground="#737991")
                    if l == "C" or l == "Ç":
                        self.letraC.configure(background="#737991", activebackground="#737991")
                    if l == "D":
                        self.letraD.configure(background="#737991", activebackground="#737991")
                    if l == "E" or l == "É" or l == "Ê":
                        self.letraE.configure(background="#737991", activebackground="#737991")
                    if l == "F":
                        self.letraF.configure(background="#737991", activebackground="#737991")
                    if l == "G":
                        self.letraG.configure(background="#737991", activebackground="#737991")
                    if l == "H":
                        self.letraH.configure(background="#737991", activebackground="#737991")
                    if l == "I" or letra == "Í":
                        self.letraI.configure(background="#737991", activebackground="#737991")
                    if l == "J":
                        self.letraJ.configure(background="#737991", activebackground="#737991")
                    if l == "K":
                        self.letraK.configure(background="#737991", activebackground="#737991")
                    if l == "L":
                        self.letraL.configure(background="#737991", activebackground="#737991")
                    if l == "M":
                        self.letraM.configure(background="#737991", activebackground="#737991")
                    if l == "N":
                        self.letraN.configure(background="#737991", activebackground="#737991")
                    if l == "O" or letra == "Ó" or letra == "Ô":
                        self.letraO.configure(background="#737991", activebackground="#737991")
                    if l == "P":
                        self.letraP.configure(background="#737991", activebackground="#737991")
                    if l == "Q":
                        self.letraQ.configure(background="#737991", activebackground="#737991")
                    if l == "R":
                        self.letraR.configure(background="#737991", activebackground="#737991")
                    if l == "S":
                        self.letraS.configure(background="#737991", activebackground="#737991")
                    if l == "T":
                        self.letraT.configure(background="#737991", activebackground="#737991")
                    if l == "U" or letra == "Ú":
                        self.letraU.configure(background="#737991", activebackground="#737991")
                    if l == "V":
                        self.letraV.configure(background="#737991", activebackground="#737991")
                    if l == "W" :
                        self.letraW.configure(background="#737991", activebackground="#737991")
                    if l == "X":
                        self.letraX.configure(background="#737991", activebackground="#737991")
                    if l == "Y":
                        self.letraY.configure(background="#737991", activebackground="#737991")
                    if l == "Z":
                        self.letraZ.configure(background="#737991", activebackground="#737991")
            
            except UnboundLocalError:
                pass    
        
        if self.contador <= 0:
            messagebox.showinfo("Alert", "\nVOCÊ PERDEU!!!!!!!!!!            \n")
            messagebox.showinfo("Info", "A palavra secreta era:\n{0}".format(self.palavra))
            self.inicio_jogo()

        # Atualiza na tela as letras encontradas na palavra secreta        
        self.palavra_secreta_label['text'] = ' '.join(self.palavra_secreta)

        if "_" not in self.palavra_secreta:
            messagebox.showinfo("Congrats", "Parabéns você acertou a palavra secreta\n{}".format(self.palavra))
            self.inicio_jogo()
    def reinicia(self):
        for widget in self.janela.winfo_children():
                widget.destroy()


    def create_widgets(self):
        #Frame teclado letras
        self.frame1 = Frame(self, relief = SUNKEN, borderwidth=8)
        self.frame1.grid(row=5)

        self.letraA = Button(self.frame1, font=("Helvetica", 12), text="A", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("AÁÂÃ"))
        self.letraA.grid(row=0, column=0, sticky="NWNESWSE")

        self.letraB = Button(self.frame1, font=("Helvetica", 12), text="B", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("B"))
        self.letraB.grid(row=0, column=1, sticky="NWNESWSE")

        self.letraC = Button(self.frame1, font=("Helvetica", 12), text="C", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("CÇ"))
        self.letraC.grid(row=0, column=2, sticky="NWNESWSE")

        self.letraD = Button(self.frame1, font=("Helvetica", 12), text="D", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("D"))
        self.letraD.grid(row=0, column=3, sticky="NWNESWSE")

        self.letraE = Button(self.frame1, font=("Helvetica", 12), text="E", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("EÉÊ"))
        self.letraE.grid(row=0, column=4, sticky="NWNESWSE")

        self.letraF = Button(self.frame1, font=("Helvetica", 12), text="F", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("F"))
        self.letraF.grid(row=0, column=5, sticky="NWNESWSE")

        self.letraG = Button(self.frame1, font=("Helvetica", 12), text="G", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("G"))
        self.letraG.grid(row=0, column=6, sticky="NWNESWSE")

        #linha 1
        self.letraH = Button(self.frame1, font=("Helvetica", 12), text="H", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("H"))
        self.letraH.grid(row=1, column=0, sticky="NWNESWSE")

        self.letraI = Button(self.frame1, font=("Helvetica", 12), text="I", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("IÍ"))
        self.letraI.grid(row=1, column=1, sticky="NWNESWSE")

        self.letraJ = Button(self.frame1, font=("Helvetica", 12), text="J", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("J"))
        self.letraJ.grid(row=1, column=2, sticky="NWNESWSE")

        self.letraK = Button(self.frame1, font=("Helvetica", 12), text="K", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("K"))
        self.letraK.grid(row=1, column=3, sticky="NWNESWSE")

        self.letraL = Button(self.frame1, font=("Helvetica", 12), text="L", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("L"))
        self.letraL.grid(row=1, column=4, sticky="NWNESWSE")

        self.letraM = Button(self.frame1, font=("Helvetica", 12), text="M", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("M"))
        self.letraM.grid(row=1, column=5, sticky="NWNESWSE")

        self.letraN = Button(self.frame1, font=("Helvetica", 12), text="N", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("N"))
        self.letraN.grid(row=1, column=6, sticky="NWNESWSE")

        #linha 2
        self.letraO = Button(self.frame1, font=("Helvetica", 12), text="O", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("OÓÔ"))
        self.letraO.grid(row=2, column=0, sticky="NWNESWSE")

        self.letraP = Button(self.frame1, font=("Helvetica", 12), text="P", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("P"))
        self.letraP.grid(row=2, column=1, sticky="NWNESWSE")

        self.letraQ = Button(self.frame1, font=("Helvetica", 12), text="Q", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Q"))
        self.letraQ.grid(row=2, column=2, sticky="NWNESWSE")

        self.letraR = Button(self.frame1, font=("Helvetica", 12), text="R", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("R"))
        self.letraR.grid(row=2, column=3, sticky="NWNESWSE")

        self.letraS = Button(self.frame1, font=("Helvetica", 12), text="S", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("S"))
        self.letraS.grid(row=2, column=4, sticky="NWNESWSE")

        self.letraT = Button(self.frame1, font=("Helvetica", 12), text="T", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("T"))
        self.letraT.grid(row=2, column=5, sticky="NWNESWSE")

        self.letraU = Button(self.frame1, font=("Helvetica", 12), text="U", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("UÚ"))
        self.letraU.grid(row=2, column=6, sticky="NWNESWSE")

        #linha 3
        self.letraV = Button(self.frame1, font=("Helvetica", 12), text="V", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("V"))
        self.letraV.grid(row=3, column=0, sticky="NWNESWSE")

        self.letraW = Button(self.frame1, font=("Helvetica", 12), text="W", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("W"))
        self.letraW.grid(row=3, column=1, sticky="NWNESWSE")

        self.letraX = Button(self.frame1, font=("Helvetica", 12), text="X", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("X"))
        self.letraX.grid(row=3, column=2, sticky="NWNESWSE")

        self.letraY = Button(self.frame1, font=("Helvetica", 12), text="Y", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Y"))
        self.letraY.grid(row=3, column=3, sticky="NWNESWSE")

        self.letraZ = Button(self.frame1, font=("Helvetica", 12), text="Z", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Z"))
        self.letraZ.grid(row=3, column=4, sticky="NWNESWSE")

        self.reiniciar = Button(self.frame1, font=("Helvetica", 12), text="Reiniciar", borderwidth=1,padx=16, pady=16, command= self.inicio_jogo)
        self.reiniciar.grid(row=3, column=5,columnspan=2, sticky="NWNESWSE")
        # Fim teclado letras

        # Letras digitadas
        self.frame2 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame2.grid(row=2,sticky="NWNESWSE")

       # Altera o rótulo para exibir "TEMA" em vez de "LETRAS DIGITADAS"
        self.tema_label = Label(self.frame2, text="TEMA", font=("Helvetica", 12))
        self.tema_label.grid(row=0, columnspan=6)

        # Adiciona um rótulo para exibir o tema atual da palavra secreta
        self.tema_atual_label = Label(self.frame2, text="", font=("Helvetica", 12))
        self.tema_atual_label.grid(row=1)

        # contador de erros
        self.frame3 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame3.grid(row=3,sticky="NWNESWSE")

        self.chances_restantes_label = Label(self.frame3, text="CHANCES RESTANTES", font=("Helvetica", 12))
        self.chances_restantes_label.grid(row=0, columnspan=6)

        self.label_contador = Label(self.frame3, font=("Helvetica", 20), text = self.contador,padx=10, pady=10)        
        self.label_contador.grid(row=1, column=0, rowspan=2, columnspan=2)


        #Palavra secreta
        self.frame4 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame4.grid(row=4,sticky="NWNESWSE")

        self.palavra_secreta_titulo = Label(self.frame4, font=("Helvetica", 12), text="PALAVRA SECRETA.", padx=10, pady=10)        
        self.palavra_secreta_titulo.grid(row=0, sticky="W")

        self.palavra_secreta_label = Label(self.frame4, font=("Helvetica", 20), text="", padx=10, pady=10)        
        self.palavra_secreta_label.grid(row=1, column=0, sticky="W") 
    
    def modo_de_jogo(self):
        con = sqlite3.connect('banco7.db')
        cursor = con.cursor()
        
        cursor.execute(f"SELECT pal_palavra FROM palavras WHERE tem_id_fk = {self.tema_id} AND pal_dificuldade = ? ORDER BY RANDOM() LIMIT 1", (self.dificuldade,))
        resultado = cursor.fetchone()
        
        if resultado:
            self.palavra = resultado[0].upper()
            self.palavra_secreta = ["_" if char.isalpha() else char for char in self.palavra]
        else:
            self.palavra = "PADRAO"
            self.palavra_secreta = ["_" for _ in self.palavra]

        con.close()

        self.palavra_secreta_label['text'] = " ".join(self.palavra_secreta)
