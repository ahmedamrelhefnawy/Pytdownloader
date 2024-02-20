import os

from .User import User

from pytube import Playlist, YouTube, Stream
from .avideo import avideo
from .manipulate_stream import Manipulate_stream

from .Storing_place import Place
from .on_progress import on_progress


class aplaylist:

    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.title = playlist.title
        self.owner = playlist.owner
        self.length = playlist.length
        self.videos = playlist.videos
        self.video_urls = playlist.video_urls

    @property
    def info(self):
        return f"Title: {self.playlist.title}\nFor: {self.playlist.owner}\nLength: {self.playlist.length} Videos"

    def print_videos(self):
        for i in range(self.length):
            print(f"{i+1}: {self.videos[i].title}")

    def choose_format(self):
        user_input = User.get_int_input(
            "1: Video\n2: Audio\n\nChoose by number: ", [1, 2])

        if user_input == 1:
            return 'video'
        else:
            return 'audio'

    def ask_download_mode(self, dl_format: str):
        os.system("cls" if os.name == "nt" else "clear")
        chosen_function = User.get_int_input(
            "1: Download all videos\n2: Download range of videos\n3: Select Videos\n\nChoose by number: ", [1, 2, 3])

        os.system("cls" if os.name == "nt" else "clear")

        if chosen_function == 1:
            self.ask_download_all(dl_format)

        elif chosen_function == 2:
            self.ask_range_download(dl_format)

        elif chosen_function == 3:
            self.ask_selective_download(dl_format)

    def ask_download_all(self, dl_format):

        print("\nLoading data, Please wait...")

        # Getting common streams
        common_streams = self.get_common_streams(range(self.length), dl_format)

        # Asking the user to choose a stream
        chosen_stream = self.ask_choose_stream(common_streams)

        Place.ask_change_place()
        print("\nPlease wait...")
        
        # Downloading selected items
        self.download_videos(chosen_stream, range(len(self.length)))

    def ask_range_download(self, dl_format):

        user_from = User.get_int_input(
            "Download From: ", range(1, self.length + 1))

        user_to = User.get_int_input(
            "Download to: ", range(user_from, self.length + 1))

        # Making sure
        self.print_range_of_videos(range(user_from - 1, user_to))

        if User.get_bool_input("\nAre these the videos you have selected ? (Y/n): "):

            print("\nLoading data, Please wait...")

            # Getting common streams
            common_streams = self.get_common_streams(
                range(user_from - 1, user_to), dl_format)

            # Asking the user to choose a stream
            chosen_stream = self.ask_choose_stream(common_streams)

            Place.ask_change_place()
            print("\nPlease wait...")
            # Downloading selected items
            self.download_videos(chosen_stream, range(user_from - 1, user_to))

        else:
            self.ask_range_download(dl_format)

    def ask_selective_download(self, dl_format: str):

        user_input = input(
            "\nSelect videos (Type their numbers in the playlist with spaces in between): ").split()

        # Saving indices
        selected_indices = []
        for index in user_input:
            if int(index) < self.length + 1:
                selected_indices.append(int(index) - 1)

        # Making sure
        self.print_selected_videos(selected_indices)

        if User.get_bool_input("\nAre these the videos you have selected ? (Y/n): "):

            print("\nLoading data, Please wait...")

            # Getting common streams
            common_streams = self.get_common_streams(
                selected_indices, dl_format)

            # Asking the user to choose a stream
            chosen_stream = self.ask_choose_stream(common_streams)

            Place.ask_change_place()
            print("\nPlease wait...")
            
            # Downloading selected items
            self.download_videos(chosen_stream, selected_indices)
        else:
            self.ask_selective_download(dl_format)

    def download_videos(self, chosen_stream: Stream, indices_list: 'list[int]'):

        length = len(indices_list)

        for index in range(len(indices_list)):

            url = self.video_urls[indices_list[index]]
            video = avideo(YouTube(url=url, on_progress_callback=on_progress))

            print(f"\n\nDownloading: {video.title}\n[video: {index + 1} from {length}]")
            video.download(chosen_stream)
        
        print("\n\n- All videos are successfully downloaded -\n".center(60))

    def print_range_of_videos(self, indices_list: 'list[int]'):
        if len(indices_list) < 7:
            self.print_selected_videos(indices_list)
        else:
            print(f"\nFrom Video: {self.videos[indices_list[0]].title}\n.\n.\n{self.videos[indices_list[len(indices_list)//2]].title}\n.\n.\nTo Video: {self.videos[indices_list[-1]].title}")

    def print_selected_videos(self, indices_list: 'list[int]'):
        selected_videos = []
        for index in sorted(set(indices_list)):
            video_of_index = self.videos[index]
            print(f"{index + 1}: {video_of_index.title}")

        return selected_videos

    def get_common_streams(self, selected_indices: 'list[int]', dl_format: str) -> 'list[Stream]':

        common_streams = []

        for index in (selected_indices[0], selected_indices[len(selected_indices)//2], selected_indices[-3]):
            for stream in avideo(self.videos[index]).get_available_streams(dl_format):

                if not self.stream_itag_exist(stream, common_streams):
                    common_streams.append(stream)

        if common_streams:
            if common_streams[0].type == 'video':
                return sorted(common_streams, key=lambda stream: int(stream.resolution[:-1]))[::-1]
            else:
                return sorted(common_streams, key=lambda stream: int(stream.abr[:-4]))[::-1]

    def print_streams(self, streams: 'list[Stream]'):

        os.system("cls" if os.name == "nt" else "clear")

        for i in range(len(streams)):
            print(
                f"{str(i + 1).zfill(2)}: {Manipulate_stream.stream_info(streams[i], False)}")

    def stream_itag_exist(self, test_stream: Stream, list_of_streams: 'list[Stream]') -> bool:

        for stream in list_of_streams:
            if stream.itag == test_stream.itag:
                return True

        return False

    def ask_choose_stream(self, streams: 'list[Stream]') -> Stream:

        self.print_streams(streams)
        user_input = User.get_int_input(
            "\nChoose a stream: ", range(1, len(streams)+1))
        return streams[user_input - 1]


if __name__ == "__main__":
    myplaylist = aplaylist(Playlist(
        "https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs"))
    myplaylist.choose_format()
