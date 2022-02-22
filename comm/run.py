# -*- coding: utf-8 -*-
# File : run.py
# Author: Off
# Date : 2022/2/11
# Desc : 运行
import os
import random
import time

from comm.basepage import BasePage
from comm.config import Excel, getConfigData
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

excel = getConfigData('Excel').get('workbook')

hotel = Excel(workbook_path=excel, sheet='Sheet1').ExcelR()


def loop1(hotelName: tuple, *, filename, row=0):
    HotelListPage().action1()
    HotelListSearchPage(hotelName[0]).action()
    HotelListPage(hotelName[0]).action2()
    data = HotelDetailPage().action()

    data_dict = {hotelName: data}
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(str(data_dict) + '\n')
    print('success')


def loop2(pastHotel: tuple, hotelNow: tuple, *, filename):
    HotelListPage(name=pastHotel[0]).action3()
    HotelListSearchPage(hotelNow[0]).action()

    b = random.randint(3, 6)
    time.sleep(b)

    HotelListPage(hotelNow[0]).action2()
    data = HotelDetailPage().action()
    data_dict = {hotelNow: data}
    with open(filename, mode='a', encoding='UTF-8') as f:
        f.write(str(data_dict) + '\n')
    print('success')


while True:
    timestamp = time.strftime('%Y%m%d%H%M%S')
    fileDir = os.path.join(os.path.dirname(__file__), '../data')
    file = os.path.abspath(fileDir + '/' + 'ctrip' + timestamp + '.txt')

    FirstPage().action()
    time.sleep(3)
    HotelSearchPage().action()
    time.sleep(3)

    loop1(hotelName=hotel[0], filename=file)
    for i in range(1, len(hotel)):

        a = random.randint(3, 6)
        time.sleep(a)

        loop2(hotel[i - 1], hotel[i], filename=file)

    BasePage().driver.quit()

    time.sleep(60*60*10)