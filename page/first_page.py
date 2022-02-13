# -*- coding: utf-8 -*-
# File : first_page.py
# Author: Off
# Date : 2022/2/13
# Desc : 首页
from selenium.webdriver.common.by import By

from comm.basepage import BasePage



class FirstPage(BasePage):
    hotel = (By.XPATH, '//android.widget.FrameLayout[@content-desc="酒店"]/android.widget.FrameLayout/android'
                       '.widget.FrameLayout/android.widget.LinearLayout')

    def action(self):
        self.locator(self.hotel).click()


