"""
Projeto em Python feito por Dev Aprender - https://www.youtube.com/watch?v=-qsH6iG7me8

Olá preciso do seguinte, um bot que faça o acesso a um site da prefeitura do meu município por meio de um login que é o meu CPF e uma
senha, feito isso dentro de um determinado campo ele preencha o CNPJ de um cliente para entrar na área de acesso dele, que ele vá ate
um menu espeșífico de nota fiscal e que faça o download dos xml, feito isso preciso que ele vá até um outro menu e faça a entrega da
declaração de serviços e salve os arquivos, tanto o xml quanto o recibo de entrega da declaração de serviços numa pasta específica no
dropbox, criando uma pasta com um nome específico para posterior importação, feito isso ele selecionará o menu e digitará o próximo
CNPJ e repete o processo."""

import PySimpleGUI as sg
from time import sleep

sg.theme('reddit')

# criar layout
login = [
    [sg.Text("Usuário")],
    [sg.Input(key="usuario")],
    [sg.Text("Senha")],
    [sg.Input(password_char="*", key="senha")],
    [sg.Button("Enviar")],
    [sg.Output(size=(43,10))]
    ]

# criar janela
janela = sg.Window("Login", layout=login)

# ler os eventos

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Enviar":
        usuario_digitado = values["usuario"]
        senha_digitado = values["senha"]
        print("Passo 1 feito...")
        sleep(5)
        print("Passo 2 feito...")
        sleep(5)
        print("Passo 3 feito...")
