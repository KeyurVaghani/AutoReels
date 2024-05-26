import moviepy.editor as mpy
from moviepy.video.fx.all import crop

def crop_video():
    clip = mpy.VideoFileClip("assest/video.mp4")
    (w, h) = clip.size
    aspect_ratio = 9/16

    new_height = h
    new_width = int(new_height * aspect_ratio)

    new_width = min(new_width, w)

    cropped_clip = crop(clip, width=new_width, height=new_height, x_center=w/2, y_center=h/2)
    cropped_clip.write_videofile('assest/video_crop.mp4')
