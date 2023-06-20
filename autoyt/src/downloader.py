#! /usr/bin/python

import yt_dlp
import os
from datetime import date, datetime
import youtubeinfo as yi
# video_info {'uploadDate', 'url', 'channel'}
def download(video_info: dict, video_format: str, directory: str):
    upload_date = video_info['uploadDate'].strftime("%Y_%m_%d")
    ydl_opts = {
        "format": video_format,
        "paths": {"home": directory + "/" + upload_date + "/" + video_info['channel']}
    }
    if not os.path.isdir(directory + "/" + upload_date):
        os.mkdir(directory + "/" + upload_date)
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(video_info['url'])
    except:
        print("Couldn't download video: " + video_info['url'])

def download_channel(id: str, video_format: str, directory: str):
    videos = yi.find_channel_videos(id, 5)
    for video in videos:
        download({'uploadDate': datetime.strptime(video['uploadDate'], '%Y-%m-%d'), 'channel': video['channel']['name'], 'url': video['link']}, video_format, directory)