import yt_dlp
import os

DOWNLOAD_DIR = "downloads"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def get_formats(url):
    """Fetch available formats (video & audio) without downloading"""
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        return formats, info

def download_video(url, format_code, progress_hook):
    """Download the video with given format_code and report progress"""
    ydl_opts = {
        'format': format_code,
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'noplaylist': True,
        'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        return file_path, info
