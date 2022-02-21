# -*- coding: utf-8 -*-
# File : hotelDetail_page.py
# Author: Off
# Date : 2022/2/14
# Desc : 酒店详情页
import os
import re
import time

from selenium.webdriver.common.by import By

from comm.basepage import BasePage


def getData(*, list2: list):
    list1 = [("早餐", "早餐"), ("人床", "床型"), ("入住", "人数"), ("㎡", "平方")]
    dict_ = {"早餐": None, "床型": None, "人数": None, "平方": None}
    for i in list1:
        for d in list2:
            if re.search(i[0], d) is not None:
                dict_[i[1]] = d
                break
            else:
                continue
    return dict_


class HotelDetailPage(BasePage):
    roomDetail = (By.XPATH, "//*[contains(@content-desc, '入住') and @class='android.view.View']")  # 房间
    roomPrice = (By.XPATH, "//*[contains(@content-desc, '¥')]")  # 价格

    exitFlag = (By.XPATH, "//*[contains(@content-desc, '开元酒店集团官方旗舰店') and @class='android.view.View']")  # 结束标记

    returnFlag = (By.XPATH, "//android.view.View[@content-desc='收藏']/preceding-sibling::android.view.View[1]")  # 返回标记

    def action(self):
        time.sleep(5)
        list_ = []
        for i in range(8):

            timestamp = time.strftime('%Y%m%d%H%M%S')
            fileDir = os.path.join(os.path.dirname(__file__), '../sources')
            file = os.path.abspath(fileDir + '/' + 'ctripPageSources' + timestamp + '.xml')
            # print(self.driver.page_source)
            with open(file, mode='w', encoding='utf-8') as f:
                f.write(self.driver.page_source)

            rooms = self.locators(self.roomDetail)
            if rooms is not None:
                for room in rooms:
                    # time.sleep(3)
                    try:
                        price = room.find_element_by_xpath("//*[contains(@content-desc, '¥')]").get_attribute(
                            'content-desc').replace('\n', "")
                    except Exception:
                        price = None
                    room_detail = room.get_attribute("content-desc").split('\n')
                    dict_ = getData(list2=room_detail)
                    dict_['价格'] = price
                    dict_['房型'] = room_detail[0]
                    # a = '({}, {})'.format(room_detail, price)
                    list_.append(str(dict_))

            # print(list_)
            if self.locator(self.exitFlag) is None:
                self.driver.swipe(self.width / 2, self.height * 0.8, self.width / 2, self.height * 0.3, duration=1500)
            else:
                break
        self.driver.back()
        # self.locator(self.returnFlag).click()

        l2 = sorted(set(list_), key=list_.index)
        return l2
