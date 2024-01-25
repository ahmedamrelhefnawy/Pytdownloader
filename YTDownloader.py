from libs import streams_manipulate, downloader
from tkinter import filedialog
from tkinter import filedialog

def browse_folder():
    path = filedialog.askdirectory()
    with open("configuration", 'w') as file:
        file.write(path)
        
print('''1: Single Video
2: Playlist
3: Change download folder''')

functions = [downloader.single_download,1 ,browse_folder]
user_input = int(input("Choose by number: ")) - 1

chosen = functions[user_input]
chosen()