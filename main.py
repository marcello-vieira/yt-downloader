import subprocess
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def painel():
    print("=" * 40)
    print("       YT-DOWNLOADER v1.0")
    print("=" * 40)
    print("[1] Baixar vídeo")
    print("[2] Sair")
    print("-" * 40)

    try:
        resposta = int(input("Escolha: "))
        return resposta
    except ValueError:
        return 0


def baixar_video():
    print("\n[DOWNLOAD]")
    link = input("Link do vídeo: ").strip()

    if not link:
        print("O link está vazio, cancelando...\n")
        return False

    print("\nBaixando... aguarde.\n")
    subprocess.run(['yt-dlp', link])
    print("\nDownload concluído!\n")


while True:
    opcao = painel()

    if opcao == 1:
        baixar_video()
        input("Pressione ENTER para continuar...")
        limpar_tela()
    elif opcao == 2:
        print("\nAté mais, obrigado por usar o programa!!!\n")
        break
    else:
        print("\nOpção inválida! Tente de novo.\n")
        input("Pressione ENTER...")
        limpar_tela()
