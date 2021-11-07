import tkinter


def newfile():
    text_area.delete(1.0, 'end')


def save_file():
    container = text_area.get(1.0, 'end')
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()


def open_file():
    file = open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)


def update_font():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font=f"{font} {size}")


# Abrindo uma tela.
window = tkinter.Tk()
# Informando o título da janela.
window.title("Notepad")
# Configurando o tamanho da tela.
# window.minsize(width=640, height=480) # Possuí tamanho mínimo
# Com o geometry conseguimos posicionar o local da tela.
# Tela não possui tamanho mínimo
window.geometry("640x480")

# Criando frame para adicionarmos botões no topo da área.
frame = tkinter.Frame(window, height=30)
# Expande o novo frame para o eixo x.
frame.pack(fill="x")

# criando barra secundária
font_text = tkinter.Label(frame, text='Font: ')
# posicionamento do texto
font_text.pack(side="left")

# parâmetros para escolher a font
spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font.pack(side="left")

# parâmetros para escolher o tamanho da font
font_size = tkinter.Label(frame, text="Font size: ")
font_size.pack(side="left")

spin_size = tkinter.Spinbox(frame, from_=6, to=60)
spin_size.pack(side="left")

button_update = tkinter.Button(frame, text="UP", command=update_font)
button_update.pack(side="left")

# Definindo a área onde podemos digitar.
text_area = tkinter.Text(window, font="Arial 14 bold", width=640, height=480)
# Empacotando um widget. Podemos adicionar parâmetros a eles.
text_area.pack()

# Adicionando um Menu
main_menu = tkinter.Menu(window)
# Criando as abas do menu. tearoff desabilitada função de arrastar o menu.
file_menu = tkinter.Menu(main_menu, tearoff=0)
# Adicionando uma função aos botões
file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="open_file", command=open_file)
file_menu.add_command(label="Exit", command=window.quit)
# Adiciona a tela
main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)

# Mantendo ela aberta em loop
window.mainloop()
