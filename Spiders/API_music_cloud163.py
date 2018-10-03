# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/7/21--20:10
__author__ = 'Henry'

'''
网易云音乐-https://music.163.com/
'''

import requests, execjs, ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_music_cloud163(url):
    with open('core.js') as f:
        jsdata = f.read()

    id = url.split('=')[1]
    form = {'ids': '[' + id + ']', 'br': 320000, 'csrf_token': ''}  # form要是字符串才行
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'  # 系数,模数
    nonce = '0CoJUm6Qyw8W8jud'  # Nonce是或Number once的缩写，在密码学中Nonce是一个只被使用一次的任意或非重复的随机数值
    pub_key = '010001'  # 公钥

    p = execjs.compile(jsdata).call('d', str(form), pub_key, modulus, nonce)
    # print(p)

    # 带入加密参数获取歌曲url
    form1 = {
        'params': p['encText'],
        'encSecKey': p['encSecKey']
    }
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    headers = {
        'Cookie': '_ntes_nnid=08b82ecba08a5f96823626e058fd0fdd,1530151335819; _ntes_nuid=08b82ecba08a5f96823626e058fd0fdd; NTES_SESS=wadXQXKGI_z9FIymvd4b.p2PmqSlgGN0BrHNUflOuQgzj0mKjiCG5_dhDsLYIJUjNeoDY.PU03pVUByrJUdOP3OlnFEr93fzSUYcCOg4KJZFy7biVf6Ct5jonvx_j.rv8Nj7OJ5PeZTHu7BBAqsw8AP8tGXBBPVemwxM4hkQclD_TCCY5vPHgtRC6BlOwVagZHltyqq.JHoAAVQsmQbmzRKYl; S_INFO=1532306469|0|3&100##|miaojin5866; P_INFO=miaojin5866@163.com|1532306469|0|cbg|10&35|anh&1532059670&mail163#anh&340100#10#0#0|139566&0|mail163|miaojin5866@163.com; __f_=1532754134690; Province=0550; City=0556; NTES_CMT_USER_INFO=77327706%7Cmiaojin5866%7C%7Cfalse%7CbWlhb2ppbjU4NjZAMTYzLmNvbQ%3D%3D; __gads=ID=bab5bda5a6797d2d:T=1533023238:S=ALNI_MZCXcdl_gJSbx7vhaoFyQh_imjGpQ; UM_distinctid=164ef4e1ec318f-096cec7b9ff534-6b1b1279-1fa400-164ef4e1ec7429; vjuids=-8d23c4dcb.164ef4e2248.0.95f3c97b1b87f; _antanalysis_s_id=1533023232898; __utma=187553192.1213453033.1533035970.1533035970.1533035970.1; __utmc=187553192; __utmz=187553192.1533035970.1.1.utmcsr=3g.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/touch/; __oc_uuid=978f06f0-94b3-11e8-b70a-ad3084746ce9; vjlast=1533023233.1533200899.13; ne_analysis_trace_id=1533200899153; vinfo_n_f_l_n3=6c734e6d05fc0062.1.0.1533023232739.0.1533200901068; s_n_f_l_n3=6c734e6d05fc00621533023232740; hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22cp-400000000387008%22%2C%22utm_medium%22%3A%20%22share%22%2C%22utm_campaign%22%3A%20%22commission%22%2C%22utm_content%22%3A%20%22%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; NNSSPID=5d500a74cc3343b48b93327028639bbf; JSESSIONID-WYYY=ge4vq7yEnZdK16kDaHJPumN3j2gZi3mvxwDsm0YSbdCnYejWFDmgxENJR07oZSSFMzJxlEjEjlYDfbeXruiFwMvaqOg6b8wt6b9AK5VmJJ5mkRrfg5al%2FiTDilzti8ZNZide7wkmydzHIDFHmsBakAGnaia9P5QYJTor5r15ujl%2FgWYl%3A1533959080848; _iuqxldmzr_=32; WM_NI=FMJj2uhcUuQITNcmBorT2XLkyWEe93jpuKNKUubsBzB%2FEshbOn0D3%2FzamkLKzlLX8H6q3s9NwBVuJI58En4tkUNYII9lzgRzIwLbGyJdMMYwr5EbC1VLQm4fwF%2FMtM6HV0s%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabb354a7a9858fcf7aace7fed4f97cbaf09eabcf7289a89babc45cf49c8bd9ec2af0fea7c3b92a8693868bb17facbd9b96d4439892ad8ec165b28cfeb9cf61bb898b86bc39aab0bbaccd4197abae94c17282f18b94eb6a8db200a5b225babfa38ccf41bab484b9bb44f6affd94bc46b59e9a96c943f7e88b8fb780a98b82bacc43fbb4b688d1728ba98483c6738abc83aedc7db2eb8b83c23b96949f8eb76eb59ae1aef747f6989ad1f237e2a3; WM_TID=xtAvr8z9XsqSTDWh%2Fx1DpYgPNoE91pen; cm_newmsg=user%3Dm****%40163.com%26new%3D-1%26total%3D-1; playerid=84708328; MUSIC_U=b097032241a737d61ae4b41d321c00eed81daaf299d487ce8b6dd89e7e556d45bf7fe7b782f803ca020a17dfe08c36db31b299d667364ed3; __remember_me=true; __csrf=dd3a12742e038ee966525a5b1a725a5a; __utma=94650624.1131882950.1532162813.1533792036.1533955492.11; __utmb=94650624.38.10.1533955492; __utmc=94650624; __utmz=94650624.1533955492.11.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    html = requests.post(url=url, data=form1, headers=headers).json()
    mp3_url = html['data'][0]['url']
    return mp3_url


# get_music_cloud163('https://music.163.com/#/song?id=1308818967')

# 注意:
# 电台节目:https://music.163.com/djradio?id=526820640 #电台的id
# 源码中请求出所有歌曲id列表再依次爬取

