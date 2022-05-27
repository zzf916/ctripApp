# -*- coding: utf-8 -*-
# File : step.py
# Author: Off
# Date : 2022/5/19
# Desc : 流程

import random
import time
from comm.config import Excel
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

class Step(object):

    def __init__(self, driver, workbook):
        self.faiList = []
        self.driver = driver
        self.workbook = workbook

    def loop0(self):
        """
        开始-酒店列表
        :return:
        """
        FirstPage(webDriver=self.driver).action()
        time.sleep(3)
        HotelSearchPage(webDriver=self.driver).action()
        time.sleep(3)

    def loop1(self, hotelName: tuple, *, filename):
        """
        打开应用到获取第一家酒店数据
        :param hotelName:  酒店名
        :param filename: 数据写入文件路径
        :return:
        """
        try:
            HotelListPage(driver=self.driver).action1()
            HotelListSearchPage(hotelName[0], driver=self.driver).action()
            HotelListPage(hotelName[0], driver=self.driver).action2()
            data = HotelDetailPage(webDriver=self.driver).action()

            data_dict = {(hotelName[0], hotelName[1]): data}
            with open(filename, mode='w', encoding='UTF-8') as f:
                f.write(str(data_dict) + '\n')

            Excel(workbook_path=self.workbook, sheet='Sheet1').ExcelW("S", hotelName[2])
            print('success')
            return data_dict
        except Exception as e:
            self.faiList.append(hotelName)
            Excel(workbook_path=self.workbook, sheet='Sheet1').ExcelW("F", hotelName[2])
            raise e



    def loop2(self, pastHotel: tuple, hotelNow: tuple, *, filename):
        """
            第二家开始的酒店
            :param pastHotel: 上此搜索的酒店
            :param hotelNow: 本次搜索酒店
            :param filename:
            :return:
        """
        try:

            HotelListPage(name=pastHotel[0], driver=self.driver).action4()
            HotelListSearchPage(hotelNow[0], driver=self.driver).action()

            b = random.randint(3, 6)
            time.sleep(b)

            HotelListPage(hotelNow[0], driver=self.driver).action2()
            data = HotelDetailPage(webDriver=self.driver).action()
            data_dict = {(hotelNow[0], hotelNow[1]): data}
            with open(filename, mode='w', encoding='UTF-8') as f:
                f.write(str(data_dict) + '\n')
            Excel(workbook_path=self.workbook, sheet='Sheet1').ExcelW("S", hotelNow[2])

            print('success')
            return data_dict
        except Exception as e:
            self.faiList.append(hotelNow)

            Excel(workbook_path=self.workbook, sheet='Sheet1').ExcelW("F", hotelNow[2])
            raise e

