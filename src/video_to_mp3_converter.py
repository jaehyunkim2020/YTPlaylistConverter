from moviepy.editor import VideoFileClip
import os
import logging

def convert_to_mp3(video_path, mp3_path):
    """
    Converts a video file to an MP3 file.

    Args:
    video_path (str): Path to the video file.
    mp3_path (str): Path to save the converted MP3 file.
    """
    try:
        if not os.path.exists(os.path.dirname(mp3_path)):
            os.makedirs(os.path.dirname(mp3_path))
    
        with VideoFileClip(video_path) as video:
            video.audio.write_audiofile(mp3_path)
        logging.info(f"Conversion successful: {os.path.basename(mp3_path)}")
    
    except Exception as e:
        logging.error(f"Error converting {video_path} to MP3: {e}")