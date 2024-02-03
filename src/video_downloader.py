from pytube import YouTube
import os
import logging

def download_videos(video_urls, download_path):
    """
    Downloads videos from a list of YouTube URLs to a specified path.

    Args:
    video_urls (list_): List of YouTube video URLs.
    download_path (str): Path to save the downloaded videos.
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    unavailable_videos = 0
    for url in video_urls:
        try:
            yt = YouTube(url)
            stream =  yt.streams.filter(progressive=True, file_extension= 'mp4').order_by('resolution').desc().first()
            output_file_path = os.path.join(download_path, stream.default_filename)

            if not os.path.exists(output_file_path):
                stream.download(download_path)
                logging.info(f"Downloaded: {url}")
                print(f"Downloaded: {yt.title}")
            else:
                logging.info(f"Already exists, skipping: {url}")
                print(f"Already downloaded, skipping: {yt.title}")

        except Exception as e:
            logging.error(f"Failed to download {url}: {str(e)}")
            print(f"Error downloading {yt.title}: {str(e)}")
            unavailable_videos += 1
    
    return unavailable_videos