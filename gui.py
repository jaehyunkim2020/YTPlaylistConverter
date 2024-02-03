import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from src.playlist_parser import get_playlist_urls
from src.video_downloader import download_videos
from src.video_to_mp3_converter import convert_to_mp3
import os
import threading

def browse_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

def on_entry_click(event, default_text):
    """Function to clear the placeholder text on focus"""
    if event.widget.get() == default_text:
        event.widget.delete(0, "end")

def create_labeled_entry(parent, label_text, row, column, placeholder_text=""):
    """Helper function to create a labeled entry with a placeholder"""
    tk.Label(parent, text=label_text).grid(row=row, column=column, sticky="w", padx=5, pady=5)
    entry = tk.Entry(parent, width=40)
    entry.insert(0, placeholder_text)
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, placeholder_text))
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry


def update_progress(current, total, title, error=None):
    # Update the GUI based on the progress
    progress['value'] = (current / total) * 100
    if error:
        status_label.config(text=f"Error with {title}: {error}")
    else:
        status_label.config(text=f"Processing {title}...")

def download_and_convert():
    # Get input values from the GUI
    playlist_url = url_entry.get()
    download_path = download_path_entry.get()
    mp3_path = mp3_path_entry.get()

    if not playlist_url or not download_path or not mp3_path:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    def task():
        try:
            video_urls = get_playlist_urls(playlist_url)
            unavailable_videos = download_videos(video_urls, download_path, progress_callback=update_progress)
            for filename in os.listdir(download_path):
                if filename.endswith(".mp4"):
                    video_file_path = os.path.join(download_path, filename)
                    mp3_filename = os.path.splitext(filename)[0] + ".mp3"
                    mp3_file_path = os.path.join(mp3_path, mp3_filename)
                    convert_to_mp3(video_file_path, mp3_file_path, progress_callback=update_progress)
            messagebox.showinfo("Complete", "Download and conversion process completed.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    threading.Thread(target=task).start()

app = tk.Tk()
app.title("YTPlaylistConverter")
app.geometry("600x400")  # Adjust the size as needed

# Create and place GUI elements
url_entry = create_labeled_entry(app, "YouTube Playlist URL:", 0, 0, "Enter Playlist URL")

download_path_entry = create_labeled_entry(app, "Download Path:", 1, 0, "Enter Download Path")
download_browse_button = tk.Button(app, text="Browse", command=lambda: browse_folder(download_path_entry))
download_browse_button.grid(row=1, column=2)

mp3_path_entry = create_labeled_entry(app, "MP3 Save Path:", 2, 0, "Enter MP3 Save Path")
mp3_browse_button = tk.Button(app, text="Browse", command=lambda: browse_folder(mp3_path_entry))
mp3_browse_button.grid(row=2, column=2)

progress = ttk.Progressbar(app, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

status_label = tk.Label(app, text="")
status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

download_button = tk.Button(app, text="Download and Convert", command=download_and_convert)
download_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

url_entry.config(fg="grey")
download_path_entry.config(fg="grey")
mp3_path_entry.config(fg="grey")

# And a progress bar (you'll need to import ttk from tkinter for this)
# from tkinter import ttk
# progress = ttk.Progressbar(app, orient=tk.HORIZONTAL, length=100, mode='determinate')
# progress.pack()


if __name__ == "__main__":
    app.mainloop