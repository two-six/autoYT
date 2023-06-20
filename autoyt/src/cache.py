#! /usr/bin/python

import toml
import os

CACHE_DIR = "cache/"

def list_channels():
    try:
        f = open(CACHE_DIR + "cache.toml", "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        return data
    except FileNotFoundError:
        init_cache()
        print("No saved channels")
    except:
        print("Error reading cache")

def add_channel(data, channel):
    if data['channels'] is None:
        return channel
    data['channels'].update(channel)
    return data

def remove_channel(data: dict, channel: str):
    if data.get('channels') is not None and data['channels'].get(channel) is not None:
        data['channels'].pop(channel, None)
    return data

def read():
    try:
        f = open(CACHE_DIR + "cache.toml", "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        if data.get("channels") is None:
            data.update({"channels": {}})
        return data
    except FileNotFoundError:
        init_cache()
        return {"channels": {}}

def save(data):
    try:
        f = open(CACHE_DIR + "cache.toml", "w", encoding="utf-8")
        f.write(toml.dumps(data))
        f.close()
    except:
        print("Error saving cache")

def init_cache():
    f = open(CACHE_DIR + "cache.toml", "w", encoding="utf-8")
    f.write(toml.dumps({"channels": {}}))
    f.close()

def export_saved():
    f = open(CACHE_DIR + "cache.toml", "r", encoding="utf-8")
    data = toml.loads(f.read())
    f.close()
    result = ""
    for channel in data['channels']:
        result += "\"" + channel + "\" "
    return result

def remove_all():
    os.remove(CACHE_DIR + "cache.toml")