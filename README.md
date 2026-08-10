# 🎥 YouTube Video Downloader

Um downloader de vídeos do YouTube em alta qualidade desenvolvido em Python, utilizando a biblioteca **pytubefix** para conexão com a API do YouTube e **MoviePy** para união (*merge*) das trilhas de áudio e vídeo de alta resolução.

---

## 🧐 Por que MoviePy e Pytubefix?

O YouTube armazena vídeos em altas resoluções (1080p, 2K, 4K) separando a trilha de imagem da trilha de som (mídias adaptativas DASH). 

Este projeto baixa automaticamente:
1. A melhor faixa de vídeo disponível (sem áudio).
2. A melhor faixa de áudio disponível.
3. Utiliza o **MoviePy** para combinar as duas faixas em um arquivo final `.mp4` em alta qualidade.

---

## 🛠️ Pré-requisitos

- **Python 3.8+** instalado.
- **FFmpeg** instalado no sistema operacional (utilizado internamente pelo MoviePy para renderização de mídia).

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/lsanzz/yt-downloader.git](https://github.com/lsanzz/yt-downloader.git)
cd yt-downloader

2. Criar e ativar o ambiente virtual (venv)
Windows:

Bash
python -m venv venv
venv\Scripts\activate
Linux/Mac:

Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar as dependências
Bash
pip install -r requirements.txt
4. Executar a aplicação
Bash
python main.py

📁 Estrutura do Projeto
Plaintext
yt-downloader/
│
├── downloads/          # Pasta onde os vídeos processados são salvos
├── venv/               # Ambiente virtual Python
├── .gitignore          # Arquivos e pastas ignorados pelo Git
├── README.md           # Documentação do projeto
├── requirements.txt    # Lista de dependências Python
└── main.py             # Código-fonte principal da aplicação

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
