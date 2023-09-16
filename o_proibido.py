from tkinter import *
import os
from tkinter import PhotoImage
class Exodia(Frame):
    def __init__(self, master, cont):
        Frame.__init__(self, master)

        self.janela = master
        self.cont = cont
        self.image_labels = [
        "Perna Esquerda de O Proibido.png",    
        "Perna Direita de O Proibido.png",       
        "Braço Esquerdo de O Proibido.png",    
        "Braço Direito de O Proibido.png",
        "Tronco de O Proibido.png",    
        "Exodia O Proibido.png", "Only Forca.png"]

        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", self.image_labels[self.cont])
        imgLogo = PhotoImage(file=img_path)
        
        self.label = Label(self.janela, image=imgLogo, background="#3D89E1")
        self.label.image = imgLogo
        self.label.pack(padx= 5, pady= 5)

        self.update_image()

    def update_image(self):
        self.label.destroy()
        
        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", self.image_labels[self.cont])
        imgLogo = PhotoImage(file=img_path)
        
        self.label = Label(self.janela, image=imgLogo,background="#3D89E1")
        self.label.image = imgLogo
        self.label.pack(padx= 5, pady= 5)

    def atua(self, atua):
        self.cont = atua
        self.update_image()
    
    def reinicia(self):
        self.label.destroy()
        
        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", "Only Forca.png")
        imgLogo = PhotoImage(file=img_path)

        
        self.label = Label(self.janela, image=imgLogo, background="#3D89E1")
        self.label.image = imgLogo
        self.label.pack(padx= 5, pady= 5)

def luck():
    app = Tk()
    Exodia(app,0)
    app.mainloop()