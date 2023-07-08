from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

#importando tkCalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

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

frame_central = Frame(janela, width=800, height=300, bg=cor1, pady=20, relief=FLAT)
frame_central.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_rodape = Frame(janela, width=800, height=300, bg=cor1, relief=FLAT)
frame_rodape.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Trabalhando no Frame Topo------------------------------

#Abrindo Imagem

img_icon = Image.open("extras/my_book_shelf/assets/images/icon_books.png")
img_icon = img_icon.resize((45,45))
img_icon = ImageTk.PhotoImage(img_icon)

#Criando Label
label_icon = Label(frame_topo, image=img_icon, padx=10, text='MyBookShelf', width=800, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=cor1, fg=cor4)
label_icon.place(x=1, y=0)


# Trabalhando no Frame Central------------------------------
#Criando Label
label_titulo = Label(frame_central, text='Título', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_titulo.place(x=10, y=10)
#Criando Entry (entrada)
entry_titulo = Entry(frame_central, width=30, justify='left', relief=SOLID)
entry_titulo.place(x=130, y=11)

#Criando Label
label_autor = Label(frame_central, text='Autor', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_autor.place(x=10, y=40)
#Criando Entry (entrada)
entry_autor = Entry(frame_central, width=30, justify='left', relief=SOLID)
entry_autor.place(x=130, y=41)
#Criando Label
label_editora = Label(frame_central, text='Editora', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_editora.place(x=10, y=70)
#Criando Entry (entrada)
entry_editora = Entry(frame_central, width=30, justify='left', relief=SOLID)
entry_editora.place(x=130, y=71)
#Criando Label
label_saga = Label(frame_central, text='Saga', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_saga.place(x=10, y=130)
#Criando Entry (entrada)
entry_saga = Entry(frame_central, width=30, justify='left', relief=SOLID)
entry_saga.place(x=130, y=131)



#Criando Label
label_ano = Label(frame_central, text='Adquirido', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_ano.place(x=10, y=100)
#Criando Entry (entrada)
entry_ano = DateEntry(frame_central, width=12,Background='darkblue',borderwidth=2, year=2000)
entry_ano.place(x=130, y=101)

#Criando checkbox lido_monica e lido_joao 
lido_monica = IntVar()
lido_joao = IntVar()
lido_monica.set(0)
lido_joao.set(0)
#Criando Label
label_lido = Label(frame_central, text='Lido', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_lido.place(x=10, y=160)
#Criando Checkbutton
check_lido_monica = Checkbutton(frame_central, text='Mônica', variable=lido_monica, onvalue=1, offvalue=0, bg=cor1, fg=cor4)
check_lido_monica.place(x=130, y=161)
check_lido_joao = Checkbutton(frame_central, text='João', variable=lido_joao, onvalue=1, offvalue=0, bg=cor1, fg=cor4)
check_lido_joao.place(x=200, y=161)
#Criando Label



janela.mainloop()