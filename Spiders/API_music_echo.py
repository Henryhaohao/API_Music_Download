# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/13--23:37
__author__ = 'Henry'

'''
echo回声-http://www.app-echo.com/
'''

import requests


def get_music_echo(url):
    id = url.rsplit('/',1)[1]
    url = 'http://www.app-echo.com/api/sound/info?id={}'.format(id)
    html = requests.get(url).json()
    mp3_url = html['info']['source']
    return mp3_url


# get_music_echo('http://www.app-echo.com/#/sound/1618712')
