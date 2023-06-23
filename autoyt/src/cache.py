import toml
import os

def list_channels(directory: str):
    path = os.path.join(directory, "cache.toml")
    try:
        f = open(path, "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        return data
    except FileNotFoundError:
        init_cache(directory)
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

def read(directory: str):
    path = os.path.join(directory, "cache.toml")
    try:
        f = open(path, "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        if data.get("channels") is None:
            data.update({"channels": {}})
        return data
    except FileNotFoundError:
        init_cache(directory)
        return {"channels": {}}

def save(data, directory: str):
    path = os.path.join(directory, "cache.toml")
    try:
        f = open(path, "w", encoding="utf-8")
        f.write(toml.dumps(data))
        f.close()
    except:
        print("Error saving cache")

def init_cache(directory: str):
    path = os.path.join(directory, "cache.toml")
    f = open(path, "w", encoding="utf-8")
    f.write(toml.dumps({"channels": {}}))
    f.close()

def export_saved(directory: str):
    path = os.path.join(directory, "cache.toml")
    f = open(path, "r", encoding="utf-8")
    data = toml.loads(f.read())
    f.close()
    result = ""
    for channel in data['channels']:
        result += "\"" + channel + "\" "
    return result

def remove_all(directory: str):
    path = os.path.join(directory, "cache.toml")
    os.remove(path)

def get_channel_name(id: str, data: dict):
    return data['channels'][id]['title']

def get_saved_channels(data: dict):
    result = list()
    for id in data['channels']:
        result.append(data['channels'][id]['title'])
    return result
