# Appending libs path
import os
import sys

# Adding modules path
parent_dir = os.path.abspath(os.path.dirname(__file__))
modules_dir = os.path.join(parent_dir, r'libs\modules')

sys.path.append(modules_dir)

while True:
    try:
        # Importing modules
        from libs.User import User
        from libs.Storing_place import Place
        from libs.aplaylist import aplaylist
        from libs.avideo import avideo
        from pytube import YouTube,Playlist
        from pytube.exceptions import VideoPrivate, VideoUnavailable, AgeRestrictedError, MembersOnly
        from libs.on_progress import on_progress

        break
    
    except ModuleNotFoundError:
        from libs.packages_installer import installer
        
        # Installing required libraries
        installer.install_requirements()

def download_playlist():
    while True:
        # try:
            user_input = input("\nEnter Playlist URL: ")
            print("\nLoading Playlist...\n")
            chosen_playlist = aplaylist(Playlist(user_input))
            
            download_format = chosen_playlist.choose_format()
            chosen_playlist.ask_download_mode(download_format)
            
            break
        # except:
        #     print(f"\n{'*'*59}\nCouldn't reach the playlist, Please try again...\n{'*'*59}\n")
        # finally:
        #     user_input = User.get_bool_input("\nDownload Another Playlist? (Y/n): ")
        #     if user_input == False:
        #         return


def download_video():
    while True:
        try:
            user_input = input("\nEnter video URL: ")
            print("\nLoading Video...")

            chosen_video = avideo(YouTube(user_input, on_progress_callback= on_progress))
            chosen_video.ask_download()
            break
        except AgeRestrictedError:
            print(f"\n{'*'*59}\n{'Age Restricted Video'.center(59)}\n{'*'*59}\n")
            
        except VideoPrivate:
            print(f"\n{'*'*59}\n{'Selected Video is Private'.center(59)}\n{'*'*59}\n")
            
        except VideoUnavailable:
            print(f"\n{'*'*59}\n{'Selected Video is Unavailable'.center(59)}\n{'*'*59}\n")
            
        except MembersOnly:
            print(f"\n{'*'*59}\n{'Selected Video is for Members Only .'.center(59)}\n{'*'*59}\n")
            
        except:
            print(f"\n{'*'*59}\n Couldn't reach the video, Please try again...\n{'*'*59}\n")
            
        finally:
            user_input = User.get_bool_input("\nDownload Another Video? (Y/n): ")
            if user_input == False:
                break
        
    



# Start
download_folder = Place()

def start_download():
    os.system("cls" if os.name == "nt" else "clear")

    print(f'''1: Download Video
2: Download Playlist
3: Change download folder
    Current: {download_folder.place}

4: Close the app''')

    user_input = User.get_int_input("\nChoose by number: ",[1, 2, 3, 4])
    while True:
        if user_input == 1:
            download_video()
            
            # Back to the main menu
            start_download()
            
        elif user_input == 2:
            download_playlist()
            
            # Back to the main menu
            start_download()
            
        elif user_input == 3:
            download_folder.change_default()
            print(f"\nDefault Folder is set to:\n{download_folder.place}")
            
            user_input = User.get_int_input("\nChoose another Option: ",[1, 2, 3, 4])
            
        else:
            exit()

start_download()