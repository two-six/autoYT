#! /usr/bin/python

import yt_dlp

def download(url: str, video_format: str, directory: str):
    ydl_opts = {
        "format": video_format,
        "paths": {"home": directory}
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)