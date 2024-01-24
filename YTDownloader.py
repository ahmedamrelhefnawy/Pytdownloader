from pytube import YouTube
from libs import choices_manip
yt = YouTube('https://www.youtube.com/shorts/opRm3x9vHH0')

streams = yt.streams.filter(type="video")
print(streams)
print(choices_manip.format_streams(streams))


# ccccccccc
