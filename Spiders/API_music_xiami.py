# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/27--8:38
__author__ = 'Henry'

'''
虾米音乐网-http://www.xiami.com/
加密方式:下载地址location进行了凯撒方阵的列数加密
'''

import requests, urllib.parse


def get_music_xiami(url):
    id = url.rsplit('/', 1)[1]
    # 获取location
    url = 'http://www.xiami.com/song/playlist/id/{}/object_name/default/object_id/0/cat/json'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.xiami.com/play?ids=/song/playlist/id/{}/object_name/default/object_id/0'.format(id),
        # 必须加上Referer才行
    }
    html = requests.get(url, headers=headers).json()
    location = html['data']['trackList'][0]['location']
    # eg: 8h28n22%8743ph1%51%428tF.e%%537793_55Ec523%t%xt22E4399%k2E-1E315p2i%FF864_13e2%%ae77E%Fa252%%31_Fy855ffae53mmF5%52%5la%9EE%5e1A1i775EF56.u37--54bf%2.11E71E5mtD2%6E344
    length = len(location) - 1
    row_num = int(location[0])
    column_num = length // row_num + 1
    mod = length % row_num
    url = location[1:]
    # 行排布
    row_list = []
    for i in range(row_num):
        if i < mod:
            # 上面多的几行
            row = url[column_num * i:column_num * (i + 1)]
            row_list.append(row)
        else:
            # 下面少的几行
            row = url[(length // row_num) * i + mod:(length // row_num) * (i + 1) + mod]
            row_list.append(row)
    # 列排布
    column_list = []
    for i in range(column_num):
        if i <= column_num - 2:
            for j in range(row_num):
                column = row_list[j][i]
                column_list.append(column)
        else:
            for j in range(mod):
                column = row_list[j][i]
                column_list.append(column)
    # 字符串拼接起来
    column_str = ''.join(column_list)
    # url解码
    url_decode = urllib.parse.unquote(column_str)
    # 将^替换成0,写出真实地址
    url_mp3 = 'https:' + url_decode.replace('^', '0')
    return url_mp3


# get_music_xiami('https://www.xiami.com/song/1776212033')
# get_music_xiami('https://www.xiami.com/song/mSGUAb673ba')
