import customtkinter as ctk


ctk.set_appearance_mode('dark')

def calcular():
    p = float(peso.get())  # Convert peso to float for proper calculation
    a = float(altura.get())  # Use altura for height, not peso
    
    imc = p / (a * a)
    
    if imc <= 18.5:
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f} e você está MAGRO!', text_color='yellow')  
    elif 18.5 < imc < 25:
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f} e você está NORMAL!', text_color='lightgreen')  
    elif 25 <= imc < 30:
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f} e você está com OBESIDADE!', text_color='yellow')  
    else:
        resultado.configure(text=f'Sr(a) {nome.get()}, o seu IMC é {imc:.1f} e você está com SOBREPESO!', text_color='red')
        

def limpar():
    nome.delete(0, ctk.END)  # Limpar do 0-FINAL da VARIAVEL
    peso.delete(0, ctk.END)  # Limpar do 0-FINAL da VARIAVEL
    altura.delete(0, ctk.END)  # Limpar do 0-FINAL da VARIAVEL
    resultado.configure(text='')
    return
    

janela = ctk.CTk()
janela.minsize(600,500)
janela.maxsize(700,550)
janela.title('Aplicativo Saúde')

corVerde = '#12b566'

# --- ICONE DA PAGINA 
janela.iconbitmap("biceps_body_building_fitness_icon_224857.ico")

texto =ctk.CTkLabel(janela,text='Aplicativo Saúde',font=('Arial',30,),text_color='#12b566')
texto.pack(padx=0, pady=10)

nome = ctk.CTkEntry(janela,placeholder_text='Digite o seu Nome',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black', border_color=corVerde)
nome.pack(padx=20, pady=20)

peso = ctk.CTkEntry(janela,placeholder_text='Digite o seu Peso',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black', border_color=corVerde)
peso.pack(padx=20, pady=20)

altura = ctk.CTkEntry(janela,placeholder_text='Digite o sua Altura',font=('Arial',20),fg_color='white', width=400, height=50,text_color='black', border_color=corVerde)
altura.pack(padx=20, pady=20)

botao =ctk.CTkButton(janela,text='Calcular',fg_color='blue', text_color='white', hover_color='cyan', height=60, command=calcular)
botao.place(x=150,y=350)

botao2 =ctk.CTkButton(janela,text='Limpar',fg_color='darkred', text_color='white', hover_color='red', height=60, command=limpar)
botao2.place(x=300,y=350)


resultado = ctk.CTkLabel(janela, text='', text_color='yellow', font=("Consolas", 12))
resultado.place(x=10, y=470)

janela.mainloop()