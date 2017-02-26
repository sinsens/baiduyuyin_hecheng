# -*- coding: utf-8 -*-
"""
Spyder Editor
百度语音合成
没有使用提供的API而是使用测试页面提供的参数，不知道以后会不会失效,在Windows下测试成功，需要mp3play包
页面地址：http://yuyin.baidu.com/#try
sinsen 2017/2/26
"""
import urllib
import mp3play
import time
import os

def say(text):
    url = 'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_demo&cod=2&lan=zh&ctp=1&pdt=1&spd=5&per=4&vol=5&pit=5'
    url = url.format(text)
    
    """ 先将音频文件下载到本地后再播放 """
    filename = str(time.time())+'.mp3'
    urllib.urlretrieve(url,filename)
    mp3 = mp3play.load(filename)
    mp3.play()
        
    """ 播放结束前要对主线程休眠，否则会直接退出执行脚本 """
    st=(mp3.seconds()+0.25)
    time.sleep(st)
    
    mp3.pause()
    """ 播放结束后删除临时文件 """
    if mp3.ispaused():
        try:
            os.remove(filename)
        except:
            print 'Error'
    
#say('你好，我是小娜，你喜欢我吗')
