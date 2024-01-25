from tkinter import filedialog
def browse_folder():
    with open("configuration", 'w') as file:
        file.write(filedialog.askdirectory())