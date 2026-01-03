import customtkinter as ctk
import tkinter.font as tkFont
import ctypes

ctypes.windll.gdi32.AddFontResourceW("DS-DIGIB.TTF")

from datetime import datetime
# from tkinter

import tkinter as tk


# ==== VARIAVEIS DE CORES ======

corPreta = "#000000"
corVerde = "#02b508"
corAmarela = "#fcdb03"
corAzul = "#044fb8"
corDourado = "#f5a402"
corVermelha = "#d90000"
corPretaAzul = "#0a0914"
corBranco = "#fcfcfc"

# ==============================

fundo = corPretaAzul
cor = corBranco
textCor = corAmarela

fontFamily = "DS-Digital" # FONTE DE TUDO
fontText = ('Consolas', 20) # TAMANHO DO TEXTO


janela = ctk.CTk() #INICIANLIZANDO 



janela.minsize(390, 180)
janela.maxsize(520, 300)
# janela.geometry("490x230") # TAMANHO DA JANELA

janela.title("TIME OF WORLD") # TITULO DA PAGINA
janela.resizable(True, True) # REDIMENSIONAR???

janela.config(bg=fundo)


def Relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    diaSemana = tempo.strftime("%A")
    dia = tempo.day
    
    proximoAno = tempo.year+1
    
    fimAno = datetime(proximoAno, 1, 1)
    
    diferenca = fimAno - tempo
    
    diasRestantes = diferenca.days
    
    textoDias = f"Faltam {diasRestantes} dias para o Ano Novo!"
    
    localAnoNovo.configure(text=textoDias)
    localAnoNovo.after(86400000, Relogio)
   
    
    
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")
    
    localTime.configure(text=hora)
    localTime.after(200, Relogio)
    localDate.configure(text=diaSemana + "/" + str(dia) + "/" + str(mes) + "/" + str(ano))
    

localTime = ctk.CTkLabel(janela, text="", text_color=cor,
             font=(fontFamily, 100), fg_color=fundo)
localTime.pack(pady=10)
# localTime.place(x=16, y=10)


localDate = ctk.CTkLabel(janela, text="", text_color=textCor,
             font=(fontText), fg_color=fundo)
localDate.pack(pady=4)
# localDate.place(x=140, y=100)


localAnoNovo = ctk.CTkLabel(janela, text="", text_color=textCor,
             font=(fontText), fg_color=fundo)
localAnoNovo.pack(pady=7)
# localAnoNovo.place(x=80, y=130)


Relogio()

#fixa acima das telas
janela.attributes("-topmost", True)
 


janela.mainloop() # INICIALIZANDO 

