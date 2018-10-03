# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--12:48
__author__ = 'Henry'

'''
豆瓣FM-https://douban.fm/
'''

import requests


def get_music_doubanfm(url):
    id = url.rsplit('/', 1)[1]
    url = 'https://douban.fm/j/v2/song/{}/'.format(id)
    html = requests.get(url).json()
    mp3_url = html['url']
    return mp3_url


# get_music_doubanfm('https://douban.fm/song/1978516gd7f0')
