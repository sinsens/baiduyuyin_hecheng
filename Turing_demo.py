# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:13:41 2017

@author: Sinsen
@project: Turing Robot demo
    集成百度语音合成，需要下载同一目录下的baidu_yuyin.py
"""
import urllib,json
from baidu_yuyin import say

uid = '12345'
def chat(text='hello'):
    print 'me:',text
    url = 'http://www.tuling123.com/openapi/api'
    key = 'af2d922e18944529a9f2ce68d3449027'
    
    parmas = urllib.urlencode({
            'key':key,
            'info':text,
            'userid':uid
            })
    try:
        res = urllib.urlopen(url,parmas)
        res = json.loads(res.read())
        text = res['text'].encode('utf-8')
        print 'niko:',text
        say(text)
    except:
        print 'error'
    
chat('今天北京天气怎么样')
