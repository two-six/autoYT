#! /usr/bin/python

import yt_dlp
import os
from datetime import datetime, timedelta
import youtubeinfo as yi
import config
from pathlib import Path

# video_info {'publishDate', 'url', 'channel', 'title', 'id'}
def download(video_info: dict, video_format: str, directory: str):
    upload_date = video_info['publishDate'].strftime("%Y_%m_%d")
    path = os.path.join(directory, upload_date)
    path = os.path.join(path, video_info['channel'])

    video_info['title'] = video_info['title'].replace("\\", "")
    video_info['title'] = video_info['title'].replace("/", "")
    video_info['title'] = video_info['title'].replace(":", "")
    video_info['title'] = video_info['title'].replace("*", "")
    video_info['title'] = video_info['title'].replace("?", "")
    video_info['title'] = video_info['title'].replace("\"", "")
    video_info['title'] = video_info['title'].replace("<", "")
    video_info['title'] = video_info['title'].replace(">", "")
    video_info['title'] = video_info['title'].replace("|", "")

    ydl_opts = {
        "format": video_format,
        "paths": {"home": path},
        "quiet": True,
        "outtmpl": {"default": "PLACEHOLDER.%(ext)s"}
        # "progress_hooks": {
        #     "status": True,
        #     "filename": True,
        #     "eta": True
        # }
    }
    if not os.path.isdir(directory):
        os.mkdir(directory)
    if not os.path.isdir(os.path.join(directory, upload_date)):
        os.mkdir(os.path.join(directory, upload_date))
    if not os.path.isdir(path):
        os.mkdir(path)
    file_name = video_info['title']
    for file in os.listdir(path):
        if Path(file).stem == file_name:
            return
    print(upload_date + "/" + video_info['channel'] + "/" + video_info['title'] + ": Downloading...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(video_info['url'])
        for file in os.listdir(path):
            if Path(file).stem  == "PLACEHOLDER":
                os.rename(os.path.join(path, file), os.path.join(path, video_info['title'] + os.path.splitext(file)[1]))
    except:
        print("Couldn't download video: " + video_info['url'])
        for file in os.listdir(path):
            if Path(file).stem  == "PLACEHOLDER":
                os.rename(os.path.join(path, file), os.path.join(path, video_info['title'] + os.path.splitext(file)[1]))

def download_channel(id: str, video_format: str, directory: str, max_video_age: int, limit: int):
    videos = yi.find_channel_videos(id, limit)
    for video in videos:
        publish_date = datetime.strptime(video['publishDate'], "%Y-%m-%d")
        if max_video_age == 0:
            download({'publishDate': publish_date, 'channel': video['channel']['name'], 'url': video['link'], 'title': video['title'], 'id': video['id']}, video_format, directory)
        else:
            now = datetime.today()
            delta = now - publish_date
            if delta.days <= max_video_age:
                download({'publishDate': publish_date, 'channel': video['channel']['name'], 'url': video['link'], 'title': video['title'], 'id': video['id']}, video_format, directory)
