#Pegar os dados da planilha
import openpyxl

#Transferir para a imagem do certificado
from PIL import Image, ImageDraw, ImageFont

#Abrir a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    #cada célula que contém a info que precisamos
    nome_curso = linha[0].value # Nome do curso
    nome_participante = linha[1].value # Nome do participante
    tipo_participacao = linha[2].value # Tipo de participação
    carga_horaria = linha[5].value #Carga horária


    data_inicio = linha[3].value # Data inicio
    data_final= linha[4].value # Data final

    data_emissao = linha[6].value # Data emissão

    #Transferir para a imagem do certificado

    #Definindo a fonte a ser usada
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf',80)
    fonte_data = ImageFont.truetype('./tahoma.ttf', 55)

    imagem = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(imagem)

    desenhar.text((1020,825), nome_participante, fill='black', font= fonte_nome)
    desenhar.text((1060, 955), nome_curso, fill='black', font= fonte_geral)
    desenhar.text((1435, 1070), tipo_participacao, fill='black', font= fonte_geral)
    desenhar.text((1480, 1190), str(carga_horaria), fill='black', font= fonte_geral)

    desenhar.text((740, 1755), data_inicio, fill='blue', font= fonte_geral)
    desenhar.text((740, 1910), data_final, fill='blue', font= fonte_geral)

    desenhar.text((2220, 1910), data_emissao, fill='blue', font= fonte_geral)


    imagem.save(f'./{indice} {nome_participante} certificado.png')