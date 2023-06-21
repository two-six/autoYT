#! /usr/bin/python

import youtubesearchpython as ysp

def find_channel_id(name):
    if is_id(name):
        return name
    videosSearch = ysp.VideosSearch(name, 20)
    channel_id_dict = {}
    for i in videosSearch.result()['result']:
        channel_id = i['channel']['id']
        if channel_id in channel_id_dict:
            channel_id_dict[channel_id] += 1
        else:
            channel_id_dict[channel_id] = 1
    return max(channel_id_dict, key=channel_id_dict.get)

def get_channel_info(id):
    try:
        channel_info = ysp.Channel.get(id)
        return channel_info
    except:
        print("Couldn't get channel information: ", id)
        return {}

def find_channel_videos(channel_id: str, limit: int = 10):
    try:
        playlist = ysp.Playlist(ysp.playlist_from_channel_id(channel_id))
        while playlist.hasMoreVideos and (len(playlist.videos) < limit or limit == 0):
            playlist.getNextVideos()
        if limit == 0:
            return list(map(lambda x: ysp.Video.get(x['link'].split('&')[0], get_upload_date=True), playlist.videos))
        return list(map(lambda x: ysp.Video.get(x['link'].split('&')[0], get_upload_date=True), playlist.videos[0:limit]))
    except:
        print("Couldn't find channel videos: " + channel_id)
        return {}

def is_id(name):
    try:
        ysp.Playlist(ysp.playlist_from_channel_id(name))
        return True
    except:
        return False

def find_videos(name: str, limit: int = 10):
    return list(map(lambda x: ysp.Video.get(x['link'], get_upload_date=True), ysp.VideosSearch(name, limit).result()['result']))