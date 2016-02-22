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
        self.Interface = 'basedata/hotstyle'
        self.params['cityId'] = 10
        self.params['offset'] = 0
        self.params['count'] = 5
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_top_brand(self):
        u"""获取每个城市下的热门品牌"""
        self.Interface = 'basedata/topBrand'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_get_same_price_style(self):
        u"""获取看了又看车型"""
        self.Interface = 'basedata/getSamePriceStyle'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        self.params['brandId'] = 1
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        self.assertEqual(result.get('code'), 10000)

    def test_model_map(self):
        u"""获取随时购选择车型"""
        self.Interface = 'basedata/modelmap'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_car_style_info(self):
        u"""根据车型id获取车款、车型、购车须知信息（随时购）"""
        self.Interface = 'basedata/ssgCarstyleInfo'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_car_style_model(self):
        u"""条件选车中根据车型id和车款ids获取车款、车型、购车须知信息（随时购）"""
        self.Interface = 'basedata/attrCarstyleModel'
        self.params['cityId'] = 10
        self.params['styleId'] = 6
        self.params['carModelIds'] = '14699'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        # print result
        self.assertEqual(result.get('code'), 10000)

    def test_style_map(self):
        u"""获取当前城市的热门车型"""
        self.Interface = 'basedata/stylemap'
        self.params['cityId'] = 10
        self.params['brandId'] = 1
        self.params['isBuy'] = 0
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_group_buy_info(self):
        u"""获取周末团详情信息"""
        self.Interface = 'groupbuy/info'
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
        self.Interface = 'basedata/modelyear'
        self.params['styleId'] = '284'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_check_sub_script(self):
        u"""获取车型是否已订阅"""
        self.Interface = 'basedata/subscription/checkSubscription'
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

    def test_buy_way(self):
        u"""获取购车方式统一接口"""
        self.Interface = 'basedata/buyway'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_brand_map(self):
        u"""获取品牌列表接口"""
        self.Interface = 'basedata/brandmap'
        self.params['cityId'] = 10
        self.params['isBuy'] = 0
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_tc_activity(self):
        u"""获取团车会接口"""
        self.Interface = 'basedata/tcactivity'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_get_all_city_open_status(self):
        u"""获取开通站点城市接口"""
        self.Interface = 'basedata/city/getAllCityInOpenStatus'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        # self.assertEqual(result.get('code'), 10000)

    def test_model_select(self):
        u"""获取随时购车型接口"""
        self.Interface = 'basedata/modelSelect'
        self.params['modelId'] = 122
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_cancel_Sub_script(self):
        u"""取消订阅提醒开团接口"""
        self.Interface = 'basedata/subscription/cancelSubscription'
        self.params['styleId'] = 110
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

    def test_subscribe(self):
        u"""订阅提醒开团接口"""
        self.Interface = 'basedata/subscription/subscribe'
        self.params['styleId'] = 110
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_get_All_City(self):
        u"""获取所有城市列表接口"""
        self.Interface = 'basedata/city/getAllCity'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_getTCCity(self):
        u"""获取提车城市接口"""
        self.Interface = 'basedata/city/getTCCity'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_getHotCity(self):
        u"""获取热门城市接口"""
        self.Interface = 'basedata/city/getHotCity'
        self.params['top'] = 1
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_getSysConfig(self):
        u"""获取系统配置选项接口"""
        self.Interface = 'basedata/getSysConfig'
        self.params['key'] = 'ssg_order_time,ssg_order_style'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_zmt_ssg_select(self):
        u"""获取周末团完善信息接口"""
        self.Interface = 'basedata/zmt/ssg/select'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_order_num(self):
        u"""获取询价人数接口"""
        self.Interface = 'basedata/ordernum'
        self.params['styleId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_new_style(self):
        u"""获取最新车型接口"""
        self.Interface = 'basedata/newstyle'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_zmt_select(self):
        u"""获取周末团完善信息页面选择项接口"""
        self.Interface = 'basedata/zmt/select'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_getHotAndAllCitys(self):
        u"""获取选择上牌城市和提现时选择开户城市接口"""
        self.Interface = 'basedata/city/getHotAndAllCitys'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_city_Mode(self):
        u"""获取城市模式接口1，周末团 2，随时购 3，混合模式 4，电商"""
        self.Interface = 'basedata/cityMode'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_queryCityByLatitude(self):
        u"""经纬度获取城市接口"""
        self.Interface = 'basedata/city/queryCityByLatitude'
        self.params['latitude'] = '39.9'
        self.params['longitude'] = '116.3'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_index(self):
        u"""获取首页新车买卖，二手车拍卖，团车养车接口"""
        self.Interface = 'basedata/index'
        self.params['cityId'] = 10
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def test_message(self):
        u"""获取放假公告接口"""
        self.Interface = 'basedata/message'
        r = requests.get(self.base_url+self.Interface, params=self.params, headers=self.headers)
        result = r.json()
        print result
        self.assertEqual(result.get('code'), 10000)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
