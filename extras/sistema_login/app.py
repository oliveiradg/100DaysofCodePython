#importando bibliotecas

import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage

# Passaando parametros para o CustomTkInter
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# criando classe principal

 # configurando janela inicial
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_janela_inicial()
        self.tela_login()

   
   


    def config_janela_inicial(self):
        self.title("Sistema de Login")
        self.geometry("700x400")
        self.resizable(False, False)

       # Criando Tela Login

    def tela_login(self):
        #trabalhando com as imagens
        self.img = PhotoImage(file="./extras/sistema_login/assets/images/login.png")

        self.label_img = ctk.CTkLabel(self, text=None, image=self.img) # type: ignore
        
        self.label_img.grid(row=1, column=0, padx=10)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()

