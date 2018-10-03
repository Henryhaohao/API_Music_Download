# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/27--8:27
__author__ = 'Henry'

'''
5sing原创音乐网-http://5sing.kugou.com
'''

import requests, json


def get_music_5sing(url):
    id = url.rsplit('/', 1)[1].split('.')[0]
    url = 'http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype=yc&from=web'.format(id)
    html = requests.get(url).text[1:-1]
    result = json.loads(html)
    mp3 = result['data']['hqurl']
    return mp3


# get_music_5sing('http://5sing.kugou.com/yc/3712138.html')
