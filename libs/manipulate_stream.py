from .modules.pytube import Stream
from .Storing_place import Place

class Manipulate_stream:
    
    @staticmethod
    def stream_info(stream: Stream, print_size = True):
        if stream == None:
            return None
        elif stream.type == "video":
            return Manipulate_stream.__video_stream_info(stream, print_size)
        else:
            return Manipulate_stream.__audio_stream_info(stream, print_size)
    
    
    def __video_stream_info(stream: Stream, print_size = True):
        
        res = stream.resolution
        fps = stream.fps
        extension = stream.subtype
        size_mb = stream.filesize_mb
        is_adaptive = stream.is_adaptive
        
        if is_adaptive:
            print_size = False
        
        return f"{res.center(5)} - {fps} FPS  {extension.ljust(5)}  {f"Size: {size_mb} MB  " if print_size == True else ''}{"( Needs Processing )" if is_adaptive else ''}"

    
    def __audio_stream_info(stream: Stream, print_size = True):
        
        abr = stream.abr
        extension = stream.subtype
        size_mb = stream.filesize_mb
        is_adaptive = stream.is_adaptive
        
        return f"{abr.center(7)} - {extension.ljust(5)}  {f"Size: {size_mb} MB  " if print_size == True else ''}"
    
    # @staticmethod
    # def download_stream_printed(stream: Stream):
    #     print(f"\nDownloading {stream.title}...")
    #     Manipulate_stream.download_stream(stream)
    
    # @staticmethod
    # def download_stream(stream: Stream):
    #     stream.download(output_path= Place.place)
    
    
if __name__ == "__main__":
    from modules.pytube import YouTube
    
    yt = YouTube('https://youtu.be/icKJtjAzfNo')
    print(yt.streams.all())
    # itag = input(":  : ")
    print(Manipulate_stream.stream_info(yt.streams.get_by_itag(251)))