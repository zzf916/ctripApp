# -*- coding: utf-8 -*-
# File : cs1.py
# Author: Off
# Date : 2022/1/28
# Desc :
from selenium import webdriver
import time
from appium import webdriver
# from comm.ys import a, b, c, d, e
from selenium.webdriver.common.by import By

from comm.basepage import BasePage

# class TestPage(BasePage):
#     a = (By.XPATH, '//*[@class="android.widget.Image" and @text="close-icon-white"]')  # 取消按钮
#     b = '//*[@class="android.widget.ImageView" and @content-desc="关键字/位置/品牌/酒店名"]'  # 搜索框
#
#     c = '//*[@resource-id="ctrip.android.view:id/a" and @text="关键字/位置/品牌/酒店名"]'  # 输入框
#
#     d = '//*[@resource-id="ctrip.android.view:id/a" and @class="android.view.ViewGroup"]'  # 搜索出的酒店列表
#
#     e = '//android.view.View[contains(@content-desc, "{}")]'.format("杭州浙勤开元名都大酒店")
#
#
# # def appium_desired():
#     a = configR().conR('xc')
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', a)
#     driver.implicitly_wait(8)
#     return driver

a = (By.XPATH, '//android.widget.FrameLayout[@content-desc="酒店"]/android.widget.FrameLayout/android'
               '.widget.FrameLayout/android.widget.LinearLayout')
b = (By.XPATH, '//*[@class="android.widget.Image" and @text="close-icon-white"]')  # 取消按钮

c = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and @text="查 询"]')  # 取消按钮
BasePage().locator(a, index=0).click()
try:
    BasePage().locator(b).click()
except Exception:
    print('没有取消按钮')

BasePage().locator(c).click()
print(BasePage().width)

with open('html.xml', 'w', encoding='utf-8') as q:
    q.write(BasePage().driver.page_source)
# if __name__ == '__main__':

# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']

# driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="酒店"]/android.widget.FrameLayout/android'
#                              '.widget.FrameLayout/android.widget.LinearLayout').click()
# try:
#     driver.find_element_by_xpath(a).click()
# except Exception:
#     print('没有取消按钮')
#
# driver.find_element_by_xpath('//*[@resource-id="ctrip.android.view:id/a" and @text="查 询"]').click()
#
# driver.find_element_by_xpath(b).click()
# driver.find_element_by_xpath(c).send_keys('杭州浙勤开元名都大酒店')
# print(driver.page_source)
# driver.find_element_by_xpath(d).click()
# driver.find_elements_by_xpath(e)[1].click()
# time.sleep(5)
#
# # driver.find_element_by_xpath("//*[contains(@content-desc, '杭州浙勤开元名都大酒店')]").click()
# # time.sleep(3)
#
# # driver.swipe(width / 2, height * 0.8, width / 2, height * 0.5, duration=500)
# # a = driver.find_elements_by_xpath("//*[contains(@content-desc, '¥')]")
# # time.sleep(3)
# for c in range(3):
#     try:
#         b = driver.find_elements_by_xpath(
#             "//*[contains(@content-desc, '入住') and not(contains(@content-desc, '编号'))]")
#
#         # print(b.get_attribute('content-desc'))
#         for i in b:
#             c = i.find_element_by_xpath("//*[contains(@content-desc, '¥')]")
#             print(i.get_attribute('content-desc'))
#             print(type(c.get_attribute('content-desc')))
#             print('\n')
#
#         driver.swipe(width / 2, height * 0.8, width / 2, height * 0.5, duration=500)
#     except Exception:
#         driver.swipe(width / 2, height * 0.8, width / 2, height * 0.5, duration=500)
#
#         continue

# print(a)
# c = []
# for i in a:
#     # i.get_attribute('content-desc')
#     c.append(i.get_attribute('content-desc'))
# d = []
# for i in b:
#     d.append(i.get_attribute('content-desc'))
#
# print(c)
# print(d)
