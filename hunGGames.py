# PSEUCODIGO 
# FAZER LOGIN - DEPENDENDO SE FOR UM ESPERCIFICO VAI SER UM ADM|USER

# FUNCOES DO ADM 
# EXIBIR TODOS OS USER, REMOVER 

# FUNCOES DO USER 
# ACESSAR O SISTEMA - CADA USER.POST(TITULO - ARTIGO - AUTOR - ANO)


# ARMAZENAR NO BANCO DE DADOS ( ARRY )




#SUPOSTO BANCO DE DADOS - USER 
usuarios = []

#USER - ATRIBUTOS
class Usuario:
    def __init__(self, userName, nome, year, email, senha ):
        self.userName = userName,
        self.nome = nome,
        self.idade = (year - 2026),
        self.email = email,
        self.senha = senha,



#FUNCAO DO SISTEMA GERAL 
def MenuComando():
    print("")
    print("[1] ENTRAR -  USUARIOS")
    print("[2] REGISTRAR - USUARIOS")
    print("[3] SAIR DO SISTEMA ")
    
    return

#FUNCAO DO SISTEMA GERAL 
def OpcaoUser(MenuOpcoes):
    
    While True:
        MenuOpcoes()
        
        opcao = input("DIGTE SUA OPCAO ")
        try: 
            opcao = int(opcao)
        
            if opcao in :
                
                return opcao 
                
                
            else:
                
                
        
    
MenuComando()

