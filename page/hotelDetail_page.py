# -*- coding: utf-8 -*-
# File : hotelDetail_page.py
# Author: Off
# Date : 2022/2/14
# Desc : 酒店详情页 数据获取

import json
import os
import re
import time
import jsonpath
from selenium.webdriver.common.by import By

from comm.basepage import BasePage


def getData(*, list2: list):
    list1 = [("房", "房型"), ("早餐", "早餐"), ("张", "床型"), ("入住", "人数"), ("㎡", "平方")]
    dict_ = {"房型": None, "早餐": None, "床型": None, "人数": None, "平方": None}
    for i in list1:
        for d in list2:
            if re.search(i[0], d) is not None:
                dict_[i[1]] = d
                break
            else:
                continue
    return dict_


class HotelDetailPage(BasePage):
    roomDetail = (By.XPATH, "//*[contains(@content-desc, '人入住') and @class='android.view.View']")  # 房间
    roomPrice = (By.XPATH, "//*[contains(@content-desc, '¥')]")  # 价格

    exitFlag = (By.XPATH, "//*[contains(@content-desc, '官方旗舰店') and @class='android.widget.ImageView']")  # 结束标记

    returnFlag = (By.XPATH, "//android.view.View[@content-desc='收藏']/preceding-sibling::android.view.View[1]")  # 返回标记

    developFlag = (By.CLASS_NAME, "android.widget.ImageView")  # 展开标记

    developDetail = (By.XPATH, "//*[contains(@content-desc, '立即确认') and not(contains(@content-desc, '㎡')) and @class='android.view.View']")  # 展开后房型



    orderFlag = (By.XPATH, "//*[@content-desc='订') and @class='android.view.View']")  # 可定

    def action(self):
        time.sleep(5)
        list_ = []
        for i in range(8):

            timestamp = time.strftime('%Y%m%d%H%M%S')
            fileDir = os.path.join(os.path.dirname(__file__), '../sources')
            file = os.path.abspath(fileDir + '/' + 'ctripPageSources' + timestamp + '.xml')

            # print(self.driver.page_source)
            # with open(file, mode='w', encoding='utf-8') as f:
            #     f.write(self.driver.page_source)

            rooms = self.locators(self.roomDetail)
            if rooms is not None:
                for room in rooms:
                    roomDetailData = room.get_attribute("content-desc")
                    room_detail = roomDetailData.split('\n')
                    dict_ = getData(list2=room_detail)
                    if len(list_) > 0 and dict_.get('房型') in jsonpath.jsonpath(list_, '$..房型'):
                        continue
                    if '早餐' not in roomDetailData:
                        try:
                            room.find_element_by_class_name("android.widget.ImageView").click()
                            time.sleep(3)
                        except Exception:
                            pass
                        while True:
                            roomDetails = self.locators(self.developDetail)
                            if len(roomDetails) == 0:
                                break
                            for roomD in roomDetails:
                                dict2 = dict_.copy()
                                room_Detail = roomD.get_attribute("content-desc")
                                try:
                                    price = roomD.find_element_by_xpath(
                                        "//*[contains(@content-desc, '¥')]").get_attribute('content-desc').replace('\n', "")
                                except Exception:
                                    price = None
                                try:
                                    roomD.find_element_by_xpath("//*[@content-desc='订' and @class='android.view.View']")
                                    dict2['isOrder'] = True
                                except Exception:
                                    dict2['isOrder'] = False
                                dict2['价格'] = price
                                dict2['早餐'] = room_Detail.split('\n')[0]
                                # list_.append(json.dumps(dict_, ensure_ascii=False))
                                list_.append(dict2)
                            time.sleep(3)
                            if len(roomDetails) <= 4:
                                break
                            if len(roomDetails) > 4:
                                self.driver.swipe(self.width / 2, self.height * 0.8, self.width / 2, self.height * 0.4, duration=2500)
                                time.sleep(2)


                    else:
                        try:
                            price = room.find_element_by_xpath("//*[contains(@content-desc, '¥')]").get_attribute(
                                'content-desc').replace('\n', "")
                        except Exception:
                            price = None
                        try:
                            room.find_element_by_xpath("//*[@content-desc='订' and @class='android.view.View']")
                            dict_['isOrder'] = True
                        except Exception:
                            dict_['isOrder'] = False
                        dict_['价格'] = price
                        # list_.append(json.dumps(dict_, ensure_ascii=False))
                        list_.append(dict_)
            if self.locator(self.exitFlag) is None:
                self.driver.swipe(self.width / 2, self.height * 0.8, self.width / 2, self.height * 0.4, duration=2500)
            else:
                break
        self.driver.back()
        # self.locator(self.returnFlag).click()
        # l2 = sorted(set(list_), key=list_.index)
        l2 = sorted(set(list(map(str, list_))), key=list(map(str, list_)).index)
        return l2
