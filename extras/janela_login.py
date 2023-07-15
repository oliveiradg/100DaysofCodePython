# Janelas Bonitas no Python - Sistema de Login com CustomTkinter


import customtkinter

janela = customtkinter.CTk()
janela.title('Login')
janela.geometry('400x300')
janela.resizable(False, False)

# Passaando parametros para o CustomTkInter
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# criando função:

def clique():
    print('Cliquei no botão')

texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=10, pady=10)

#usuario
usuario = customtkinter.CTkEntry(janela, placeholder_text='Email')
usuario.pack(padx=10 , pady=10)

#senha
senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show='*')
senha.pack(padx=10 , pady=10)

# checkbox lembrar senha
checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=10 , pady=10)

#botao login 
botao_login = customtkinter.CTkButton(
    janela, text='Login', command=clique)
botao_login.pack(padx=10 , pady=10)

#rodape 
rodape = customtkinter.CTkLabel(janela, text='Feito com ❤ para os #100daysOfPython ')
rodape.pack(padx=5 , pady=20)








janela.mainloop()