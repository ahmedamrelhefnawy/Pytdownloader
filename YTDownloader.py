import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, r'libs\modules')

sys.path.append(vendor_dir)

from libs.Storing_place import Place
from libs import downloader
import libs.modules.tkinter as tk
from libs.modules.tkinter import filedialog

def change_default():
    
    path = filedialog.askdirectory(title='Select Folder') # Open browse window
    
    if path:  # Check if a folder was selected
        
        file = open("configuration", 'w')
        file.write(path) # Saves the directory to the file
        
        file.close() # Closes the file


# Necessary to open browse menu
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

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
        change_default()
        import YTDownloader
        break
    elif user_input == "4":
        break

    else:
        user_input = input("Please enter a valid choice number: ")

root.destroy() # Close the Tkinter window
