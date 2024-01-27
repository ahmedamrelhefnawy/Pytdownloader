import sys


def on_progress(stream, chunk, bytes_remaining):   # This function to show the status bar of downloading.
    """on_progress_Callback function"""

    total_size = stream.filesize
    total_size_mb = round(total_size / 1000000, 2)
    bytes_downloaded = total_size - bytes_remaining            # The remaining size in bytes.
    size_downloaded_mb = round(bytes_downloaded / 1000000, 2)  # The remaining size in mb.
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Downloaded: {round(pct_completed, 2)} %       Remaining: {round((bytes_remaining / 1000000), 2)} MB")


# def progress_func(stream, chunk, bytes_remaining):
#     """on_progress_Callback function"""

#     curr = stream.filesize - bytes_remaining
#     print(f"remaining size is : {round((bytes_remaining/1000000), 2)}")
#     done = int(50 * curr / stream.filesize)
#     sys.stdout.write("\r[{}{}] ".format('😁' * done, ' ' * (50-done)) )
#     print("")
#     sys.stdout.flush()
