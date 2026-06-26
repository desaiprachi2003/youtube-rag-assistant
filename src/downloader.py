from yt_dlp import YoutubeDL
from src.config import DATA_DIR


def download_audio(url):
    options = {
        "format": "bestaudio/best",
        "outtmpl": str(DATA_DIR / "%(title)s.%(ext)s"),
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)

        filename = ydl.prepare_filename(info)

    metadata = {
        "video_id": info["id"],
        "title": info["title"],
        "channel": info["channel"],
        "url": url,
        "duration": info["duration"],
        "language": info.get("language", "unknown")
    }

    return filename, metadata