#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"

import unittest
from selenium import webdriver
from time import sleep
from test_case.tc_db import MySQLHelper


class TestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_keyword_search(self):
        u"""团车报名"""
        self.driver.maximize_window()
        self.driver.get('http://bj.tuanche.com/')
        brand = self.driver.find_element_by_id('factoryVal')
        brand.find_element_by_xpath("//option[@value='23']").click()
        carstyle = self.driver.find_element_by_name('carstyle')
        carstyle.find_element_by_xpath("//option[@value='154']").click()
        self.driver.find_element_by_name('user').send_keys(u'乾隆')
        self.driver.find_element_by_name('phone').send_keys('13388888888')
        self.driver.find_element_by_class_name('inputsubmit-sign').click()
        sleep(2)
        db = MySQLHelper(host='172.16.12.44', user='testread', password='test123^&*', db='che100')
        sql = "SELECT phone FROM tc_apply WHERE name = '乾隆';"
        result = db.query_all(sql)
        phone = result[0]['phone']
        self.assertEqual(phone, '13388888888')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
