# -*- coding: utf-8 -*-
# File : hotelList_page.py
# Author: Off
# Date : 2022/2/13
# Desc : 酒店列表
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelListPage(BasePage):

    def __init__(self, name):
        super().__init__()
        self.hotel_name = name
        self.hotel = (By.XPATH, '//android.view.View[contains(@content-desc, "{}")]'.format(self.hotel_name))  # 酒店
        self.search = (By.XPATH, '//*[@class="android.widget.ImageView" and @content-desc="关键字/位置/品牌/酒店名"]')  # 搜索框

    def action1(self):
        self.locator(self.search).click()

    def action2(self):
        self.locator(self.hotel).click()