import customtkinter as ctk
from tkinter import * # ALL FERRAMENTAS DO TKINTER
from tkinter import messagebox #PARA MENSAGENS DE ALERTA


def add_tarefa():
    t = tarefas.get()
    
    if (t):
        
        lista_tarefa.insert(0,t)
        tarefas.delete(0, 'end')
        salvar_tarefas()
    else:
        messagebox.showerror('ERRO', 'Insira uma tarefa!')
        
def del_tarefa():
    selecionada = lista_tarefa.curselection()
    
    if (selecionada):
        lista_tarefa.delete(selecionada)
        messagebox.showinfo('AVISO', 'Tarefa deleta com sucesso!')
    else:
        messagebox.showerror('ERRO', 'Selecione uma tarefa!')
        

def salvar_tarefas():
    # diversos formatos de arquivo
    with open('tarefas.txt', 'w' ) as taf:
        tarefas = lista_tarefa.get(0, END)
        for x in tarefas:
            taf.write(x+'\n')        


def carregar_tarefas():
    with open('tarefas.txt', 'r') as taf:
        tarefas = taf.readlines()
        for x in tarefas:
            lista_tarefa.insert(0, x)


ctk.set_appearance_mode("dark")
janela = ctk.CTk() #CRIANDO A JANELA E ATRIBUINDO O NOME A ELA
janela.geometry('500x800')
janela.title('Lista de Tarefas - Versão 1.0')

colorPadrao = '#ff9100'

tarefas = ctk.CTkEntry(janela, width=320, height=40,
                       border_color=colorPadrao, placeholder_text="Digite a tarefa a ser criada", 
                       font=('Consolas', 16))
tarefas.pack(pady=10)

btAdicionar = ctk.CTkButton(janela, width=100, height=40, fg_color="green",
                            hover_color='darkgreen',text="Adicionar Tarefa", font=('Consolas', 15, 'bold'), text_color='white',
                            cursor='hand2', command=add_tarefa)
btAdicionar.place(x=90, y=60)

btExcluir = ctk.CTkButton(janela, width=100, height=40, fg_color="red",
                            hover_color='darkred',text="Excluir Tarefa", font=('Consolas', 15, 'bold'), text_color='white',
                            cursor='hand2', command=del_tarefa)
btExcluir.place(x=280, y=60)

# O LISTBOX É MEDIDO PELA QUANTIADE DE LETRAS v v v 
lista_tarefa = Listbox(janela, width=40, height=15, font=('Verdana', 12, 'bold'),
                       background='#3b3b3b', highlightbackground=colorPadrao, fg=colorPadrao)

lista_tarefa.place(x=30, y=120)


carregar_tarefas()
janela.mainloop()