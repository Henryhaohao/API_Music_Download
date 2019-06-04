# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/2--14:01
__author__ = 'Henry'

'''
QQ音乐-https://y.qq.com/
'''

import requests, re
song_url='https://v1.itooi.cn/tencent/url?id={}&quality=128'

def get_music_qq(url,mid):
    if(mid=='0'):
        obj = re.search(r'(?<=songid=)\d+', url, re.I)  #预见匹配
        surl = 'https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songid={}&tpl=yqq_song_detail&format=jsonp&callback=getOneSo' \
           'ngInfoCallback'.format(obj.group(0))
        html = requests.get(surl)
        obj = re.findall(r'(mid.*?,)', html.text, re.I)
        mid = obj[3].rsplit('"', 2)[1]
        url = song_url.format(mid)
        return url
    else:
        url = song_url.format(mid)
        return url


# get_music_qq('https://y.qq.com/n/yqq/song/001s47AV2pyfEy.html')
