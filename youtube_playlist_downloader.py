from pytube import Playlist
import os


url = str(input("\nSpecify you playlist URL\n"))
p = Playlist(url)
print(f'The number of videos in the Playlist: {p.length}')
BASE_DIR = os.getcwd()
SAVE_DIR = BASE_DIR + '/' + p.playlist_id
print(f'Playlist download: {p.title}')
video_number = 0
for video in p.videos:
    video_number += 1
    prefix = str(video_number) + '.'
    vid = video.streams.filter(progressive=True, file_extension='mp4', res='720p').first()
    print(prefix + ' Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
    vid.download(output_path=SAVE_DIR, filename_prefix=prefix)
    print('Video Downloaded')
print('Playlist download complete!')
