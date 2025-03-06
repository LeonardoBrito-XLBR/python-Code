import customtkinter as ctk 

#TEMA DA EXTENSAO
ctk.set_appearance_mode('dark')



#TAMANHO MAXIMO DE 1920 X 1080 - MEDIA DAS TELAS FULL HD
janela = ctk.CTk('#000000') #comportta cores hexadecimais 
janela.geometry('500x300')

#PERMITIR REDIMENSIONAR AS JANELAS 
janela.resizable(False, False)

#TITULO DA JANELA
janela.title('Sistema de Acesso 2025')

#TITULO DENTRO DA JANELA 
ctk.CTkLabel(janela, 
             text='Sistema de Acesso',
             font=('Consolas', 32, 'bold' ),
             text_color='green').pack(pady=20)


login = ctk.CTkEntry(janela, width=400,
                     height=35,
                     placeholder_text='Digite o seu usuario',
                     font=('calibri',17))

login.pack(pady=5)

senha = ctk.CTkEntry(janela, width=400,
                     height=35,
                     placeholder_text='Digite sua senha',
                     show='ヮ',
                     font=('calibri',17))

senha.pack(pady=20)


botao = ctk.CTkButton(janela, width=150,
                      height=38,
                      text_color='black',
                      fg_color='green',
                      text='Acessar',
                      hover_color='darkgreen',)

botao.pack()

janela.mainloop()