#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"
import urllib
import time
from ImgDiscern import get_verify


def download_img(url, path):
    urllib.urlretrieve(url, path)
    # time.sleep(5)
    text = get_verify('1.png')
    return text

if __name__ == '__main__':
    url = 'http://tuanche.com/service/verifycode?1452677247397'
    path = 'D://sold-console//ImgDiscren//1.png'
    download_img(url, path)
    text = get_verify('1.png')
    while text == '':
        print text + 'text is null!'
        download_img(url, path)
        text = get_verify('1.png')
        print text, 'is while'
        print type(text), 'is while'
    print text, 'is no'
    print type(text), 'is no'
