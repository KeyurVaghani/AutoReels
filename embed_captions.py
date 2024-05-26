from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt
from pilmoji import Pilmoji
from PIL import ImageFont, Image
import numpy as np

def create_subtitle_clips(subtitles, videosize,fontsize=12, font='Arial', color='white', debug = True):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(subtitle.text, fontsize=fontsize, color=color, size=(video_width*3/4, None)
                             , method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height* 2.5 / 5 

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips

def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000