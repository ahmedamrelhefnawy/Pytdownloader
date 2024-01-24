def format_streams(streams):
    streams_list = []
    for stream in streams:
        streams_list.append(
            {"res": stream.resolution, "fps": stream.fps, "extension": stream.mime_type[7:], "size": stream.filesize_mb,
             "itag": stream.itag})

    return streams_list
