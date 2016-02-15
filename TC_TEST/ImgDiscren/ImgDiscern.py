# -*- coding: utf-8 -*-
"""采用PIL 和pytesser进行简单的验证码识别
程序包中已经包含了pytesser，但是需要自己安装PIL

使用样例
getverify1('v1.jpg') 返回值为识别出的字符

author：nwpulei@gmail.com
2013-1-1
"""
from PIL import Image
import sys, time
from pytesser import *
import urllib

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)


def get_verify(name):
    # 打开图片
    im = Image.open(name)
    # 转化到亮度
    imgry = im.convert('L')
    imgry.save('g' + name)
    # 二值化
    out = imgry.point(table, '1')
    out.save('b' + name)
    # 识别
    text = image_to_string(out)
    # 识别对吗
    text = text.strip()
    text = text.upper()
    return text


def download_img(url, path):
    urllib.urlretrieve(url, path)
    time.sleep(5)
    text = get_verify('1.png')
    return text

if __name__ == '__main__':
    url = 'http://tuanche.com/service/verifycode?1452677247397'
    down_load_path = 'D://sold-console//ImgDiscren//1.png'
    text = download_img(url, down_load_path)
    if text:
        print text, 'if'
    else:
        text = download_img(url, down_load_path)
        print text, 'else'

