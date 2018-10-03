# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/23--17:11
__author__ = 'Henry'

'''
千千音乐(原百度音乐)-http://www.taihe.com/
'''

import requests


def get_music_qianqian(url):
    id = url.rsplit('/', 1)[1]
    url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid={}&from=web'.format(id)
    html = requests.get(url).json()
    mp3_url = html['bitrate']['file_link']
    return mp3_url


# get_music_qianqian('http://www.taihe.com/song/601427388')
