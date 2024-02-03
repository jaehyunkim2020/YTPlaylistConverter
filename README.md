# YTPlaylistConverter
a Python script that downloads and converts YouTube playlist videos into MP3 files


## Introduction

This script allows users to download videos from a YouTube playlist and convert them into MP3 format. It's designed to be easy to use, providing a command-line interface for efficient processing.

I have always enjoyed having the music files directly in my phone instead of using services like YouTube Music or Spotify due to the ads and subscription fees which was something I didn't want to pay for as a broke college student.

## Installation

### Pre-requisites
- Python 3.x
- pip (Python package manager)

### Set up

1. Clone the repository: `git clone <your-repo-link>`

2. Navigate to the cloned directory: `cd <your-repo-directory>`

3. Install required packages: `pip install -r requirements.txt`

## Usage

To use the script, run the following command in the terminal:

`python main.py <YouTube Playlist URL> --download_path <path-to-download-folder> --mp3_path <path-to-mp3-folder>`

### Example
`python main.py https://www.youtube.com/playlist?list=<YOUR_PLAYLIST_ID> --download_path ./downloads --mp3_path ./mp3`

## Features
- **Download Videos**: Downloads all videos from a provided YouTube playlist URL.
- **Convert to MP3**: Converts the downloaded videos into MP3 format.
- **Error Handling**: Gracefully handles and logs errors during download and conversion.
- **Command-Line Interface**: Easy to use command-line interface.

## Contributing
Contributions to the project are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

- jaehyunkim2020@gmail.com
- https://www.linkedin.com/in/jaehyunkim2020/

## Limitations (for now 🙂)

- The script cannot retrieve metadata to include artists name to the file name.
- The script cannot clean the file name to get rid of unnecessary characters (e.g. if the video title has something like "(Official Audio)")

## Future Features

1. GUI to make the program user-friendly to those who aren't familiar with using the command line
2. Also script Spotify playlists
