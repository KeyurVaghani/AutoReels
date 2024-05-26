from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter

def download_caption(video_url):
    video_id = video_url.split("v=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = SRTFormatter()
    json_formatted = formatter.format_transcript(transcript)
    with open('assest/captions.srt', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)