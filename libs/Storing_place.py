import os

        
class Place:
    """on_complete_Callback function"""
    """Choosing the place of storing youtube videos, and changing this place whenever wanted."""

    def __init__(self):
        
        output = open("configuration",'r').readline()
        self.place = output if output else os.path.join(os.path.expanduser("~"), "Desktop")

    # This function is used to open the place where the video has been downloaded.
    def open_folder(self, chunk, chunk_):
        
        print("Download done")
        os.startfile(self.place)
        user_input = input("Another video ? (y/n): ").lower()[0]
        
        if user_input == "y":
            import YTDownloader
        else:
            exit()

    # If the user wanted to change the place of storing, we use this function.
    def choose_place(self):
        
        from .modules import tkinter as tk
        from .modules.tkinter import filedialog
        
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window
        
        self.place = filedialog.askdirectory() # Open browse window