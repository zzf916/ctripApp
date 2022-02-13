# -*- coding: utf-8 -*-
# Author: Off
# Date : 2022/2/12
# Desc :
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from comm.config import getConfigData
from comm.logs import Logging

data = getConfigData('trip')
log = Logging().logger
webDriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', data)

class BasePage(object):

    def __init__(self):
        self.driver = webDriver
        self.width = self.driver.get_window_size().get('width')
        self.height = self.driver.get_window_size().get('height')


    def locator(self, loc, index=0):
        try:
            WebDriverWait(self.driver, 15, 1).until(lambda driver: driver.find_elements(*loc)[index].is_displayed())
            log.info("获取到元素：%s" % str(loc))
            return self.driver.find_elements(*loc)[index]
        except TimeoutException:
            log.info("获取元素失败：%s" % str(loc))
