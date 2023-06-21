#! /usr/bin/python

import os
import shutil
from datetime import datetime, timedelta

def remove_old_videos(days: int, directory: str):
    if days == 0:
        return
    max_date = datetime.today() - timedelta(days=days)
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        if os.path.isdir(d):
            if datetime.strptime(file, "%Y_%m_%d") < max_date:
                shutil.rmtree(d)

def remove_all_videos(directory: str):
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        shutil.rmtree(d)

def find_videos(name: str, directory: str):
    result = ""
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        d = os.path.join(d, name) 
        if os.path.isdir(d):
            for vid_name in os.listdir(d):
                result += os.path.join(d, vid_name) + "\n"
    return result

def remove_invalid_videos(saved_channels: list, directory: str):
    for dir in os.listdir(directory):
        d = os.path.join(directory, dir)
        for channel in os.listdir(d):
            if not channel in saved_channels:
                shutil.rmtree(os.path.join(d, channel))
    for dir in os.listdir(directory):
        path = os.path.join(directory, dir)
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

def remove_from_channel(channel: str, directory: str):
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        for ch in os.listdir(d):
            if ch == channel:
                shutil.rmtree(os.path.join(d, ch)) 

def remove_empty_dirs(directory: str):
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        if len(os.listdir(d)) == 0:
            shutil.rmtree(d)