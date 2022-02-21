# -*- coding: utf-8 -*-
# Author: Off
# Date : 2022/2/12
# Desc :
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from comm.config import getConfigData
from comm.logs import Logging

data = getConfigData('oppo')
log = Logging().logger
webDriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', data)

class BasePage(object):

    def __init__(self):
        self.driver = webDriver
        self.driver.implicitly_wait(5)
        self.width = self.driver.get_window_size().get('width')
        self.height = self.driver.get_window_size().get('height')


    def locator(self, loc, index=0):
        try:
            # WebDriverWait(self.driver, 5, 1).until(lambda driver: driver.find_element(*loc).is_displayed())
            e = self.driver.find_elements(*loc)[index]
            log.info("获取元素：%s" % str(loc))
            return e
        except Exception:
            log.info("获取元素失败：%s" % str(loc))
            return None


    def locators(self, loc):
        try:
            # WebDriverWait(self.driver, 5, 1).until(lambda driver: driver.find_element(*loc).is_displayed())
            e = self.driver.find_elements(*loc)
            log.info("获取到元素：%s" % str(loc))
            return e
        except Exception:
            log.info("获取元素失败：%s" % str(loc))
            return None

    # # 向上滑动屏幕 左上角坐标（0，0）
    # def swipe_up_to_find_element(self, loc):
    #     for i in range(5):
    #         try:
    #             log.info("第{}次定位：%s".format(i + 1), str(loc))
    #             self.locator(loc).click()
    #             break
    #         except Exception:
    #             log.info("第{}次划屏：%s".format(i + 1), str(loc))
    #             # duration=500 500毫秒执行时间
    #             self.driver.swipe(self.width / 2, self.height * 0.8, self.width / 2, self.height * 0.5,
    #                               duration=500)