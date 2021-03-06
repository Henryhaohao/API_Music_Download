# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--17:06
__author__ = 'Henry'

'''
主运行程序
'''

from Spiders.API_music_cloud163 import get_music_cloud163
from Spiders.API_music_1ting import get_music_1ting
from Spiders.API_music_5sing import get_music_5sing
from Spiders.API_music_365 import get_music_365
from Spiders.API_music_changba import get_music_changba
from Spiders.API_music_doubanFM import get_music_doubanfm
from Spiders.API_music_echo import get_music_echo
from Spiders.API_music_jiutian import get_music_jiutian
from Spiders.API_music_kugou import get_music_kugou
from Spiders.API_music_kuwo import get_music_kuwo
from Spiders.API_music_lizhiFM import get_music_lizhifm
from Spiders.API_music_migu import get_music_migu
from Spiders.API_music_mvbox import get_music_mvbox
from Spiders.API_music_qianqian_baidu import get_music_qianqian
from Spiders.API_music_qq import get_music_qq
from Spiders.API_music_xiami import get_music_xiami
from Spiders.API_music_ximalayaFM import get_music_ximalayafm


def main(url):
    if 'music.163' in url:
        print('此链接为网易云音乐')
        print('此音乐下载地址为:' + get_music_cloud163(url))
        exit()
    if 'qq.com' in url:
        print('此链接为QQ音乐')
        print('此音乐下载地址为:' + get_music_qq(url))
        exit()
    if 'taihe.com' in url:
        print('此链接为千千(百度)音乐')
        print('此音乐下载地址为:' + get_music_qianqian(url))
        exit()
    if 'xiami.com' in url:
        print('此链接为虾米音乐')
        print('此音乐下载地址为:' + get_music_xiami(url))
        exit()
    if 'kugou.com/song' in url:
        print('此链接为酷狗音乐')
        print('此音乐下载地址为:' + get_music_kugou(url))
        exit()
    if 'kuwo.cn' in url:
        print('此链接为酷我音乐')
        print('此音乐下载地址为:' + get_music_kuwo(url))
        exit()
    if '1ting.com' in url:
        print('此链接为一听音乐')
        print('此音乐下载地址为:' + get_music_1ting(url))
        exit()
    if '5sing.kugou' in url:
        print('此链接为5sing音乐')
        print('此音乐下载地址为:' + get_music_5sing(url))
        exit()
    if 'yue365.com' in url:
        print('此链接为365音乐')
        print('此音乐下载地址为:' + get_music_365(url))
        exit()
    if 'changba.com' in url:
        print('此链接为唱吧音乐')
        print('此音乐下载地址为:' + get_music_changba(url))
        exit()
    if 'app-echo' in url:
        print('此链接为echo回声')
        print('此音乐下载地址为:' + get_music_echo(url))
        exit()
    if '9sky.com' in url:
        print('此链接为九天音乐')
        print('此音乐下载地址为:' + get_music_jiutian(url))
        exit()
    if 'migu.cn' in url:
        print('此链接为咪咕音乐')
        print('此音乐下载地址为:' + get_music_migu(url))
        exit()
    if 'mvbox.cn' in url:
        print('此链接为MVbox音乐')
        print('此音乐下载地址为:' + get_music_mvbox(url))
        exit()
    if 'ximalaya.com' in url:
        print('此链接为喜马拉雅FM')
        print('此音乐下载地址为:' + get_music_ximalayafm(url))
        exit()
    if 'douban.fm' in url:
        print('此链接为豆瓣FM')
        print('此音乐下载地址为:' + get_music_doubanfm(url))
        exit()
    if 'lizhi.fm' in url:
        print('此链接为荔枝FM')
        print('此音乐下载地址为:' + get_music_lizhifm(url))
        exit()


if __name__ == '__main__':
    print('*' * 30 + '欢迎来到小豪音乐下载助手' + '*' * 30)
    url = input('[请输入歌曲/FM的网址链接]:')
    main(url)
