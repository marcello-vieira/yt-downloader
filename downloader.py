import utils
import subprocess


class Downloader:
    def __init__(self):
        self.url = None
        self.link_video = ""
        self.caminho = utils.caminho_padrao()

    def escolher_caminho(self):
        caminho_anterior = self.caminho

        self.caminho = utils.definir_diretorio()
        if not self.caminho:
            print("nenhum caminho definido. Usando o caminho padrao")
            self.caminho = caminho_anterior
        else:
            print(f"caminho alterado para {self.caminho}")

    def montar_comando(self, modo_audio=False):
        print(f"o download ocorrerá em: {self.caminho}")
        escolha = input('deseja alterar o caminho? (s/n) ')

        if escolha.lower() in ['s', 'sim']:
            self.escolher_caminho()
        else:
            print(f"continuando em {self.caminho}")

        self.comando = ['yt-dlp', '-P', self.caminho]
        if modo_audio:
            self.comando += ['--extract-audio', '--audio-format', 'mp3']

        return self.comando

    def baixar(self):
        self.link_video = input("digite o link do video: ").strip()

        if not self.link_video:
            print("nenhum link informado")
            return

        comando_completo = self.comando + [self.link_video]

        try:
            subprocess.run(comando_completo, check=True)
            print("download concluído")

        except subprocess.CalledProcessError as e:
            print(f"ocorreu um erro: {e}")

        except Exception as e:
            print(f"ocorreu um erro: {e}")
