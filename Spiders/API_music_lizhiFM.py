# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--14:20
__author__ = 'Henry'

'''
荔枝FM-http://www.lizhi.fm/
'''

# _ud.mp3:超高清; _hd.mp3:高清; _sd.m4a:低清

import requests


def get_music_lizhifm(url):
    id = url.rsplit('/', 1)[1]
    url = 'http://www.lizhi.fm/media/url/{}'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    html = requests.get(url, headers=headers).json()
    mp3_url = html['data']['url']
    return mp3_url


# get_music_lizhifm('http://www.lizhi.fm/14275/2695272442531976710')
