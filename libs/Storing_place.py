import os


class Place:
    """on_complete_Callback function"""
    """Choosing the place of storing youtube videos, and changing this place whenever wanted."""

    def __init__(self):
        self.place = "E:\Youtube Videos"

    # This function is used to open the place where the video has been downloaded.
    def open_folder(self, chunk, chunk_):
        print("Download done")
        os.startfile(self.place)
        input("Another video?")
        if input == "yes":
            return   # Here we will put the downloading function so that we download again.
        else:
            return

    # If the user wanted to change the place of storing, we use this function.
    def choose_place(self, plac):
        self.place = plac
        return self.place
