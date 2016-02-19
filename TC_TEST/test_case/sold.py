#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"

import unittest
import requests


class Sold(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://t.umapi.tuanche.com/'
        self.headers = {
            'traceinfo': "versionname=2.4.0;versioncode=20151201;"
                         "imei=865291025047373;sim=null;macaddress=0c:1d:af:df:1a:95;"
                         "buildversion=4.4.4;osversion=19;model=MI 4W;appname=GroupbuyCar;"
                         "source=22;network=;location=116.319659,39.897641;channelid=10001;"
                         "deviceid=865291025047373;seq=8652910250473730063;"
                         "num=0c:1d:af:df:1a:95-1438140600296",
            'des': "false"}

        self.params = {'token': '854bf097c58514233e5c781efc30184d7d8406271ed8ca49ba7307481784273bcac'
                                '1150d3c8e5919c74066ce612ec567_37f8d1bb56095b47ace61557b91a817a',
                       'time': '1453693074',
                       'sign': '40bbe5ba28ac6c41f575b0042df85575'}

    def test_get_city(self):
        u"""获取城市接口"""
        self.Interface = 'basedata/city/getCitys'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_hot_style(self):
        u"""获取热门城市列表"""
        self.Interface = '/basedata/hotstyle'
        self.params['cityId'] = 10
        self.params['offset'] = 0
        self.params['count'] = 5
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_1(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
