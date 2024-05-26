from moviepy.editor import VideoFileClip, CompositeVideoClip
import pysrt
import subprocess

from download_youtube import download_video, download_music
from caption_youtube import download_caption
from crop import crop_video   
from embed_captions import create_subtitle_clips
from video_with_music import add_music

def convert_mp4_to_mov(input_path, output_path):
    command = f"ffmpeg -i {input_path} {output_path}"
    subprocess.run(command, shell=True)

video_url = 'https://www.youtube.com/watch?v=QIz15aJR3Mw'
music_url = 'https://www.youtube.com/watch?v=nEPhaprM8Sg'

download_video(video_url)
download_caption(video_url)
download_music(music_url)
crop_video()

video_path = "assest/video_crop.mp4"
srtfilename = "assest/captions.srt"
output_path = "assest/output_video.mp4"
video = VideoFileClip(video_path)
subtitles = pysrt.open(srtfilename)

begin,end= video_path.split(".mp4")
output_path = begin+'_subtitled'+".mp4"

subtitle_clips = create_subtitle_clips(subtitles,video.size)
final_video = CompositeVideoClip([video] + subtitle_clips)
final_video.write_videofile(output_path)
convert_mp4_to_mov("assest/video_with_music.mp4", "assest/output_video.mov")
add_music()