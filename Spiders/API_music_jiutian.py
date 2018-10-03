# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--12:05
__author__ = 'Henry'

'''
九天音乐网-http://www.9sky.com/
'''

import requests, re


def get_music_jiutian(url):
    html = requests.get(url).text
    mp3 = re.search(r"songUrl':'(.*?)'", html).group(1)
    return mp3


# get_music_jiutian('http://www.9sky.com/music?ids=3662')
