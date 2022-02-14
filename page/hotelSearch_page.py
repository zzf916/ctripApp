# -*- coding: utf-8 -*-
# File : hotelSearch_page.py
# Author: Off
# Date : 2022/2/13
# Desc :
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelSearchPage(BasePage):
    # 弹窗取消按钮
    popup = (By.XPATH, '//*[@class="android.widget.Image" and @text="close-icon-white"]')
    # 查询按钮
    search = (By.XPATH, '//*[@resource-id="ctrip.android.view:id/a" and @text="查 询"]')

    def action(self):
        self.locator(self.popup).click()
        self.locator(self.search).click()
