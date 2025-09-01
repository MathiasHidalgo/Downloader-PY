import yt_dlp

def download_best_quality_audio(url):
    """
    Downloads the best available quality audio from the given URL.

    Args:
        url (str): The URL of the video/audio to download.
        output_template (str): The template for the output filename.
                               e.g., '%(title)s.%(ext)s' for title.extension
                               or 'audio_files/%(title)s.%(ext)s' if you
                               want a subfolder.
    """
    ydl_opts = {
        'format': 'bestaudio/best',      # Selects the best audio format
        'extract_audio': True,           # Extracts audio from video files
        'audio_format': 'best',          # Attempts to keep original audio format
                                         # or converts to the best quality supported
        'audio_quality': 0,              # 0 is the best quality (lossless if available)
                                         # (Relevant if re-encoding is necessary)
        #'outtmpl': output_template,      # Output file path template
        'noplaylist': True,              # Only download the video if it's part of a playlist
        'nocheckcertificate': True,      # Useful if you encounter SSL errors (use with caution)
                                         # e.g., r'C:\path\to\ffmpeg\bin\ffmpeg.exe' on Windows
                                         # or '/usr/local/bin/ffmpeg' on macOS/Linux
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # Use FFmpeg to extract audio
            'preferredcodec': 'best',    # Prefer the best audio codec
            'preferredquality': '0',     # 0 is the highest quality
        }],
        # You might want to consider 'keepvideo': False if you only want the audio
        # and don't need the intermediate video file if it's downloaded first.
        # 'keepvideo': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'audio')
            # The 'ext' might be the original video extension before audio extraction.
            # It's better to rely on the actual downloaded file's extension if you need it.
            # For simplicity, we'll assume a common audio extension like 'opus' or 'm4a'
            # as yt-dlp will try to keep the original best quality.
            # If you need the exact final extension, you might have to check after download
            # or rely on the postprocessor output if available in info_dict.
            print(f"Downloaded best quality audio for '{video_title}' using template '{output_template}'")

    except Exception as e:
        print(f"An error occurred: {e}")


run = True
while run:
    link = input("Enter YouTube link to download (or type 'EXIT' to quit): ")
    if "youtube.com" in link or "youtu.be" in link:
        print("Downloading...")
        download_best_quality_audio(link)
    elif link.upper() == "EXIT":
        print("Exiting program. Thank you!")
        run = False
    else:
        print("Invalid YouTube link. Try again!")

#if __name__ == "__main__":
    #video_url = input("Enter the video URL to download audio from: ")
    # Example usage:
    # This will save the audio as "<Video Title>.<best_audio_extension>" in the current directory.
    #download_best_quality_audio(video_url)

    # If you want to specify a subfolder (e.g., 'audio_downloads')
    # Make sure this folder exists or is created by your external handling.
    # download_best_quality_audio(video_url, output_template='audio_downloads/%(title)s.%(ext)s')
