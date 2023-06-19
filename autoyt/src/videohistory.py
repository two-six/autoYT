#! /usr/bin/py

from datetime import date
import toml

HISTORY_PATH = "cache/"

def add_video(data: dict, video_id: str, name: str, folder_name: str):
    now = date.today().strftime("%m-%d-%Y ")
    if data[now] is None:
        tmp_data = {now: {}}
        tmp_data.update(data)
        data = tmp_data
    
    data[now].update({video_id: {"name": name, "folder": folder_name}})
    return data
        

def read():
    try:
        f = open(HISTORY_PATH + "history.toml", "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        return data
    except FileNotFoundError:
        init_history()
        return {date.today().strftime("%m-%d%-%Y "): []}
    except:
        print("Error reading history data")

def save(data: dict):
    try:
        f = open(HISTORY_PATH + "history.toml", "w", encoding="utf-8")
        f.write(toml.dumps(data))
        f.close()
    except:
        print("Error saving history data")

def init_history():
    now = date.today().strftime("%m-%d-%Y ")
    default_content = {now: {}}
    f = open(HISTORY_PATH + "history.toml", "w", encoding="utf-8")
    f.write(toml.dumps(default_content))
    f.close()
    return default_content