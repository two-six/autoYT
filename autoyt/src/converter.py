#! /usr/bin/python

def convert_channel_info(data): 
    return {'url': data['url'], 'title': data['title'], 'subscribers': data['subscribers']['simpleText'], 'views': data['views']}

def convert_videos_output(data):
    result = ""
    for video in data['result']:
        result += "Title: " + video['title'] + "\nChannel: " + video['channel']['name'] + "\nViews: " + video['viewCount']['short'] + "\nLink: " + video['link'] + "\n-------------------------------------------\n\n"
    return result