# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/13--20:40
__author__ = 'Henry'

'''
 酷狗音乐-http://www.kugou.com/
'''

import requests, re


def get_music_kugou(url):
    html = requests.get(url).text
    reg = re.search('hash":"(.*?)".*?album_id":(.*?)}', html)
    album_id = reg.group(2)
    hash = reg.group(1)
    url_info = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}'.format(hash, album_id)
    html_info = requests.get(url_info).json()
    play_url = html_info['data']['play_url']
    return play_url


# get_music_kugou('http://www.kugou.com/song/qa79h9a.html')
