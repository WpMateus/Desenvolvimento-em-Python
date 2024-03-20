import PySimpleGUI as sg

#Primeira interface para selecionar a operação desejada
def menu_layout():
    return [
        [sg.Text("Selecione a operação:")],
        [sg.Radio('Adição', "RADIO1", key='a'), sg.Radio('Subtração', "RADIO1", key='s'),
         sg.Radio('Multiplicação', "RADIO1", key='m')],
        [sg.Radio('Divisão', "RADIO1", key='d'), sg.Radio('Potência', "RADIO1", key='p')],
        [sg.Button('Calcular'), sg.Button('Sair')]
    ]

#Função do resultado
def resultado_layout(resultado):
    return [
        [sg.Text(f"Resultado: {resultado}", size=(20, 1))]
    ]

#Função do menu principal, onde ele exibe a janela calculadora com os resultados do menu_layout

def main():
    window = sg.Window('Calculadora', layout=menu_layout())

    while True:
        event, values = window.read()

        #Faz um laço while, onde dentro tem condição if, se for clicado na janela sair, fecha o programa e para o laço
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        
        #Se for clicado em calcular sem informar a operação, irá gerar um popup de erro e nisso seguirá com o programa aberto
    
        if event == 'Calcular':
            operacao_selecionada = [key for key, value in values.items() if value]
            if not operacao_selecionada:
                sg.popup_error("Selecione uma operação antes de calcular.")
                continue

        #Se for clicado em calular, ele irá ler a operação selecionada e realizará o if correspondente a oparação desejada
            operacao = operacao_selecionada[0]
            numero1 = float(sg.popup_get_text("Informe o primeiro valor:"))
            numero2 = float(sg.popup_get_text("Informe o segundo valor:"))

            if operacao == 'a':
                resultado = numero1 + numero2
            elif operacao == 's':
                resultado = numero1 - numero2
            elif operacao == 'm':
                resultado = numero1 * numero2
            elif operacao == 'd':
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    sg.popup_error("Não é possível dividir por zero.")
                    continue
            elif operacao == 'p':
                resultado = numero1 ** numero2

            window.close()
            window = sg.Window('Calculadora', layout=resultado_layout(resultado))

    window.close()

if __name__ == "__main__":
    main()
