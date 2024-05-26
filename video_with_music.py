from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def add_music():
    video = VideoFileClip('assest/video_crop_subtitled.mp4')

    original_audio = video.audio
    new_audio = AudioFileClip('assest/music.mp3')
    new_audio = new_audio.subclip(0, video.duration) 
    original_audio = original_audio.volumex(0.90)
    new_audio = new_audio.volumex(0.10)
    combined_audio = CompositeAudioClip([original_audio, new_audio])

    video_with_audio = video.set_audio(combined_audio)
    video_with_audio.write_videofile('assest/video_with_music.mp4')