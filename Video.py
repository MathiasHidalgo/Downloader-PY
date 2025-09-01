import yt_dlp

def download(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',   # Can change to 'webm' if needed
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'nocheckcertificate': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download complete!")
    except Exception as e:
        print(f"Download error: {e}")

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
