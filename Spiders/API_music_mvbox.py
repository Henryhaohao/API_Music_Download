# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--12:48
__author__ = 'Henry'

'''
MVBox-http://www.mvbox.cn/
'''

import requests, re


def get_music_mvbox(url):
    html = requests.get(url).text
    mp3_url = re.search(r"fileUrl = '(.*?)'", html).group(1)
    return mp3_url


# get_music_mvbox('http://space.mvbox.cn/2612527/fc/1959795.html')
