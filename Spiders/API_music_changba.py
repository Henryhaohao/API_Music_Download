# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--12:57
__author__ = 'Henry'


'''
唱吧-https://changba.com/
'''

import requests, re

def get_music_changba(url):
    html = requests.get(url).text
    mp3_url = re.search(r'var a="(.*?)"',html).group(1)
    return mp3_url


# get_music_changba('https://changba.com/s/i1x0XtdvFpn03qY2PVSedQ')