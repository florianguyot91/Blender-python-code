import os
from pytube import YouTube
from pathlib import Path

def youtube2mp3 (url,outdir):
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.get_audio_only()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')


if __name__ == "__main__":
    print("Paste URL:")
    url = input()
    youtube2mp3(url,"Musics")