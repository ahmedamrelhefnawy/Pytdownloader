import os
from .modules.pytube import YouTube, Playlist
from .modules.pytube.exceptions import VideoUnavailable, VideoPrivate
from .streams_manipulate import streams_print, format_streams
from ..libs.on_progress import on_progress
from .modules.moviepy.editor import AudioFileClip, VideoFileClip



def download_details(downloadable_object):
    return f'''\n\n{"*" * 50}
Title:  {downloadable_object.title}
For: {downloadable_object.author if downloadable_object.__class__ == YouTube else downloadable_object.owner}
{"*" * 50}'''


def verify(downloadable_object):
    print(download_details(downloadable_object))
    user_input = input(
        "Is this what you have chosen ? (y/n): ").strip().lower()[0]
    while True:
        if user_input == 'y':
            print("Please wait...")
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


def single_download(place_object):

    formats = ["video", "audio"]
    format_index = int(
        input("\n\n1: Video\n2: Audio Only\n\nChoose Format: ")) - 1

    selected_format = formats[format_index]

    user_input = input("Enter video link: ")
    yt = YouTube(url=user_input, on_progress_callback=on_progress,
                on_complete_callback=place_object.open_folder)
        
    try:
        while not verify(yt):
            user_input = input("Enter video link: ")
            yt = YouTube(user_input)
    
    except VideoUnavailable:
        print("\n Error: Selected Video is not available")
        import YTDownloader

    streams = yt.streams.filter(type=selected_format)

    chosen_itag = get_user_choice(streams)

    output_path = place_object.place
    if not output_path:
        output_path = os.path.join(os.path.expanduser("~"), "Desktop")

    stream = streams.get_by_itag(chosen_itag)

    if stream.is_progressive:
        stream.download(output_path=output_path)
    else:
        download_DASH(streams, chosen_itag, output_path, yt)


def playlist_single_download(yt_object, selected_format, itag, res, place_object, playlist_name):

    yt = yt_object
    
    streams = yt.streams.filter(type= selected_format)
    
    playlist_name = playlist_name
    output_path = place_object.place + f"\{playlist_name}"

    try:
        stream = streams.get_by_itag(itag)
    except:
        formatted_streams = format_streams(streams)
        for stream in formatted_streams:
            if int(stream["res"][0:-1]) <= int(res[0:-1]):
                stream = streams.get_by_itag(stream["itag"])
                break

    if stream.is_progressive or selected_format == "audio":
        stream.download(output_path=output_path)
    else:
        download_DASH(streams, itag, output_path, yt.title)


def playlist_download(place_object):
    
    formats = ["video", "audio"]
    format_index = int(
        input("\n1: Video\n2: Audio Only\n\nChoose Format: ")) - 1
    
    selected_format = formats[format_index]
    
    P_URL = input("Enter playlist URL: ")
    Plist = Playlist(f'{P_URL}')

    while not verify(Plist):
        P_URL = input("Enter playlist URL: ")
        Plist = Playlist(f'{P_URL}')

    video = YouTube(Plist.video_urls[0])
    streams = video.streams.filter(type= selected_format)
    chosen_itag = get_user_choice(streams)
    
    for url_index in range(len(Plist.video_urls)):
        
        print(f"Downloading {video.title} [video: {url_index + 1} from {Plist.length}]")
        try:       
            video = YouTube(Plist.video_urls[url_index], on_progress_callback= on_progress)
            res = streams.get_by_itag(chosen_itag).resolution
            
            playlist_single_download(yt_object= video,
                                     selected_format= selected_format,
                                     itag= chosen_itag,
                                     res= res,
                                     place_object= place_object,
                                     playlist_name= Playlist.title)

        except VideoUnavailable:
            print(f"Video {video.title} is unavailable, skipping...")

    print("Download done.")
    os.startfile(place_object.place)
    user_input = input("Another video ? (y/n): ").lower()[0]
    
    if user_input == "y":
        import YTDownloader
    else:
        exit()


def download_DASH(streams, itag, output_path, title):
    video_file = streams.get_by_itag(itag).download(
        output_path=output_path)
    try:
        audio_file = streams.get_by_itag(251).download(output_path=output_path, filename="audio")
    except:
        audio_file = streams.get_by_itag(140).download(output_path=output_path, filename="audio")

    combine_video_audio(video_file, audio_file, output_path)


def combine_video_audio(video_file, audio_file, output_file_name):
    video_stream = VideoFileClip(video_file)
    audio_stream = AudioFileClip(audio_file)

    # Concatenate the video stream with the audio stream
    final_video = video_stream.set_audio(audio_stream)

    # Export the final video with audio
    final_video.write_videofile(output_file_name + ".mp4")

    os.remove(video_file)
    os.remove(audio_file)