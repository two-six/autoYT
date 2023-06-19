#! /usr/bin/python

import toml

def list_channels():
    try:
        f = open("cache.toml", "r", encoding="utf-8")
        try: 
            data = toml.loads(f.read())
            for channel in data['channels']:
                print("Name: " + data['channels'][channel]['name'])
                print("Channel ID: " + channel)
                print()
        except:
            init_cache()
            print("No saved channels")
        f.close()
    except FileNotFoundError:
        init_cache()
        print("No saved channels")
    except:
        print("Error reading cache")

def add_channels(data, channel):
    if data['channels'] is None:
        return channel
    data['channels'].update(channel)
    return data

def read():
    try:
        f = open("cache.toml", "r", encoding="utf-8")
        data = toml.loads(f.read())
        f.close()
        if data.get("channels") is None:
            data.update({"channels": {}})
        return data
    except FileNotFoundError:
        init_cache()
        return {"channels": {}}
    except:
        print("Error reading cache")
        exit()

def save(data):
    try:
        f = open("cache.toml", "w", encoding="utf-8")
        f.write(toml.dumps(data))
        f.close()
    except:
        print("Error saving cache")

def init_cache():
    f = open("cache.toml", "w", encoding="utf-8")
    f.write(toml.dumps({"channels": {}}))
    f.close()

def convert_channel_info(data): 
    return {'url': data['url'], 'title': data['title'], 'subscribers': data['subscribers']['simpleText'], 'views': data['views']}