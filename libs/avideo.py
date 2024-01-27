from User import User
from modules.pytube import YouTube, Stream
from manipulate_stream import Manipulate_stream
from Storing_place import Place


class avideo:

    def __init__(self, yt_obj: YouTube):
        self.yt = yt_obj
        self.video_streams = yt_obj.streams.filter(type= "video").order_by("resolution")[::-1]
        self.audio_streams = yt_obj.streams.filter(type= "audio").order_by("abr")[::-1]

    @property
    def info(self):
        return f"Title: {self.yt.title}\nFor: {self.yt.author}\nLength: {self.yt.length}"

    def ask_download(self):
        user_input = User.get_int_input("1: Video\n2: Audio\nChoose by number: ", [1, 2])
        print("\n")
        
        if user_input == 1:
            self.ask_download_video()
        else:
            self.ask_download_audio()

    def ask_download_video(self):
        self.print_video_streams()

        chosen_index = User.get_int_input("\nSelect a format: ",
            range(1, len(self.video_streams) + 1))

        Place.ask_change_place()
        
        self.download_video(self.video_streams[chosen_index - 1])

    def ask_download_audio(self):
        self.print_audio_streams()

        chosen_index = User.get_int_input("\nSelect a format: ",
            range(1, len(self.audio_streams) + 1))

        Place.ask_change_place()

        self.download_audio(self.audio_streams[chosen_index - 1])

    def download_video(self, stream: Stream):
        chosen_itag = stream.itag
        chosen_stream = self.yt.streams.get_by_itag(chosen_itag)

        if chosen_stream:
            if chosen_stream.is_adaptive:
                self.download_adaptive(stream)
            else:
                chosen_stream.download(output_path=Place.place)

        else:
            avideo.__print_quality_not_found()
            closest_stream = avideo.__get_closest_video_stream(stream)

            self.__print_closest_quality(closest_stream)

            if closest_stream.is_adaptive:
                self.download_adaptive(closest_stream)
            else:
                closest_stream.download(output_path=Place.place)

    def download_audio(self, stream: Stream):
        chosen_itag = stream.itag
        chosen_stream = self.yt.streams.get_by_itag(chosen_itag)

        if chosen_stream:
            chosen_stream.download(output_path=Place.place)
        else:
            avideo.__print_quality_not_found()
            closest_stream = avideo.__get_closest_audio_stream(
                stream)
            self.__print_closest_quality(closest_stream)

            chosen_stream.download(output_path=Place.place)

    def __get_closest_video_stream(self, stream: Stream):
        res = int(stream.resolution[:-1])

        for stream in self.yt.streams.order_by("res")[::-1]:
            if int(stream.res[:-1]) <= res:
                return stream

    def __get_closest_audio_stream(self, stream: Stream):
        abr = int(stream.abr[:-4])

        for stream in self.yt.streams.order_by("res")[::-1]:
            if int(stream.abr[:-4]) <= abr:
                return stream

    def __print_quality_not_found():
        print("\nChosen quality is not available for this video,\ndownloading the closest one...\n")

    def __print_closest_quality(closest_quality_stream):
        return f"Downloading {Manipulate_stream.stream_info(closest_quality_stream)}"

    def download_adaptive(self, stream: Stream):
        
        video_name = f"video.{stream.subtype}"
        stream.download(output_path=Place.place, filename=video_name)

        audio = self.yt.streams.get_audio_only()
        audio_name = f"audio.{audio.subtype}"
        audio.download(output_path=Place.place, filename=audio_name)

        from video_manipulation import combine_video_audio
        combine_video_audio(video_file=f"{Place.place}\\{video_name}",
                            audio_file=f"{Place.place}\\{audio_name}",
                            output_file_name=f"{Place.place}\\{stream.title}")

    def print_video_streams(self):

        for stream_index in range(len(self.video_streams)):
            print(
                f"{str(stream_index + 1).zfill(2)}: {Manipulate_stream.stream_info(self.video_streams[stream_index])}")

    def print_audio_streams(self):

        for stream_index in range(len(self.audio_streams)):
            print(
                f"{str(stream_index + 1).zfill(2)}: {Manipulate_stream.stream_info(self.audio_streams[stream_index])}")

if __name__ == "__main__":
    
    from on_progress import on_progress
    yt = YouTube("https://www.youtube.com/watch?v=VxcbppCX6Rk", on_progress_callback= on_progress)
    my_video = avideo(yt)
    my_video.ask_download()