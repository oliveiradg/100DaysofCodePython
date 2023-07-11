from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

#importando tkCalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando o modulo de conexão
from view import *

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


# Criando janela---------------------------------------------------------

janela = Tk()
janela.title("")
janela.geometry("800x600")  # largura, altura
janela.configure(background=cor9)
janela.resizable(width=False, height=False) #impede de alterar tam da janela

style = ttk.Style(janela)
style.theme_use("clam")

# Criando Frames --------------------------------------------------------------


frame_topo = Frame(janela, width=800, height=50, bg=cor1, relief=FLAT)
frame_topo.grid(row=0, column=0)

frame_central = Frame(janela, width=800, height=300, bg=cor1, pady=20, relief=FLAT)
frame_central.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_rodape = Frame(janela, width=800, height=300, bg=cor1, relief=FLAT)
frame_rodape.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Criando Funnções--------------------------------------------------------------------------------

global tree   
# Função Inserir
def inserir():

    
    titulo = entry_titulo.get()
    genero =  entry_genero.get()
    autor = entry_autor.get()
    editora = entry_editora.get()
    ano = entry_ano.get_date()
    saga = entry_saga.get()
    lido_monica = check_lido_monica.get()
    lido_joao = check_lido_joao.get()
    imagem = imagem_string
    
    lista_inserir = [titulo, genero, autor, editora, ano, saga, imagem],
    
    for i in lista_inserir:
        if i == '' :
            messagebox.showerror('Erro', 'preencha todos os campos')
            return
# titulo, genero, autor, saga, editora, lido_monica, lido_joao, imagem

        inserir_form(lista_inserir)
        messagebox.showinfo('Sucesso', 'Os Dados foram inseridos com sucesso')

        entry_titulo.delete(0, END)
        entry_genero.delete(0,END)
        entry_autor.delete(0, END)
        entry_editora.delete(0, END)
        entry_ano.delete(0, END)
        entry_saga.delete(0, END)
        check_lido_monica.set(0)
        check_lido_joao.set(0)
       
        for widget in frame_central.winfo_children():
            widget.destroy()

        mostrar()

# Função para escolher Imagem
def escolher_imagem():
    global imagem, imagem_string, label_imagem
    imagem = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("png files", "*.png"),("all files", "*.*")))
    imagem_string = str(imagem)
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,190))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_central, image=imagem, bg=cor1)
    label_imagem.place(x=600, y=10)




# Trabalhando no Frame Topo-----------------------------------------------------

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

# Criando Genero
label_genero = Label(frame_central, text='Gênero', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_genero.place(x=10, y=190)
#Criando Entry (entrada)
entry_genero = Entry(frame_central, width=30, justify='left', relief=SOLID)
entry_genero.place(x=130, y=190)

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

# Criando Botões--------------------------------------


#Criando Botão carregar
label_carregar = Label(frame_central, text='Imagem', height=1, anchor=NW, font=('Verdana 10 bold'),bg=cor1, fg=cor4)
label_carregar.place(x=10, y=220)
botao_carregar = Button(frame_central, command=escolher_imagem, text='Carregar'.upper(), font='Verdana 8 ', width=25, compound=CENTER, anchor=CENTER, overrelief=RIDGE,  relief=RAISED, bg=cor1, fg=cor0)
botao_carregar.place(x=130, y=220)

# Criando Botão inserir

img_add = Image.open("extras/my_book_shelf/assets/images/add.png")
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frame_central,command= inserir, image=img_add, text=' Adicionar'.upper(), font='Verdana 8 ', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE,  relief=RAISED, bg=cor1, fg=cor0)
botao_inserir.place(x=330, y=10)

# Criando Botão alterar
img_alterar = Image.open("extras/my_book_shelf/assets/images/alterar.png")
img_alterar = img_alterar.resize((20,20))
img_alterar = ImageTk.PhotoImage(img_alterar)
botao_alterar = Button(frame_central, image=img_alterar, text=' Alterar'.upper(), font='Verdana 8 ', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE,  relief=RAISED, bg=cor1, fg=cor0)
botao_alterar.place(x=330, y=50)

# Criando Botão excluir
img_excluir = Image.open("extras/my_book_shelf/assets/images/excluir.png")
img_excluir = img_excluir.resize((20,20))
img_excluir = ImageTk.PhotoImage(img_excluir)
botao_excluir = Button(frame_central, image=img_excluir, text=' Excluir'.upper(), font='Verdana 8 ', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE,  relief=RAISED, bg=cor1, fg=cor0)
botao_excluir.place(x=330, y=90)

# Botão Ver Imagem
img_ver = Image.open("extras/my_book_shelf/assets/images/ver.png")
img_ver = img_ver.resize((20,20))
img_ver = ImageTk.PhotoImage(img_ver)
botao_ver = Button(frame_central, image=img_ver, text='Ver Imagem'.upper(), font='Verdana 8 ', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE,  relief=RAISED, bg=cor1, fg=cor0)
botao_ver.place(x=330, y=215)

####################################

# Labels Quantidade total
label_total = Label(frame_central, width=15, text='', height=4, anchor=CENTER, font=('Verdana 10 bold'), bg=cor7, fg=cor1)
label_total.place(x=450, y=17)
label_total_text = Label(frame_central, pady=2, text='   Total de Livros    ', height=1, anchor=NW, font=('Verdana 10 bold'), bg=cor7, fg=cor1)
label_total_text.place(x=450, y=12)





# tabela -----------------------------------------------------------

def mostrar():

    # creating a treeview with dual scrollbars
    tabela_head = ['#ID', 'Título', 'Autor', 'Editora', 'Saga', 'Adquirido', 'Lido']

    lista_itens = []


    tree = ttk.Treeview(frame_rodape, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_rodape, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_rodape, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_rodape.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center", "center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    total_livros = len(lista_itens)

    label_total['text'] = str(total_livros)

mostrar()


janela.mainloop()