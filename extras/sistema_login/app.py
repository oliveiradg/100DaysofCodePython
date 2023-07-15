#importando bibliotecas

import customtkinter as ctk
import tkinter as tk

# Passaando parametros para o CustomTkInter
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# criando classe principal
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_janela_inicial()

    # configurando janela inicial
    



    def config_janela_inicial(self):
        self.title("Sistema de Login")
        self.geometry("700x400")
        self.resizable(False, False)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()

        
