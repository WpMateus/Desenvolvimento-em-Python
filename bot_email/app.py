'''
Criar uma interface gráfica para receber, email, senha e escolher os arquivos que deseja
'''

import PySimpleGUI as sg

sg.theme('reddit')

janela_principal = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexos', target='input_anexos'), sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher pasta planilha', target='input_planilha'), sg.Input(key='input_planilha')],
    [sg.Button('Salvar')],
]

janela = sg.Window('Principal', layout=janela_principal)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        caminho_anexos = values['input_anexos']
        caminho_planilha = values['input_planilha']
        print(f'O e-mail digitado foi {email}')
        print(f'O senha digitado foi {senha}')
        print(f'O caminho da pasta de anexos foi {caminho_anexos}')
        print(f'O caminho da pasta de planilhas foi {caminho_planilha}')