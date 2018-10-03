# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/13--22:47
__author__ = 'Henry'

'''
咪咕音乐-http://music.migu.cn/v3
'''

import requests


def get_music_migu(url):
    id = url.rsplit('/',1)[1]
    url = 'http://music.migu.cn/v3/api/music/audioPlayer/songs?type=1&copyrightId={}'.format(id)
    id = requests.get(url).json()['items'][0]['songId']
    url_info = 'http://music.migu.cn/v2/async/audioplayer/playurl/{}'.format(id)
    html_info = requests.get(url_info).json()
    mp3_url = html_info['songAuditionUrl']
    return mp3_url


# get_music_migu('http://music.migu.cn/v3/music/song/6005660TDDT')
