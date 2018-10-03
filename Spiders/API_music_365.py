# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--12:24
__author__ = 'Henry'

'''
365音乐网-http://www.yue365.com/
'''


# mp3地址js生成代码:
# var surl = "http://96.ierge.cn/" ;
# nurl = parseInt(MusicId/30000) + "/" + parseInt(MusicId/2000) + "/" + MusicId +".mp3";


def get_music_365(url):
    id = url.rsplit('/', 1)[1].split('.')[0]
    url = 'http://96.ierge.cn/' + str(int(int(id) / 30000)) + '/' + str(int(int(id) / 2000)) + '/' + id + '.mp3'
    return url


# get_music_365('http://www.yue365.com/play/36254/414301.shtml')
