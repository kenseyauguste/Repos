import yt_dlp

def convert_youtube_to_mp3(youtube_url, output_path='/Users/kenseyauguste/Downloads'):
    """
    Downloads the audio from a YouTube URL and converts it to MP3.

    Args:
        youtube_url (str): The URL of the YouTube video.
        output_path (str): The directory to save the MP3 file. Defaults to the current directory.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Adjust quality as needed (e.g., '320')
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Successfully downloaded and converted '{youtube_url}' to MP3.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    convert_youtube_to_mp3(url)