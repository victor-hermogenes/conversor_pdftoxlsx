import PySimpleGUI as sg
import tabula
from openpyxl import Workbook
import os

icon = 'Icon.ico'
def pdf_to_xlsx(input_pdf, output_xlsx):
    dfs = tabula.read_pdf(input_pdf, pages='all', multiple_tables=True)
    wb = Workbook()
    ws = wb.active
    for df in dfs:
        for row in df.itertuples(index=False):
            ws.append(row)
    wb.save(output_xlsx)


layout = [
    [sg.Text('Selecione um arquivo PDF para conversão')],
    [sg.InputText(key='-PDF-'), sg.FileBrowse(file_types=(("PDF Files", "*.pdf")))],
    [sg.Text('Salvar como')],
    [sg.InputText(key='-XLSX-'), sg.FileSaveAs(file_types=(("Excel Files", "*.xlsx")))],
    [sg.Button('Converter'), sg.Button('Sair')],
    [sg.Output(size=(60, 10))]
]

theme = sg.theme('DarkAmber')

window = sg.Window('Conversor de PDF para XLSX', layout, icon=icon)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Converter':
        input_pdf = values['-PDF-']
        output_xlsx = values['-XLSX-']

        if not input_pdf or not output_xlsx:
            sg.popup_error('Por favor, selecione um arquivo PDF e especifique o destino do XLSX.')
            continue

        try:
            pdf_to_xlsx(input_pdf, output_xlsx)
            sg.popup_ok('Conversão concluída!')
        except Exception as e:
            sg.popup_error(f'Ocorreu um erro durante a conversão: {e}')

window.close()
