import subprocess
import os

# https://www.youtube.com/watch?v=VjDg2txbbik


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def painel():
    print("=" * 40)
    print("       YT-DOWNLOADER v1.0")
    print("=" * 40)
    print("[1] Baixar vídeo")
    print("[2] Baixar áudio")
    print("[3] Sair")
    print("-" * 40)

    try:
        resposta = int(input("Escolha: "))
        return resposta
    except ValueError:
        return 0


def baixar_video():
    limpar_tela()
    print("\n[DOWNLOAD - VIDEO]")
    link = input("Link do vídeo: ").strip()

    if not link:
        print("O link está vazio, cancelando...\n")
        return False

    print("processando...")

    titulo = subprocess.check_output([
        'yt-dlp',
        '--get-title',
        link], text=True).strip()

    print(f"obtido: {titulo}\nfazendo o download do vídeo.")

    try:
        subprocess.run(['yt-dlp', link])
        print("\nDownload concluído!\n")
    except Exception as erro:
        print(f'Houve um erro durante o download :/\n{erro}')


def baixar_audio():
    limpar_tela()
    print("\n[DOWNLOAD - AUDIO]")
    link = input("Link do vídeo: ").strip()

    if not link:
        print("O link está vazio, cancelando...\n")
        return False

    print('baixando o áudio, aguarde...')
    try:
        subprocess.run([
            'yt-dlp',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            link
            ])

    except Exception as erro:
        print(f'Houve um erro ao extrair o áudio :/\n{erro}')


while True:
    opcao = painel()

    if opcao == 1:
        baixar_video()
        input("Pressione ENTER para continuar...")
        limpar_tela()
    elif opcao == 2:
        baixar_audio()
        input("Pressione ENTER para continuar...")
        limpar_tela()
    elif opcao == 3:
        print("\nAté mais, obrigado por usar o programa!\n")
        break
    else:
        print("\nOpção inválida! Tente de novo.\n")
        input("Pressione ENTER...")
        limpar_tela()
