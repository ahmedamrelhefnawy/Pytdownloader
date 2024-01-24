from pytube import YouTube
from libs import choices_manipulate

yt = YouTube('https://www.youtube.com/shorts/opRm3x9vHH0')

streams = yt.streams.filter(type="video")
for stream in streams:
    print(stream)

choices_manipulate.streams_print(streams)