# -*- coding: utf-8 -*-
# File : hotelDetail_page.py
# Author: Off
# Date : 2022/2/14
# Desc : 酒店详情页
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


class HotelDetailPage(BasePage):
    roomDetail = (By.XPATH, "//*[contains(@content-desc, '入住') and @class='android.view.View']")  # 房间
    roomPrice = (By.XPATH, "//*[contains(@content-desc, '¥') and @class='android.view.View']")  # 价格

    exitFlag = (By.XPATH, "//*[contains(@content-desc, '开元酒店集团官方旗舰店') and @class='android.view.View']")  # 结束标记

    returnFlag = (By.XPATH, "//android.view.View[@content-desc='收藏']/preceding-sibling::android.view.View[1]")  # 返回标记

    def action(self):
        list_ = []
        for i in range(20):
            rooms = self.locators(self.roomDetail)
            if rooms is not None:
                for room in rooms:
                    price = room.find_element(*self.roomPrice).get_attribute('content-desc')
                    room_detail = room.get_attribute("content-desc")
                    a = '({}, {})'.format(room_detail, price)
                    list_.append(a)
            if self.locator(self.exitFlag) is None:
                self.driver.swipe(self.width / 2, self.height * 0.8, self.width / 2, self.height * 0.5, duration=500)
            else:
                break

        self.locator(self.returnFlag).click()

        return list_
