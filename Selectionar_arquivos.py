from tkinter import *
from tkinter.filedialog import askopenfilename


class Application:
 def __init__(self, master=None):
  self.widget1 = Frame(master)
  self.widget1.pack()
  self.msg = Label(self.widget1, text="Busque o arquivo")
  self.msg["font"] = ("Calibri", "9", "italic")
  self.msg.pack()
  self.sair = Button(self.widget1)
  self.sair["text"] = "Buscar"
  self.sair["font"] = ("Calibri", "9")
  self.sair["width"] = 10
  self.sair["command"] = self.mudarTexto
  self.sair.pack()
  self.msg2 = Label(self.widget1, text="")
  self.msg2["font"] = ("Calibri", "9", "italic")
  self.msg2.pack()
    
  self.ler = Button(self.widget1)
  self.ler["text"] = "Ler Arquivo"
  self.ler["font"] = ("Calibri", "9")
  self.ler["width"] = 10
  self.ler["command"] = self.lertexto
  self.ler.pack() 
    

 def mudarTexto(self):
  if self.msg["text"] == "Busque o arquivo":
     filename = askopenfilename() # Isto te permite selecionar um arquivo
     self.msg2["text"] = filename
    
 def lertexto(self):
  if self.msg["text"] == "Busque o arquivo":
     filename = askopenfilename() # Isto te permite selecionar um arquivo
     self.msg2["text"] = filename
 



root = Tk()
Application(root)
root.mainloop()
