import os
from rich.panel import Panel
from rich.console import Console
from tkinter import Tk
from tkinter.filedialog import askdirectory


def menu():
    console = Console()
    conteudo = "[1] Baixar vídeo\n[2] Baixar áudio\n[3] Sair"
    console.print(Panel(
        conteudo,
        title="[cyan]YT Downloader[/]",
        border_style="white",
        width=30
    ))


def caminho_padrao():
    caminho = os.path.join(os.path.expanduser('~/Downloads'))
    return caminho


def definir_diretorio():
    Tk().withdraw()
    diretorio = askdirectory(
        initialdir=os.path.expanduser("~/Downloads"),
        title='escolha a pasta onde salvar o download'
    )

    return diretorio


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
