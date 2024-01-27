import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
modules_dir = os.path.join(parent_dir, r'libs\modules')

sys.path.append(modules_dir)

from libs.Storing_place import Place
from libs import downloader
import libs.modules.tkinter as tk
from libs.modules.tkinter import filedialog
from PyQt5.QtWidgets import QFileDialog

download_folder = Place()

print(f'''1: Single Video
2: Playlist
3: Change download folder
    Current: {download_folder.place}

4: Close the app''')

user_input = input("\nChoose by number: ")

while True:
    if user_input == "1":
        downloader.single_download(download_folder)
        break
    elif user_input == "2":
        downloader.playlist_download(download_folder)
    elif user_input == "3":
        download_folder.change_default()
        print(f"\nDefault Folder is set to:\n{download_folder.place}")
        user_input = input("\nChoose another Option: ")

    elif user_input == "4":
        break

    else:
        user_input = input("Please enter a valid choice number:")

