from cx_Freeze import setup, Executable
import os

# O nome do arquivo Python que você quer transformar em executável
target = 'layout.py'

# Caminho para o ícone (se aplicável)
icon_path = os.path.join(os.path.dirname(__file__), 'Icon.ico')

# Configurações do executável
executables = [
    Executable(
        script=target,
        base="Win32GUI",  # Para criar uma GUI sem console
        icon=icon_path    # Caminho para o ícone
    )
]

# Configuração do setup
setup(
    name="ConversorPDFtoXLSX",
    version="0.1",
    description="Conversor de PDF para XLSX",
    options={
        "build_exe": {
            "includes": ["tabula", "openpyxl", "PySimpleGUI"],  # Módulos que serão incluídos
            "include_files": ['Icon.ico']       # Arquivos extras a serem incluídos
        }
    },
    executables=executables
)