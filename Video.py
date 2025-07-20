import yt_dlp


def download(link):
    # set the correct options before download
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Selects best video and best audio, then merges
        'merge_output_format': 'webm',         # Forces the output container to WebM (or 'mkv')
        'outtmpl':'%(title)s.%(ext)s', # Output file path template
        'noplaylist': True,                     # Only download the video if it's part of a playlist
        'nocheckcertificate': True,             # Useful if you encounter SSL errors (use with caution)
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm'
        }]
    }
    try:
        # attempt to download without errors
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download complete!")
    except:
        # message to be printed in the case of error
        print("Download error!")

run = True
while run:
    link = input("Enter YouTube link to download (or type 'EXIT' to quit): ")
    if "youtube.com" in link or "youtu.be" in link:
        print("Downloading...")
        download(link)
    elif link.upper() == "EXIT":
        print("Exiting program. Thank you!")
        run = False
    else:
        print("Invalid YouTube link. Try again!")


