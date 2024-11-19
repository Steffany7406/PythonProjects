import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login CTK")
        self.geometry('400x500')

    def Tittle(self, App):
        self.label = ctk.CTkLabel(self, text="Faça Login", font=("Harlow Solid Italic", 50)).pack(pady=30)
        
    def On_App(self, App):
        self.label_app = ctk.CTkLabel(self, text="Usuário/Email:", font=('High Tower Text', 15)).pack()
        self.entry = ctk.CTkEntry(self, placeholder_text='Username...', height=45, width=250).pack(pady=8)
        self.label_pass = ctk.CTkLabel(self, text="Senha:", font=('High Tower Text', 15)).pack()
        self.entry2 = ctk.CTkEntry(self, placeholder_text='Password...', height=45, width=250, show='*').pack(pady=2)
        self.button = ctk.CTkButton(self, text='Entrar'.upper(), font=('Rockwell Extra Bold', 20) , height=68, width=250).pack(pady=10)

    def clique(self):
        self.check = ctk.CTkCheckBox(self, text='Lembre-me').pack(padx=10, pady=10)
        print('Cliquei no botão.')

if __name__ == "__main__":
    app = App()
    app.Tittle(app)
    app.On_App(app)
    app.clique()
    app.mainloop()