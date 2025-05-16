import customtkinter as ctk

from datetime import datetime
# from tkinter


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
cor = corVermelha


janela = ctk.CTk() #INICIANLIZANDO 

janela.geometry("540x230") # TAMANHO DA JANELA

janela.title("TIME OF WORLD") # TITULO DA PAGINA
janela.resizable(False, False) # REDIMENSIONAR???

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
    

localTime = ctk.CTkLabel(janela, text="", text_color=corBranco,
             font=("Consolas", 80), fg_color=fundo)
localTime.pack(pady=10)


localDate = ctk.CTkLabel(janela, text="", text_color=corDourado,
             font=("Casadia code", 20), fg_color=fundo)
localDate.pack(pady=4)


localAnoNovo = ctk.CTkLabel(janela, text="", text_color=corDourado,
             font=("Casadia code", 20), fg_color=fundo)
localAnoNovo.pack(pady=10)


Relogio()

#fixa acima das telas
janela.attributes("-topmost", True)
 


janela.mainloop() # INICIALIZANDO 

