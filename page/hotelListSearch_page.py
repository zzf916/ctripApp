# -*- coding: utf-8 -*-
# File : hotelListSearch_page.py
# Author: Off
# Date : 2022/2/13
# Desc : 酒店搜索
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelListSearchPage(BasePage):
    def __init__(self, hotelname):
        super().__init__()
        self.hotel_name = hotelname
        self.search = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and @class="android.widget.EditText"]')  # 搜索框
        self.hotelList = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and contains(@text, "{}")]'.format(self.hotel_name))  # 酒店列表

    def action(self):
        self.locator(self.search).send_keys(self.hotel_name)
        self.locators(self.hotelList)[1].click()