from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

# Cores

cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # Branca
cor2 = "#4fa882"  # Verde
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"  # Letra
cor5 = "#e06636"  # Profit
cor6 = "#038cfc"  # Azul
cor7 = "#3fbfb9"  # Verde
cor8 = "#263238"  # + Verde
cor9 = "#e9edf5"  # + Verde


# Criando janela

janela = Tk()
janela.title("")
janela.geometry("800x600")  # largura, altura
janela.configure(background=cor9)
janela.resizable(width=False, height=False) #impede de alterar tam da janela

style = ttk.Style(janela)
style.theme_use("clam")

# Criando Frames


frame_topo = Frame(janela, width=800, height=50, bg=cor1, relief=FLAT)
frame_topo.grid(row=0, column=0)

frame_menu = Frame(janela, width=800, height=300, bg=cor1, pady=20, relief=FLAT)
frame_menu.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_rodape = Frame(janela, width=800, height=300, bg=cor1, relief=FLAT)
frame_rodape.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)



#Abrindo Imagem

img_icon = Image.open("extras/my_book_shelf/assets/images/icon_books.png")
img_icon = img_icon.resize((45,45))
img_icon = ImageTk.PhotoImage(img_icon)

#Criando Label
label_icon = Label(frame_topo, image=img_icon, text='MyBookShelf', width=800, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=cor1, fg=cor4)
label_icon.place(x=0, y=0)








janela.mainloop()