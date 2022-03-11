# -*- coding: utf-8 -*-
# File : cs.py
# Author: Off
# Date : 2022/2/18
# Desc :
import smtplib
import time
from email.mime.text import MIMEText

import schedule as schedule
from appium.webdriver import webdriver

from comm.config import getConfigData

from selenium import webdriver
import time
from appium import webdriver
EMAIL_SEND_USERNAME = 'ricky.zhao@kaiyuanhotels.com'
# 邮箱密码
EMAIL_SEND_PASSWORD = 'Office10105050'

data = getConfigData('you')

def send_email(receiver):
    if '@sina.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.sina.com'
    elif '@163.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.163.com'
    else:
        smtp_server = 'smtp.exmail.qq.com'
    # code = str(random.randint(1000, 9999))
    # msg = '验证码为' + code
    msg = MIMEText('嘿嘿嘿qq！')
    msg['Subject'] = '嘿嘿嘿！！'
    msg['from'] = EMAIL_SEND_USERNAME
    msg['to'] = receiver

    smtp = smtplib.SMTP(host=smtp_server)
    smtp.connect(smtp_server)
    smtp.starttls()
    smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
    smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
    smtp.quit()


def appium_desired():

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', data)
    driver.implicitly_wait(8)
    driver.find_element_by_id('com.yongyou.youpu:id/tab_app').click()
    driver.find_element_by_id('com.yongyou.youpu:id/logo').click()
    time.sleep(10)
    driver.quit()
    send_email('7358369111@qq.com')

    print('222222')




if __name__ == '__main__':
    send_email('7358369111@qq.com')
    # appium_desired()

    # schedule.every().day.at('22:12:35').do(appium_desired)
    #
    #
    # while True:
    #     schedule.run_pending()
