# -*- coding: utf-8 -*-
# File : step.py
# Author: Off
# Date : 2022/5/19
# Desc :
import json
import os
import random
import time

from appium import webdriver

from comm.basepage import BasePage
from comm.config import Excel, getConfigData
from comm.linuxCon import LinuxBase
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

class Step(object):

    def __init__(self, driver):
        self.driver = driver

    def loop1(self, hotelName: tuple, *, filename):
        """
        打开应用到获取第一家酒店数据
        :param hotelName:  酒店名
        :param filename: 数据写入文件路径
        :return:
        """
        FirstPage(webDriver=self.driver).action()
        time.sleep(3)
        HotelSearchPage(webDriver=self.driver).action()
        time.sleep(3)
        HotelListPage(driver=self.driver).action1()
        HotelListSearchPage(hotelName[0], driver=self.driver).action()
        HotelListPage(hotelName[0], driver=self.driver).action2()
        data = HotelDetailPage(webDriver=self.driver).action()

        data_dict = {(hotelName[0], hotelName[1]): data}

        return data_dict

    def loop2(self, pastHotel: tuple, hotelNow: tuple, *, filename):
        """
            第二家开始的酒店
            :param pastHotel: 上此搜索的酒店
            :param hotelNow: 本次搜索酒店
            :param filename:
            :return:
            """
        HotelListPage(name=pastHotel[0], driver=self.driver).action3()
        HotelListSearchPage(hotelNow[0], driver=self.driver).action()

        b = random.randint(3, 6)
        time.sleep(b)

        HotelListPage(hotelNow[0], driver=self.driver).action2()
        data = HotelDetailPage(webDriver=self.driver).action()
        data_dict = {(hotelNow[0], hotelNow[1]): data}

        return data_dict
