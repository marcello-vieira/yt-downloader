import os
import subprocess
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt


class App:
    def __init__(self):
        self.console = Console()
        self.looping_principal()

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        self.conteudo = "[1] baixar video\n[2] baixar audio\n[3] sair"
        self.console.print(Panel(
            self.conteudo,
            title="[cyan]YT Downloader[/]",
            border_style="white",
            width=30
            ))

    def baixar(self, modo_audio=False):
        self.link = Prompt.ask("[bold yellow]Link do video[/]").strip()
        if not self.link:
            self.limpar_tela()
            print("[red]O link ficou vazio, tente de novo[/]")
            return

        self.comando = ['yt-dlp']
        if modo_audio:
            self.comando += [
                '--extract-audio',
                '--audio-format',
                'mp3',
                '--audio-quality',
                '0']
        self.comando.append(self.link)
        try:
            print("[green]iniciando...[/]")
            subprocess.run(self.comando)
            self.limpar_tela()
            print("[green]concluído! verifique na pasta do projeto :)[/]")
        except Exception as erro:
            print("[bold red]Houve um erro durante o download :/[/]")

        input("[Aperte Enter para retornar]")

    def looping_principal(self):
        while True:
            self.limpar_tela()
            self.menu()
            self.escolha = Prompt.ask(
                "[bold green]Sua escolha[/]")

            match self.escolha:
                case '1':
                    self.baixar(modo_audio=False)
                case '2':
                    self.baixar(modo_audio=True)
                case '3':
                    # self.limpar_tela()
                    print("[cyan]Programa encerrado, até mais![/]")
                    break

                case _:
                    print("[red]escolha algo válido.[/]")
                    input("Aperte [Enter] para tentar de novo")
                    continue


if __name__ == '__main__':
    App()
