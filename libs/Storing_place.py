import os
from User import User
        
class Place:
    """on_complete_Callback function"""
    """Choosing the place of storing youtube videos, and changing this place whenever wanted."""
    
    place = open("./cache/configuration",'r').readline() if open("./cache/configuration",'r').readline() else os.path.join(os.path.expanduser("~"), "Desktop")

    @staticmethod
    def open_folder(chunk, chunk_):
        
        print("\nDownload done")
        os.startfile(Place.place)
        user_input = input("Another video ? (y/n): ").lower()[0]
        
        #TODO: Replace this with code starter
        if user_input == "y":
            import YTDownloader
        else:
            exit()

    @staticmethod
    def ask_change_place():
        user_input = User.get_bool_input("Would you like to download it in a different folder ? (y/n): ")
        if user_input:
            Place.change_place()
        
    # If the user wanted to change the place of storing, we use this function.
    @staticmethod
    def change_place():
        
        import sys
        from PyQt5.QtWidgets import QFileDialog, QApplication
        
        app = QApplication(sys.argv)
        
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)

        if folder_dialog.exec_():
            Place.place = folder_dialog.selectedFiles()[0]
            
        app.quit()
    
    @staticmethod
    def change_default():
        import sys
        from PyQt5.QtWidgets import QFileDialog, QApplication
        
        app = QApplication(sys.argv)
        
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)

        if folder_dialog.exec_():
            
            Place.place = folder_dialog.selectedFiles()[0]
            
            file = open('configuration', 'w')
            file.write(Place.place)
            file.close()
        
        app.quit()