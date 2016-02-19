#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"

import unittest
import requests


class BaseData(unittest.TestCase):

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

    def test_top_brand(self):
        u"""获取每个城市下的热门品牌"""
        self.Interface = '/basedata/topBrand'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_get_same_price_style(self):
        u"""获取看了又看车型"""
        self.Interface = '/basedata/getSamePriceStyle'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        self.params['brandId'] = 1
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_model_map(self):
        u"""获取随时购选择车型"""
        self.Interface = '/basedata/modelmap'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_car_style_info(self):
        u"""根据车型id获取车款、车型、购车须知信息（随时购）"""
        self.Interface = '/basedata/ssgCarstyleInfo'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_car_style_model(self):
        u"""条件选车中根据车型id和车款ids获取车款、车型、购车须知信息（随时购）"""
        self.Interface = '/basedata/attrCarstyleModel'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        self.params['carModelIds'] = '14699'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_style_map(self):
        u"""获取当前城市的热门车型"""
        self.Interface = '/basedata/stylemap'
        self.params['cityId'] = 10
        self.params['brandId'] = 1
        self.params['isBuy'] = 0
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_group_buy_info(self):
        u"""获取周末团详情信息"""
        self.Interface = '/groupbuy/info'
        self.params['cityId'] = 10
        self.params['brandId'] = 1
        self.params['styleId'] = 1
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_group_buy_evaluate(self):
        u"""获取周末团评价列表"""
        self.Interface = 'groupbuy/evaluate'
        self.params['cityId'] = 10
        self.params['brandId'] = 1
        self.params['offset'] = 1
        self.params['count'] = 4
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_model_year(self):
        u"""获取车款年份列表"""
        self.Interface = '/basedata/modelyear'
        self.params['styleId'] = '284'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_check_sub_script(self):
        u"""获取车型是否已订阅"""
        self.Interface = '/basedata/subscription/checkSubscription'
        self.params['styleId'] = '12'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        if result.get('code') == 10000:
            print result.get('msg')
        elif result.get('code') == 2:
            print result.get('msg')
        else:
            print result.get('msg')
        # self.assertEqual(result.get('code'), 10000)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
