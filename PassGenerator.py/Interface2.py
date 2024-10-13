#Programa de interface para

#Armazena o site/software para o qual a senha será gerada
#Armazena o usuario/email
#Possibilitar a configuração do tamanho da senha
#Possibilitar música de fundo ao iniciar o programa

import random
import PySimpleGUI as sg
import os

class PassGen:
    def  __init__(self):
        sg.theme('linear-gradiente= white, gray, black')
        layout = [
            [sg.Text('Site/Software', size=(10,1))],
            [sg.Input(key='site',  size=(20,1))],
            [sg.Text('Email/Usuário',  size=(10,1))],
            [sg.Input(key='usuario', size=(20,1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars',  default_value=1, size=(3,1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        #Declarar janela
        self.janela = sg.Window('Password Generator', layout , size=(600, 300))

    def Iniciar(self):
        while True:
            evento,  valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                sg.popup(nova_senha)
                self.salvar_senha(nova_senha, valores)
                
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&'
        chars = random.choices(char_list,k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
              
    def Salvar_senha(self, nova_senha, valores):
        with open('senhas.txt','a',newline='') as arquivo:
            arquivo.write(f'Site: {valores["site"]}, Usuario : {valores["usuario"]}, Nova Senha: {nova_senha}')



gen = PassGen()
gen.Iniciar()

