import customtkinter as ctk

ctk.set_appearance_mode('dark')

intarface = ctk.CTk()
intarface.geometry('800x500')

intarface.resizable(False,False)

intarface.title('Sistema de Conversao de Moeadas')

# intarface.iconbitmap('10384161.png')


colorText = 'Orange'



ctk.CTkLabel(intarface,
             text="CONVERSAO DE MOEADAS",
             font=('Consolas', 30),
             text_color=colorText,
             ).pack()

ctk.CTkLabel(intarface,
             text='VALOR DE REAL',
             text_color=colorText,
             font=('Consolas', 20)).pack()

intarface.mainloop()
