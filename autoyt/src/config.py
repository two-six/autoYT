#! /usr/bin/python

import toml
import os

def get_download_dir():
    try:
        f = open("./config/config.toml")
        data = toml.loads(f.read())
        f.close()
        return data['download_dir']
    except:
        init()
        return './videos'

def get_cache_dir():
    try:
        f = open("./config/config.toml")
        data = toml.loads(f.read())
        f.close()
        return data['cache_dir']
    except:
        init()
        return './cache'
    
def get_all():
    try:
        f = open("./config/config.toml")
        data = toml.loads(f.read())
        f.close()
        return data
    except:
        init()
        return {"download_dir": "./videos", "cache_dir": "./cache"}

def get_download_quality(channel: str):
    try:
        f = open("./config/config.toml")
        data = toml.loads(f.read())
        f.close()
        if data.get(channel) is None:
            return data.get("quality")
        if data[channel].get("quality") is None:
            return data.get("quality")
    except:
        init()
        return "ba+bv"

def init():
    try:
        f = open("./config/config.toml", "w")
        f.write(toml.dumps({"download_dir": "./videos", "cache_dir": "./cache", "quality": "ba+bv"}))
        f.close()
    except:
        print("Couldn't create config file")

def get_config_dir():
    return os.path.join(os.getcwd(), 'config/config.toml')