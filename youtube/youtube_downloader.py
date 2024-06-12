import pytube
from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, TextClip, ImageSequenceClip, CompositeVideoClip, concatenate_videoclips

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()


def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links


def download_convert_youtube_to_mp3():
    print("Welcome to NeuralNine YouTube Downloader and Converter v0.2 Alpha")
    print("Loading...")
    print('''
    What do you want?

    (1) Download YouTube Videos Manually
    (2) Download a YouTube Playlist
    (3) Download YouTube Videos and Convert Into MP3

    Downloading copyrighted YouTube videos is illegal!
    I am not responsible for your downloads! Go at your own risk!

    Copyright (c) NeuralNine 2020
    ''')

    choice = input("Choice: ")

    if choice == "1" or choice == "2":
        quality = input("Please choose a quality (low, medium, high, very high):")
        if choice == "2":
            link = input("Enter the link to the playlist: ")
            print("Downloading playlist...")
            download_playlist(link, quality)
            print("Download finished!")
        if choice == "1":
            links = input_links()
            for link in links:
                download_video(link, quality)
    elif choice == "3":
        links = input_links()
        for link in links:
            print("Downloading...")
            filename = download_video(link, 'low')
            print("Converting...")
            convert_to_mp3(filename)
    else:
        print("Invalid input! Terminating...")

