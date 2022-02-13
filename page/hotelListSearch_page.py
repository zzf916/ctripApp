# -*- coding: utf-8 -*-
# File : hotelListSearch_page.py
# Author: Off
# Date : 2022/2/13
# Desc : 酒店搜索
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelListSearchPage(BasePage):
    search = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and @text="关键字/位置/品牌/酒店名"]')  # 搜索框
    hotelList = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and @class="android.view.ViewGroup"]')  # 酒店列表

    def action(self, hotelname):
        self.locator(self.search).send_keys(hotelname)
        self.locator(self.hotelList).click()