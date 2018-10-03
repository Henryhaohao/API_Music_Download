# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--11:40
__author__ = 'Henry'

'''
一听音乐-https://www.1ting.com
'''

import requests, re


def get_music_1ting(url):
    '''传入音乐网址(eg:https://www.1ting.com/player/d3/player_1024574.html)'''
    html = requests.get(url).text
    result = re.search(r'create\(\[(.*?)\]\)', html).group(1)
    mp3 = eval(result)[7].split('.')[0].replace('\\', '')
    mp3_url = 'https://www.1ting.com/api/audio?' + mp3 + '.mp3'
    headers = {
        'referer': url,  # 必须加上referer
        'user-agent': 'Mozilla/5.0 (WindowsNT6.1;WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    mp3 = requests.get(mp3_url, headers=headers).url  # 302跳转
    return mp3


# get_music_1ting('https://www.1ting.com/player/65/player_1191234.html')
