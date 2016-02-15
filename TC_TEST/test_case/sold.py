#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"

import unittest
from selenium import webdriver
from time import sleep


class Sold(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://test2.sold.tuanche.com'

    def test_login(self):
        u"""后台登录"""
        print 'Began The test_case test_login'
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)
        username = self.driver.find_element_by_id('empLogin')
        username.clear()
        username.send_keys('qing.gao')
        password = self.driver.find_element_by_id('empPwd')
        password.clear()
        password.send_keys(123456)
        self.driver.find_element_by_class_name('btn').click()
        sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_id('topFrame'))
        self.driver.find_element_by_id('user_info')
        aa = self.driver.find_element_by_xpath(".//*[@id='user_info']/span/strong/a").text
        self.assertEqual(aa, u'高情')
        print 'End The test_case test_login'

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
