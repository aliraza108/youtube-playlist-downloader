from pytube import Playlist, YouTube

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download(output_path=output_path)
        print(f'Successfully downloaded: {yt.title}')
    except Exception as e:
        print(f'Error downloading {video_url}: {e}')

def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url)
    print(f'Downloading playlist: {playlist.title}')
    
    for video_url in playlist.video_urls:
        download_video(video_url, output_path)

# Example usage
playlist_url = 'https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg'
output_path = 'Downloads'
download_playlist(playlist_url, output_path)
