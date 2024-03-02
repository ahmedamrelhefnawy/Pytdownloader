from pytube import Stream
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
    
    @staticmethod
    def __video_stream_info(stream: Stream, print_size = True):
        
        res = stream.resolution
        fps = stream.fps
        extension = stream.subtype
        size_mb = stream.filesize_mb
        is_adaptive = stream.is_adaptive
        
        if is_adaptive:
            print_size = False
        
        return f'''{res.center(5)} - {fps} FPS  {extension.ljust(5)}  {f"Size: {size_mb} MB  " if print_size == True else ''}{"( Needs Processing )" if is_adaptive else ''}'''

    @staticmethod
    def __audio_stream_info(stream: Stream, print_size = True):
        
        abr = stream.abr
        extension = stream.subtype
        size_mb = stream.filesize_mb
        
        return f'''{abr.center(7)} - {extension.ljust(5)}  {f"Size: {size_mb} MB  " if print_size == True else ''}'''