各大音乐/FM平台歌曲下载API集合 ![enter image description here](Pic/logo.png)
===========================
![](https://img.shields.io/badge/Python-3.6.3-green.svg) ![](https://img.shields.io/badge/requests-2.18.4-green.svg) ![](https://img.shields.io/badge/PyExecJS-1.5.1-green.svg) 

|Author|:sunglasses:Henryhaohao:sunglasses:|
|---|---
|Email|:hearts:1073064953@qq.com:hearts:

    
****
## :dolphin:声明
### 软件均仅用于学习交流，请勿用于任何商业用途！感谢大家！
## :dolphin:介绍
### 该项目为常见的各大音乐平台/FM平台歌曲/音频下载 (目前:包括14个音乐网站,3个FM网站)  
### 如果大家有别的想要添加的音乐平台，欢迎大家来Fork and Pull！  

|音乐/FM平台|歌曲/FM链接示例|
|----|-----|
|[网易云音乐](https://music.163.com/)|https://music.163.com/#/song?id=418603177|
|[虾米音乐](http://www.xiami.com/)|https://www.xiami.com/song/1776212033|
|[QQ音乐](https://y.qq.com/)|https://y.qq.com/n/yqq/song/001s47AV2pyfEy.html|
|[千千(百度)音乐](http://www.taihe.com/)|http://www.taihe.com/song/601427388|
|[酷狗音乐](http://www.kugou.com/)|http://www.kugou.com/song/#hash=DE41BABE5CFD9FA34FE5A0F4C40997BD&album_id=1833108|
|[酷我音乐](http://www.kuwo.cn/)|http://www.kuwo.cn/yinyue/53959930|
|[echo回声](http://www.app-echo.com/)|http://www.app-echo.com/#/sound/1618712|
|[咪咕音乐](http://music.migu.cn/v3/)|http://music.migu.cn/v3/music/song/6005660TDDT|
|[九天音乐](http://www.9sky.com/)|http://www.9sky.com/music?ids=3662|
|[365音乐](http://www.yue365.com/)|http://www.yue365.com/play/36254/414301.shtml|
|[一听音乐](https://www.1ting.com/)|https://www.1ting.com/player/65/player_1191234.html|
|[5sing音乐](http://5sing.kugou.com/)|http://5sing.kugou.com/yc/3712138.html|
|[MVbox音乐](http://www.mvbox.cn/)|http://space.mvbox.cn/2612527/fc/1959795.html|
|[唱吧](https://changba.com/)|https://changba.com/s/i1x0XtdvFpn03qY2PVSedQ|
|[喜马拉雅FM](https://www.ximalaya.com/)|https://www.ximalaya.com/youshengshu/16679724/102504549|
|[豆瓣FM](https://douban.fm/)|https://douban.fm/song/1978516gd7f0|
|[荔枝FM](http://www.lizhi.fm/)|http://www.lizhi.fm/14275/2695272442531976710|
- 项目介绍:通过传入歌曲/FM音频的播放地址返回其对应的歌曲/音频下载地址
- 爬虫文件:Spiders目录下的各个python文件
- 运行方式:运行Spiders目录下main.py文件即可
## :dolphin:运行环境
Version: Python3
## :dolphin:安装依赖库
```
pip3 install -r requirements.txt
```
> 注意:此项目需安装pyexecjs库，因为网易云音乐(API_music_cloud163.py)的爬取需执行JS文件进行解密
## :dolphin:运行截图
> - **传入歌曲/FM链接获取下载地址**<br><br>
![enter image description here](Pic/run.gif)
## :dolphin:**总结**
> **最后，如果你觉得这个项目不错或者对你有帮助，给个Star呗，也算是对我学习路上的一种鼓励！<br>
 哈哈哈，感谢大家！笔芯~**:cupid::cupid:




