from modules.pytube import Stream
from Storing_place import Place

class Manipulate_stream:
    
    @staticmethod
    def stream_info(stream: Stream):
        if stream == None:
            return None
        elif stream.type == "video":
            return Manipulate_stream.__video_stream_info(stream)
        else:
            return Manipulate_stream.__audio_stream_info(stream)
    
    
    def __video_stream_info(stream: Stream):
        
        res = stream.resolution
        fps = stream.fps
        extension = stream.subtype
        size_mb = stream.filesize_mb
        is_adaptive = stream.is_adaptive
        
        return f"{res.center(5)} - {fps} FPS  {extension.ljust(5)}  Size: {size_mb} MB  {"( Needs Processing )" if is_adaptive else ''}"

    
    def __audio_stream_info(stream: Stream):
        
        abr = stream.abr
        extension = stream.subtype
        size_mb = stream.filesize_mb
        is_adaptive = stream.is_adaptive
        
        return f"{abr.center(7)} - {extension.ljust(5)}  Size: {size_mb} MB"
    
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