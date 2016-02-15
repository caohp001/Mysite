#!/usr/bin/env python
# encoding: utf-8
__author__ = "caoHP"
import unittest
import time
import os
import HTMLTestRunner
from test_case import sold
from test_case import tuanche
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def send_mail(file_name):
    mail_from = 'caohp001@126.com'
    mail_to = ['hongpeng.cao@tuanche.com', 'dabang.xing@tuanche.com', 'changlei.chen@tuanche.com']
    # 定义正文
    f = open(file_name, 'rb')
    mail_body = f.read()
    f.close()
    # print mail_body
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = 'TuanChe Test Report'
    # 定义发送时间
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    print 'Began to link the mail server'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    print 'enter user name password'
    smtp.login(mail_from, '60346533')
    print 'Began send Email'
    smtp.starttls()
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'Email has send out!'


def get_report():
    result_dir = './report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(os.getcwd() + '\\report\\' + fn) if not
               os.path.isdir(os.getcwd() + '\\report\\' + fn) else 0)
    print lists
    file_name = os.path.join(os.getcwd() + '\\report\\', lists[-1])
    print file_name
    send_mail(file_name)


testUnit = unittest.TestSuite()
testUnit.addTest(unittest.makeSuite(sold.Sold))
testUnit.addTest(unittest.makeSuite(tuanche.TuAnChe))


now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = os.getcwd() + '\\report\\' + now + 'result.html'

fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'团车养车测试报告',
    description=u'用例执行情况:')
runner.run(testUnit)

time.sleep(3)
get_report()
