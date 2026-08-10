# 🎥 YouTube Video Downloader

Um downloader de vídeos do YouTube em alta qualidade, desenvolvido em **Python**, utilizando:

* **pytubefix** → Para acessar e baixar streams do YouTube
* **MoviePy** → Para combinar (*merge*) áudio + vídeo
* **FFmpeg** → Para processamento de mídia

---

## ✨ Funcionalidades

* 📥 Download automático da melhor qualidade disponível
* 🎬 Suporte a vídeos em **1080p, 2K e 4K**
* 🔊 Download separado de áudio e vídeo (DASH)
* 🔗 União automática em arquivo final `.mp4`
* ⚡ Processo simples e rápido

---

## 🧐 Como funciona?

O YouTube utiliza o formato **DASH**, onde:

* Vídeo e áudio são separados em altas resoluções

Este projeto realiza automaticamente:

1. 📹 Download da melhor qualidade de vídeo (sem áudio)
2. 🎧 Download da melhor faixa de áudio
3. 🔄 Combinação usando **MoviePy + FFmpeg**
4. 💾 Geração do arquivo final em `.mp4`

---

## 🛠️ Pré-requisitos

Antes de começar, você precisa ter:

* 🐍 **Python 3.8+**
* 🎞️ **FFmpeg** instalado no sistema

### 🔧 Instalar FFmpeg

* Windows: Baixe e adicione ao PATH
* Linux:

```bash
sudo apt install ffmpeg
```

* Mac:

```bash
brew install ffmpeg
```

---

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/lsanzz/yt-downloader.git
cd yt-downloader
```

---

### 2. Criar ambiente virtual

#### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Linux / 🍎 Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o projeto

```bash
python main.py
```

---

## 📁 Estrutura do projeto

```bash
yt-downloader/
│
├── downloads/          # Vídeos finalizados
├── venv/               # Ambiente virtual
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Documentação
├── requirements.txt    # Dependências
└── main.py             # Aplicação principal
```

---

## 📄 Licença

Este projeto está sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais detalhes.

---

## 💡 Observações

* Certifique-se de que o **FFmpeg está no PATH**
* Alguns vídeos podem ter restrições do YouTube
* A velocidade depende da sua conexão
