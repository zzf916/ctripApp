# -*- coding: utf-8 -*-
# File : hotelList_page.py
# Author: Off
# Date : 2022/2/13
# Desc : 酒店列表
import random
import time

from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelListPage(BasePage):

    def __init__(self, name="hh", *, driver):
        super().__init__(webDriver=driver)
        self.hotel_name = name
        self.hotel = (By.XPATH, '//*[contains(@content-desc, "{}")]'.format(self.hotel_name))  # 酒店
        self.search = (By.XPATH, '//*[@class="android.widget.ImageView" and @content-desc="关键字/位置/品牌/酒店名"]')  # 搜索框
        self.search2 = (By.CLASS_NAME, 'android.view.View')

    def action1(self):
        a = random.randint(1, 3)
        time.sleep(a)
        self.locator(self.search).click()

    def action2(self):
        a = random.randint(3, 6)
        time.sleep(a)
        self.locators(self.hotel)[1].click()

    def action3(self):
        a = random.randint(1, 3)
        time.sleep(a)
        self.locator(self.hotel).click()

    def action4(self):
        time.sleep(2)
        self.locators(self.search2)[3].click()


