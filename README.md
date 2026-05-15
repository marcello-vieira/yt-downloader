# 🎬 YT Downloader

Um baixador de vídeos simples, mas funcional e feito em Python utilizando o yt-dlp.

## Funcionalidades

- Baixa vídeos do YouTube utilizando a ferramenta yt-dlp
- Menu interativo no terminal
- Loop contínuo (baixe vários vídeos sem precisar reiniciar o programa)

---

## 📦 Requisitos

Para que possa ser executado sem problemas, você precisa ter instalado:

- Python 3+
- yt-dlp
- Outras dependências listadas em `requirements.txt`

### Verifique as versões instaladas

```bash
python3 --version
yt-dlp --version
```

Caso não tenha algum deles instalado, veja a seção:
[Instalação das dependências](#-instalação-das-dependências)

---

## Instalação

clone o repositório:

```bash
git clone https://github.com/marcello-vieira/yt-downloader.git
```

entre na pasta do projeto:

```bash
cd yt-downloader
```
crie um ambiente virtual

```bash
python3 -m venv .venv
```

ative o ambiente virtual 👇️

### Linux / macOS
```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

em seguida, instale as dependências

```bash
pip install -r requirements.txt
```

execute o programa:

```bash
python3 main.py
```
Seja feliz baixando seus vídeos :)

---

## 🛠 Instalação das dependências

### Python
Caso você ainda não tenha o Python instalado, baixe a versão mais recente no site oficial:

[Python.org Downloads](https://www.python.org/downloads/)

---

### yt-dlp
Para instalar o yt-dlp no seu sistema, siga estes passos:

### Linux / macOS

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp \
-o /usr/local/bin/yt-dlp

sudo chmod a+rx /usr/local/bin/yt-dlp
```

---

### Windows

Baixe o executável oficial: https://github.com/yt-dlp/yt-dlp/releases/latest

Depois:
- coloque o arquivo `yt-dlp.exe` em uma pasta
- adicione essa pasta ao PATH do sistema

---

## 🚧 Status do projeto

Este projeto ainda está no início e foi criado com o objetivo de praticar e aprender Python 😄

Novas funcionalidades e melhorias serão adicionadas aos poucos conforme eu evoluo como desenvolvedor 👀

---

## ❤️ Agradecimentos

Um agradecimento especial ao projeto yt-dlp,
responsável por toda a parte de download dos vídeos.

Projeto oficial:
https://github.com/yt-dlp/yt-dlp
