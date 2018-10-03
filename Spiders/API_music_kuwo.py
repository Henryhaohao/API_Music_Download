# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/3--11:25
__author__ = 'Henry'

'''
酷我音乐-http://www.kuwo.cn/
'''

import requests


def get_music_kuwo(url):
    id = url.rsplit('/', 1)[1]
    url = 'http://antiserver.kuwo.cn/anti.s?format=acc|mp3&rid=MUSIC_{}&type=convert_url&response=res'.format(id)
    html = requests.get(url, allow_redirects=False)  # 禁止重定向
    mp3_url = html.headers['Location']  # 获取302跳转到的网址
    return mp3_url


# get_music_kuwo('http://www.kuwo.cn/yinyue/53959930')
