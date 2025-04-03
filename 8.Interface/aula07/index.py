import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode('dark')


# ----- INICIALIZAR A JANELA PELA BIBLIOTECA -----------------------
janela = ctk.CTk('black') #<- RECEBE CORES HEXADECIMAS

#TAMANHO DA JANELA 
janela.geometry('600x450') 

#PERMITIR REDIMENSIONAR A JANELA
janela.resizable(False, False)

#TITULO DA JANELA
janela.title("Sistema de Posto") 

# ICONE DA JANELA
janela.iconbitmap('3668856-car-fuel-gas-station_108026.ico')

# ------------------------------------------------------------------

# TABELA DE CORES 
rosa = '#e100ff'
azul = '#00fff7'


# -------  TITULOS DA JANELA PRINCIPAL  ---------
ctk.CTkLabel(janela,
             text= 'APP de Consumo de Viagem',
             font=('Consolas', 25), 
             text_color=rosa 
             ).pack(pady=(25,0))

ctk.CTkLabel(janela,
             text= '03/2025 - SENAI BAHIA',
             font=('Consolas', 15,), 
             text_color=rosa
             ).pack()
# -----------------------------------------------



#------- TITULO DO INPUT DISTANCIA
ctk.CTkLabel(janela,
             text='Distancia',
             text_color=azul,
             font=('Consolas',16),
             ).place(x=0, y=0)


#------ INPUT DA DISTANCIA 

distancia = ctk.CTkEntry(janela, width=400,
                         height=30,
                         placeholder_text='Digite a distancia em KM ',
                         fg_color='#2b2b2b'
                         )
distancia.pack(pady=5) 
#-------   FECHANDO O METEDO

ctk.CTkLabel(janela,
             text='Consumo',
             text_color=azul,
             font=('Consolas',16),
             ).pack()

consumo = ctk.CTkEntry(janela,
                       width=400, 
                       height=30,
                       placeholder_text='Digite o cosumo em Litros',
                        fg_color='#2b2b2b'
                       )
consumo.pack(pady=5)

ctk.CTkLabel(janela,
             text='Preço',
             text_color=azul,
             font=('Consolas',16)
             ).pack()

preco = ctk.CTkEntry(janela,
                       width=400, 
                       height=30,
                       placeholder_text='Digite o preco atual',
                       fg_color='#2b2b2b'
                       )
preco.pack(pady=5)


botao = ctk.CTkButton(janela,
                      width = 50,
                      height=38,
                      text_color='black',
                      text='Calcular o valor da viagem',
                      fg_color='#2b2b2b', 
                      hover_color=rosa)
                        

botao.pack(pady=10)

#MOSTRA A JANELA 
janela.mainloop()
