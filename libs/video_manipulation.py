import os, sys
from .modules.moviepy.editor import VideoFileClip, AudioFileClip 

def combine_video_audio(video_file, audio_file):
    
    video_stream = VideoFileClip(video_file.replace(r'\\', '/'))
    audio_stream = AudioFileClip(audio_file)

    # Get file extension and output path
    output_file_extension = os.path.splitext(video_file)[1]
    output_file_path = rf"{os.path.dirname(video_file)}/combining video{output_file_extension}"
    
    print('\n')
    # Concatenate the video stream with the audio stream
    final_video = video_stream.set_audio(audio_stream)
    
    # Export the final video with audio
    final_video.write_videofile(output_file_path)
    remove_last_line()
    
    # Cleaning
    os.remove(video_file)
    os.remove(audio_file)
    
    os.rename(rf"{os.path.dirname(video_file)}/combining video{output_file_extension}", video_file)

def remove_last_line():
    sys.stdout.write("\033[F")  # Move cursor up one line
    sys.stdout.write("\033[K")  # Clear the line
    
if __name__ == "__main__":
    combine_video_audio("C:/Users/ahmed/Desktop/temp/video.mp4", "C:/Users/ahmed/Desktop/temp/audio.mp4","How Old Are Your Ears (Hearing Test)")