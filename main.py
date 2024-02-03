
import argparse
from src.playlist_parser import get_playlist_urls
from src.video_downloader import download_videos
from src.video_to_mp3_converter import convert_to_mp3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='YouTube Playlist Downloader and Converter')
    parser.add_argument('playlist_url', help='YouTube Playlist URL')
    parser.add_argument('--download_path', default='./download', help="Path to save downloaded videos")
    parser.add_argument('--mp3_path', default='./mp3', help='Path to save converted MP3 files')

    args = parser.parse_args()

    print("Starting YouTube Playlist Downloader and Converter...")
    video_urls = get_playlist_urls(args.playlist_url)
    print(f"Found {len(video_urls)} videos in the playlist")

    unavailable_videos = download_videos(video_urls, args.download_path)

    # Converting downloaded videos to MP3
    for filename in os.listdir(args.download_path):
        if filename.endswith(".mp4"):
            video_file_path = os.path.join(args.download_path, filename)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_file_path = os.path.join(args.mp3_path, mp3_filename)

            logging.info(f"Converting {video_file_path} to {mp3_file_path}")
            convert_to_mp3(video_file_path, mp3_file_path)

    if unavailable_videos > 0:
        print(f"\n{unavailable_videos} videos were unavailable and could not be downloaded.")

    print("\nDownload and conversion process completed.")
    print(f"Total videos processed: {len(video_urls)}")


if __name__ == '__main__':
    main()

# playlist_url = 'https://www.youtube.com/playlist?list=PLu9tImInkmpNxzcOJjuQgzaiaDeXLxlyb'
# download_path = './download'
# mp3_path = './mp3'

# video_urls = get_playlist_urls(playlist_url)
# print("URLs to download: ", video_urls)

# download_videos(video_urls, download_path)

