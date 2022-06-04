from pydub import AudioSegment
import os
import click
import os

@click.command()
@click.option('--link', '-l', default="link", help='The link to the audio you want to download')
@click.option('--file', '-f', default="filename", help='The filename you want to set for the export')
def download_audio(link, file):
    """
    Download audio from youtube. Usage:
    
    >> python download_audio.py -l https://youtu.be/toZW65rksYY -f Borgir
    
    """
    
    # Download only audio from youtube at the highest quality
    os.system(f"youtube-dl --extract-audio --audio-quality 0 {link}")
    print('download completed')

    # get latest edited file
    base_folder = os.getcwd()
    files = [x for x in os.listdir(base_folder)]
    latest_file = max(files , key = os.path.getctime)

    # conversion from webm to mp3
    sound = AudioSegment.from_file(f"{base_folder}/{latest_file}")
    sound.export(f"/Users/ludovicocesaro/Desktop/Music/{file}.mp3", format="mp3", bitrate="128k")
    print("exported correctly")

    # delete download for cleanup
    os.remove(f"{base_folder}/{latest_file}")

if __name__ == "__main__":
    download_audio()
