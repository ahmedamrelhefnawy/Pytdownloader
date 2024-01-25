import os
from pytube import YouTube, Playlist
from .streams_manipulate import streams_print, format_streams
import ffmpeg


def download_details(downloadable_object):
    return f'''\n\n{"*" * 50}
Title:  {downloadable_object.title}
For: {downloadable_object.author}
{"*" * 50}'''


def verify(func, downloadable_object):
    print(download_details(downloadable_object))
    user_input = input(
        "Is this what you have chosen ? (y/n): ").strip().lower()[0]
    while True:
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            user_input = input(
                "Invalid Input, Please type either 'y' as Yes or 'n' as No: ").strip().lower()[0]


def get_user_choice(streams):

    streams, type_of_streams = format_streams(streams)
    streams_print(streams, type_of_streams)

    while True:
        choice = int(input("Choose by number: "))-1
        if choice in range(len(streams)):
            return streams[choice]["itag"]
        else:
            print("Invalid input, please choose a number between the numbers above.")


def single_download():
    
    formats = ["video","audio"]
    format_index = int(input("\n\n1: Video\n2: Audio Only\n\nChoose Format: ")) - 1
    
    selected_format = formats[format_index]
    
    user_input = input("Enter video link: ")
    yt = YouTube(user_input)

    while not verify(single_download, yt):
        user_input = input("Enter video link: ")
        yt = YouTube(user_input)

    streams = yt.streams.filter(type=selected_format)
    
    chosen_itag = get_user_choice(streams)

    output_path = open("configuration", 'r').readline()
    if not output_path:
        output_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    stream = streams.get_by_itag(chosen_itag)
    if stream.is_progressive():
        stream.download(output_path=output_path)
    else:
        download_DASH(streams, chosen_itag, output_path, yt)
        

def download_DASH(streams, itag, output_path, yt):
    video_file = streams.get_by_itag(itag).download(output_path=output_path if output_path else os.path.join(os.path.expanduser("~"), "Desktop"),)
    audio_file = streams.get_by_itag(140).download(output_path=output_path if output_path else os.path.join(os.path.expanduser("~"), "Desktop"), filename= "audio")
    combine_video_audio(video_file, audio_file, output_path, yt)
    
def combine_video_audio(video_file, audio_file, output_file_name, yt):
    video_stream = ffmpeg.input(video_file)
    audio_stream = ffmpeg.input(audio_file)
    
    ffmpeg.output(audio_stream, video_stream, output_file_name, acodec='copy', vcodec='copy', loglevel="quiet").run(overwrite_output=True)
    
    os.remove(audio_file)