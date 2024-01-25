<<<<<<< HEAD
from libs import streams_manipulate, downloader
from tkinter import filedialog
from tkinter import filedialog
=======
from pytube import YouTube
>>>>>>> 8b041c22e6ec46d95c5ed4f9b9b31c9108e24e3f

def browse_folder():
    path = filedialog.askdirectory()
    with open("configuration", 'w') as file:
        file.write(path)
        
print('''1: Single Video
2: Playlist
3: Change download folder''')

functions = [downloader.single_download,1 ,browse_folder]
user_input = int(input("Choose by number: ")) - 1

<<<<<<< HEAD
chosen = functions[user_input]
chosen()
=======
>>>>>>> 8b041c22e6ec46d95c5ed4f9b9b31c9108e24e3f
