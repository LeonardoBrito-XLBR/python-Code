# --- ESSE E UM CALCULO DE IMC CORPORAL --- #
import customtkinter as ctk


# FUNCAO PARA CALCULAR IMC 

def calculo():
    pesoUsu = float(peso.get())
    alturaUsu = float(altura.get())
    
    resultado = pesoUsu / (alturaUsu)**2
    
    if resultado < 18.5:
        condicao = "BAIXO PESO"
    elif resultado >=18.5 and resultado <= 24.99:
        condicao = "NORMAL"
    elif resultado >= 25 and resultado <= 29.99:
        condicao = "SOBREPESO"
    elif resultado > 30:
        condicao = "OBESIDADE"
        
    resultadoIMC.configure(text=f"O RESULTADO DO IMC {resultado:.2f} SIGNIFICA QUE VC ESTA {condicao} ")
    
    
     
    


# INICIANDO
windows = ctk.CTk()

# VARIAVEIS DE COLOR
corText = 'Orange'
corResultadoBom = 'Green'
corResultadoMedio = 'Yellow'
corResultadoGrave = 'Red'


#LARGURA DA JANELA
windows.geometry('800x600')

# RELUGAR A JANELA? VERTICAL E HORIZONTAL
windows.resizable(False, False)

# TITULO DA JANELA
windows.title('VEJA SEU TIPO CORPORAL')

# TEXTO DA JANELA
ctk.CTkLabel(windows, text="SISTEMA DE CALCULO IMC",
             font=("Consolas", 32, 'bold'),
             text_color=corText,
             ).pack()

ctk.CTkLabel(windows, text="Hoje vc vai saber sua condicao corporal",
             font=('Consolas', 20),
             text_color=corText,
             ).pack()

# TEXTO DO INPUT
ctk.CTkLabel(windows, text="DIGITE O SEU PESO ATUAL",
             font=('Consolas', 20),
             text_color=corText,
             ).place(x=250, y=120)


# INPUTS DOS DADOS | VARIAVEL
peso = ctk.CTkEntry(windows, 
                    text_color="black",
                    fg_color='white',
                    height=30,
                    width=300,
                    )
peso.place(x=250, y=160)

ctk.CTkLabel(windows, text="DIGITE A SUA ALTURA ATUAL",
             font=('Consolas', 20),
             text_color=corText,
             ).place(x=250, y=200)

altura = ctk.CTkEntry(windows,
                    text_color="black",
                    fg_color='white',
                    height=30,
                    width=300,
                    )
altura.place(x=250, y=240)

# BOTAO PARA FUNCOES
botao = ctk.CTkButton(windows, width=300, height=50,
                      text_color='white',
                      text='CALCULAR',
                      fg_color='orange',
                      hover_color='black',
                      command=calculo)

botao.place(x=250, y=300)

# LABEL DO RESULTADO 
resultadoIMC = ctk.CTkLabel(
    windows,
    font=("Consolas", 24), 
    text_color=corResultadoBom,
    text="",
)
resultadoIMC.place(x=30, y=380)


# FECHANDO 
windows.mainloop()