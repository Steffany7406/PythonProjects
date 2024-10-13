from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*', size=(20, 1))],

    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)
#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if  eventos == 'Entrar':
        if  valores['usuario'] == 'Steffany' and valores['senha'] == '1234567':
            sg.popup('Bem vindo!')

