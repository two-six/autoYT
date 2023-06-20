#! /usr/bin/python

def convert_channel_info(data): 
    return {'url': data['url'], 'title': data['title'], 'subscribers': data['subscribers']['simpleText'], 'views': data['views']}

def convert_videos_output(data):
    result = ""
    for video in data:
        result += "Title: " + video['title'] + "\nChannel: " + video['channel']['name'] + "\nUpload Date: " + video['uploadDate'] + "\nLink: " + video['link'] + "\n-------------------------------------------\n\n"
    return result

def convert_channel_videos_output(data: list, channel_id: str, limit: int):
    result = "Channel Name: " + data[0]['channel']['name'] + "\nChannel Link: https://youtube.com/channel/" + channel_id + "\n-------------------------------------------\n\n"
    for i in range(limit):
        result += "Title: " + data[i]['title'] + "\nLink: " + data[i]['link'].split('&')[0] + "\nUpload Date: " + data[i]['uploadDate'] + "\n-------------------------------------------\n\n"
    return result

def convert_channel_list(data: dict):
    result = ""
    for channel in data['channels']:
        result += "Name: " + data['channels'][channel]['title'] + "\nLink: " + data['channels'][channel]['url'] + "\nChannel ID: " + channel + "\n-------------------------------------------\n\n" 
    return result