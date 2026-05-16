from downloader import Downloader
from utils import menu, limpar_tela


if __name__ == "__main__":
    app = Downloader()
    while True:
        limpar_tela()
        menu()
        escolha = input("Escolha uma das opções: ")

        match escolha:
            case "1":
                limpar_tela()
                app.montar_comando()
                app.baixar()
                input('pressione enter para retornar ao menu')

            case "2":
                limpar_tela()
                app.montar_comando(modo_audio=True)
                app.baixar()
                input('pressione enter para retornar ao menu')
            case "3":
                limpar_tela()
                print("encerrando. Ate mais!")
                break
            case _:
                input("Opcão inválida. Tente novamente.\n")
                limpar_tela()
