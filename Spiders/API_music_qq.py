# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/2--14:01
__author__ = 'Henry'

'''
QQ音乐-https://y.qq.com/
'''

import requests, re
song_url='https://v1.itooi.cn/tencent/url?id={}&quality=128'

def get_music_qq(url):
    id = url.rsplit('/', 1)[1].split('.')[0]
    # html = requests.get(url).text
    # media_mid = re.search(r'strMediaMid":"(.*?)",', html).group(1)
    # url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?cid=205361747&uin=1073064953&songmid=%s&filename=C400%s.m4a&guid=8874047000' % (
    #     id, media_mid)
    # html = requests.get(url).json()
    # filename = html['data']['items'][0]['filename']
    # vkey = html['data']['items'][0]['vkey']
    # print(html)
    # print(filename)
    # print(vkey)
    if id == '':
        print('抱歉,此歌曲为付费版本哦~')
        exit()
    else:
        url = song_url.format(id)
        return url


# get_music_qq('https://y.qq.com/n/yqq/song/001s47AV2pyfEy.html')
