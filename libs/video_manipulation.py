import os
from modules.moviepy.editor import VideoFileClip, AudioFileClip 

def combine_video_audio(video_file, audio_file, output_file_name):
    video_stream = VideoFileClip(video_file)
    audio_stream = AudioFileClip(audio_file)

    # Concatenate the video stream with the audio stream
    final_video = video_stream.set_audio(audio_stream)

    # Export the final video with audio
    final_video.write_videofile(output_file_name + ".mp4")

    os.remove(video_file)
    os.remove(audio_file)