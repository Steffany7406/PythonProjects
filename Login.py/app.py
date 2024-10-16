import customtkinter 

#Customizando background
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Abrindo a janela
janela = customtkinter.CTk()
janela.geometry("500x300")

#função para verificar a funcionalidade do botão
def clique():
    print("Cliquei no botão")

#Texto da Janela
texto = customtkinter.CTkLabel(janela, text='Login on Py')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela,  placeholder_text='Sua senha', show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembre-me')
checkbox.pack(padx=10, pady=10)

#Botao do login
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

#Mantendo a janela aberta pro usuário
janela.mainloop()
