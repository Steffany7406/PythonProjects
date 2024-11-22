import customtkinter as ctk
from tkinter import ttk #Usado para mudar a aparencia do aplicativo (apenas se for necessário)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login CTK")
        self.geometry('500x620')

        self.current_frame = None  #Exibir tela de Login primeiro
        self.Tittle()
        self.On_App()
        self.clique()

    def switch_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        frame.pack(fill="both", expand=True)
        self.current_frame = frame    

    def Tittle(self):
        self.label = ctk.CTkLabel(self, text="Faça Login", font=("Harlow Solid Italic", 50)).pack(pady=30)
        
    def On_App(self):
        login_frame = ctk.CTkFrame(self)
        login_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.label_app = ctk.CTkLabel(login_frame, text="Usuário/Email:", font=('High Tower Text', 15)).pack()
        self.entry = ctk.CTkEntry(login_frame, placeholder_text='Username...', height=45, width=250).pack(pady=8)
        self.label_pass = ctk.CTkLabel(login_frame, text="Senha:", font=('High Tower Text', 15)).pack()
        self.entry2 = ctk.CTkEntry(login_frame, placeholder_text='Password...', height=45, width=250, show='*').pack(pady=2)
        self.button = ctk.CTkButton(login_frame, text='Entrar'.upper(), font=('Rockwell Extra Bold', 20), height=54, width=250).pack(pady=10)
        self.check = ctk.CTkCheckBox(self, text='Lembre-me').pack(padx=10, pady=10)
        self.switch_frame(login_frame)

    def clique(self):
        self.button_regs = ctk.CTkButton(self, text='Cadastrar', font=('Rockwell Extra Bold', 20), height=54, width=250).pack()
        print('Cliquei no botão.')
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
