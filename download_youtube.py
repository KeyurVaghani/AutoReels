# tamporary fix for 400 Bad Request
from pytubefix import YouTube

def download_video(url, save_path='assest/'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if video:
            video.download(save_path, filename='video.mp4')
            print("Download successful!")
        else:
            print("No progressive stream available for this video.")
    except Exception as e:
        print("Error:", e)

def download_music(url, save_path='assest'):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        if audio:
            audio.download(save_path, filename='music.mp3')
            print("Download successful!")
        else:
            print("No audio stream available for this video.")
    except Exception as e:
        print("Error:", e)
