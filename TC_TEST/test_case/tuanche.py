#!/usr/bin/env python
# encoding: utf-8
__author__ = "CaoHP"

import unittest
from selenium import webdriver
from time import sleep
from tc_db import MySQLHelper
from ImgDiscren import ImgDownload


class TuAnChe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        u"""团车登录"""
        print 'Began The test_case test_login'
        self.driver.get('http://uc.tuanche.com/login/toLogin?pg=brandIndex&pl=denglut')
        self.driver.maximize_window()
        self.driver.find_element_by_id('phone').send_keys('15901564660')
        self.driver.find_element_by_id('password').send_keys('60346533')
        self.driver.find_element_by_id('loginBtn').click()
        sleep(1)
        username = self.driver.find_element_by_class_name('leftNickName').text
        self.assertEqual(username, u'fdj28661768')
        print 'End The test_case test_login'

    def test_sign_up(self):
        u"""团车报名"""
        print 'Began The test_case test_sign_up'
        down_load_path = 'D://sold-console//ImgDiscren//1.png'
        self.driver.get('http://bj.tuanche.com/b2/tuan/?pg=brandIndex&pl=brandImg')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(".//*[@id='mainDetailStyle']/li[3]/span").click()
        self.driver.find_element_by_name('userName').send_keys(u'张三')
        self.driver.find_element_by_name('userTel').send_keys(13391897268)
        self.driver.find_element_by_xpath(".//*[@id='buyMethod']/li[1]").click()
        # img_url = self.driver.find_element_by_id('verifycodeimg').get_attribute('src')
        # img_text = ImgDownload.download_img(img_url, down_load_path)
        # print img_text
        # while img_text == '':
        #     img_text = ImgDownload.download_img(img_url, down_load_path)
        #     print img_text, 'in while loop '
        # self.driver.find_element_by_id('verifytext').send_keys(img_text)
        # self.driver.find_element_by_class_name('mainDetailF-sub').click()
        print 'End The test_case test_sign_up'

    def test_group_join(self):
        u"""团车报名"""
        print 'Began The test_case test_group_join'
        self.driver.maximize_window()
        self.driver.get('http://bj.tuanche.com/')
        brand = self.driver.find_element_by_id('factoryVal')
        brand.find_element_by_xpath("//option[@value='23']").click()
        carstyle = self.driver.find_element_by_name('carstyle')
        carstyle.find_element_by_xpath("//option[@value='154']").click()
        self.driver.find_element_by_name('user').send_keys(u'张三')
        self.driver.find_element_by_name('phone').send_keys('13322221234')
        self.driver.find_element_by_class_name('inputsubmit-sign').click()
        print 'End The test_case test_group_join'

    def test_keyword_search(self):
        u"""团车查询"""
        print 'Began The test_case test_keyword_search'
        self.driver.maximize_window()
        self.driver.get('http://bj.tuanche.com/')
        self.driver.find_element_by_id('bdcs-search-form-input').send_keys(u'速腾')
        self.driver.find_element_by_id('bdcs-search-form-submit').click()
        sleep(1)
        print self.driver.title
        print self.driver.current_url
        print self.driver.window_handles
        now_handle = self.driver.current_window_handle
        all_handle = self.driver.window_handles
        for i in all_handle:
            if i != now_handle:
                self.driver.switch_to_window(i)
                sleep(3)
                keyword = self.driver.find_element_by_id('kw').get_attribute('value')
                print keyword
        self.assertEqual(keyword, u'速腾')
        print 'End The test_case test_keyword_search'

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
