from pytube import Playlist

def get_playlist_urls(playlist_url):
    """
    Extracts video URLs from a given YouTube playlist URL.

    Args:
    playlist_url (str): URL of the YouTube playlist.

    Returns:
    list: A list of video URLs contained in the playlist.
    """
    playlist = Playlist(playlist_url)

    # This fixes the empty playlist.videos list
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

    return [url for url in playlist.video_urls]