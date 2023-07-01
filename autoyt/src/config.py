import toml
import os

CONFIG_PATH = os.path.join(os.path.expanduser('~'), ".config/autoyt/config.toml")
CACHE_DIR = os.path.join(os.path.expanduser('~'), ".cache/autoyt")
VIDEOS_PATH = os.path.join(os.path.expanduser('~'), "Videos/autoYT")

def get_download_dir():
    try:
        f = open(os.path.join(CONFIG_PATH))
        data = toml.loads(f.read())
        f.close()
        return data['download_dir']
    except:
        init()
        return VIDEOS_PATH

def get_cache_dir():
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        return data['cache_dir']
    except:
        init()
        return os.path.join(os.path.expanduser('~'), ".cache/autoyt/")
    
def get_all():
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        return data
    except:
        init()
        return {"download_dir": VIDEOS_PATH, "cache_dir": CACHE_DIR, "quality": "ba+bv[height<=?1080]", "max_video_age": 5, "max_downloaded_channel_videos": 5, "delete_videos_age": 5, "channels_check_break": 600}

def get_max_downloaded_channel_videos(channel: str):
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        if data.get(channel) is None:
            return data.get("max_downloaded_channel_videos")
        if data[channel].get("max_downloaded_channel_videos") is None:
            return data.get("max_downloaded_channel_videos")
    except:
        init()
        return 5


def get_download_quality(channel: str):
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        if data.get(channel) is None:
            return data.get("quality")
        if data[channel].get("quality") is None:
            return data.get("quality")
    except:
        init()
        return "ba+bv[height<=?1080]"

def get_max_video_age():
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        return data["max_video_age"]
    except:
        return 5

def get_delete_videos_age():
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        return data["delete_videos_age"]
    except:
        return 5

def get_channels_check_break():
    try:
        f = open(CONFIG_PATH)
        data = toml.loads(f.read())
        f.close()
        return data['channels_check_break']
    except:
        return 600

def init():
    try:
        os.makedirs(os.path.join(os.path.expanduser('~'), ".config/autoyt"), exist_ok=True)
        f = open(CONFIG_PATH, "w")
        f.write(toml.dumps({"download_dir": VIDEOS_PATH, "cache_dir": CACHE_DIR, "quality": "ba+bv[height<=?1080]", "max_video_age": 5, "delete_videos_age": 5, "channels_check_break": 600}))
        f.close()
    except:
        print("Couldn't create config file")

def get_config_dir():
    return os.path.join(os.path.expanduser('~'), ".config/autoyt")