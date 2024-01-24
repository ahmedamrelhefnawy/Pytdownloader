def format_streams(streams):
    '''Converts the List of streams into a List of dictionaries'''

    type_of_streams = streams[0].type

    if type_of_streams == "video":
        streams_list = formatted_video_streams(streams)
        streams_list = sorted_streams_desc(streams_list, "video")
    else:
        streams_list = formatted_audio_streams(streams)
        streams_list = sorted_streams_desc(streams_list, "audio")
    return streams_list, type_of_streams


def formatted_video_streams(streams):

    streams_list = []

    for stream in streams:
        streams_list.append({"itag": stream.itag,
                             "res": stream.resolution,
                             "fps": stream.fps,
                             "extension": stream.mime_type[6:],
                             "size": stream.filesize_mb})

    return streams_list


def formatted_video_streams(streams):

    streams_list = []

    for stream in streams:
        streams_list.append({"itag": stream.itag,
                             "res": stream.resolution,
                             "fps": stream.fps,
                             "extension": stream.mime_type[6:],
                             "video_codec": stream.video_codec,
                             "size": stream.filesize_mb})

    return streams_list


def formatted_audio_streams(streams):

    streams_list = []

    for stream in streams:
        streams_list.append({"itag": stream.itag,
                             "abr": stream.abr,
                             "extension": stream.mime_type[6:],
                             "size": stream.filesize_mb})

    return streams_list


def sorted_streams_desc(streams_list, type):
    '''Orders the streams based on Quality then The Extension'''
    if type == "video":
        return sorted(streams_list, key=lambda x: (int(x["res"][:-1]), x["extension"]))[::-1]
    else:
        return sorted(streams_list, key=lambda x: (int(x["abr"][:-4]), x["extension"]))[::-1]


def streams_print(streams):
    '''prints the choices to the user'''
    streams_list, type_of_streams = format_streams(streams)

    if type_of_streams == "video":
        for stream_index in range(len(streams_list)):
            stream = streams_list[stream_index]
            print(f"{str((stream_index + 1)).zfill(2) }: {stream['res'].center(5)}, {stream['fps']} FPS - {stream['extension'].ljust(5)} size: {stream['size']} MB")
    else:
        for stream_index in range(len(streams_list)):
            stream = streams_list[stream_index]
            print(f"{str((stream_index + 1)).zfill(2) }: {stream['ab'].center(7)} - {stream['extension'].ljust(5)} size: {stream['size']} MB")
