import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import VideoFileClip, AudioFileClip

def limpar_nome_arquivo(nome: str) -> str:
    """Remove caracteres especiais que não podem ser usados em nomes de arquivos."""
    caracteres_validos = [c for c in nome if c.isalnum()  or c in (" ", "_", "-")]
    return "".join(caracteres_validos).strip()

def baixar_trilhas_youtube(url: str, pasta_destino: str = "downloads") -> tuple[str, str, str]:
    """
    Conecta ao YouTube, baixa a melhor qualidade de vídeo e a melhor 
    qualidade de áudio separadamente em uma pasta de downloads.
    """
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    print("Conectando ao YouTube...")
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"\nTítulo encontrado: {yt.title}\n")

    print("Baixando a melhor faixa de vídeo disponível...")
    stream_video = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)
        .order_by("resolution")
        .desc()
        .first()
    )
    caminho_video_temp = stream_video.download(
        output_path=pasta_destino, filename_prefix="temp_vid_"
    )

    print("\nBaixando a melhor faixa de áudio disponível...")
    stream_audio = yt.streams.filter(adaptive=True, only_audio=True).first()
    caminho_audio_temp = stream_audio.download(
        output_path=pasta_destino, filename_prefix="temp_aud_"
    )

    return yt.title, caminho_video_temp, caminho_audio_temp

def processar_e_juntar_midia(titulo_original: str, caminho_video_temp: str, caminho_audio_temp: str, pasta_destino: str = "downloads") -> None:
    """
    Usa o MoviePy para combinar os arquivos temporários de vídeo e áudio 
    em um único arquivo final MP4 e remove os temporários.
    """
    nome_limpo = limpar_nome_arquivo(titulo_original)
    caminho_final = os.path.join(pasta_destino, f"{nome_limpo}.mp4")

    print(f"\nUnindo vídeo e áudio para criar: {nome_limpo}.mp4")

    clip_video = VideoFileClip(caminho_video_temp)
    clip_audio = AudioFileClip(caminho_audio_temp)

    if hasattr(clip_video, 'with_audio'):
        video_final = clip_video.with_audio(clip_audio)
    else:
        video_final = clip_video.set_audio(clip_audio)

    video_final.write_videofile(
        caminho_final,
        codec="libx264",
        audio_codec="aac",
        logger=None
    )

    clip_video.close()
    clip_audio.close()
    video_final.close()

    os.remove(caminho_video_temp)
    os.remove(caminho_audio_temp)

    print(f"\nConcluído com sucesso! Salvo em: {caminho_final}")
    
def executar_downloader():
    """Função principal que coordena a execução do programa."""
    print("=" * 40)
    print("      DOWNLOADER DE VÍDEOS DO YOUTUBE      ")
    print("=" * 40)

    url_usuario = input("\nCole a URL do vídeo do YouTube: ").strip()

    if not url_usuario:
        print("Erro: A URL não pode estar vazia.")
        return

    try:
        titulo, path_vid, path_aud = baixar_trilhas_youtube(url_usuario)

        processar_e_juntar_midia(titulo, path_vid, path_aud)

    except Exception as erro:
        print(f"\nOcorreu um erro durante o processo: {erro}")


if __name__ == "__main__":
    executar_downloader()