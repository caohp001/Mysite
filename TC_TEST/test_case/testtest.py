#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"

import unittest
from selenium import webdriver
from time import sleep
from tc_db import MySQLHelper


class TestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_keyword_search(self):
        self.driver.get('http://bj.tuanche.com/b2/tuan/?pg=brandIndex&pl=brandImg')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(".//*[@id='mainDetailStyle']/li[3]/span").click()
        self.driver.find_element_by_name('userName').send_keys(u'张三')
        self.driver.find_element_by_name('userTel').send_keys(13391897269)
        self.driver.find_element_by_xpath(".//*[@id='buyMethod']/li[1]").click()
        sleep(2)
        db = MySQLHelper(host='10.2.0.202', user='xingdb_read', password='abc.1234%', db='che100')
        sql = "SELECT name FROM che100.`tc_apply` WHERE phone = '张三' ORDER BY id DESC;"
        result = db.query_all(sql)
        self.assertEqual(result, '13391897269')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
