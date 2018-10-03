# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--13:09
__author__ = 'Henry'

'''
喜马拉雅FM-https://www.ximalaya.com/
'''

import requests


def get_music_ximalayafm(url):
    id = url.rsplit('/', 1)[1]
    url = 'https://www.ximalaya.com/revision/play/tracks?trackIds={}'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': url
        # 必须加上Referer才行
    }
    html = requests.get(url, headers=headers).json()
    mp3_url = html['data']['tracksForAudioPlay'][0]['src']
    return mp3_url


# get_music_ximalayafm('https://www.ximalaya.com/youshengshu/16679724/102504549')
# get_music_ximalayafm('https://www.ximalaya.com/toutiao/4519297/126690880')
