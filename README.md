# 🎬 YT Downloader

Um baixador de vídeos simples, funcional e feito em Python utilizando o yt-dlp.

## Funcionalidades

- Baixa vídeos do YouTube a ferramenta yt-dlp
- Menu interativo no terminal
- Loop contínuo (baixe vários vídeos sem precisar reiniciar o programa)

---

## 📦 Requisitos

Para que possa ser executado sem problemas, você precisa ter instalado:

- Python 3+
- yt-dlp

### Verifique as versões instaladas

```bash
python3 --version
yt-dlp --version
```

Caso não tenha algum deles instalado, veja a seção:
[Instalação das dependências](#-instalação-das-dependências)

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/yt-downloader.git
```

Entre na pasta do projeto:

```bash
cd yt-downloader
```

Execute o programa:

```bash
python3 main.py
```
E seja feliz baixando seus vídeos :)

---

## 🛠 Instalação das dependências

### Python

Baixe a versão mais recente no site oficial:

[Python.org Downloads](https://www.python.org/downloads/)

---

### yt-dlp

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

Este projeto ainda está no início e foi criado com o objetivo de praticar Python.

👀 Novas funcionalidades e melhorias serão adicionadas aos poucos conforme eu evoluo como desenvolvedor 😄

---

## ❤️ Agradecimentos

Um agradecimento especial ao projeto yt-dlp,
responsável por toda a parte de download dos vídeos.

Projeto oficial:
https://github.com/yt-dlp/yt-dlp
