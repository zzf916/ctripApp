# -*- coding: utf-8 -*-
# File : run.py
# Author: Off
# Date : 2022/2/11
# Desc : 运行
import os
import time

from comm.config import Excel, getConfigData
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage


excel = getConfigData('Excel').get('workbook')

hotel = Excel(workbook_path=excel, sheet='Sheet1').ExcelR()


def loop1(*, filename, hotelName=None, row=0):
    HotelListPage().action1()
    HotelListSearchPage().action(hotelName)
    HotelListPage(hotelName).action2()
    data = HotelDetailPage().action()

    data_dict = {hotelName: data}
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(str(data_dict))
    print('success')


def loop2(pastHotel, hotelNow, *, filename):
    HotelListPage(name=pastHotel).action3()
    HotelListSearchPage().action(hotelNow)
    HotelListPage(hotelNow).action2()
    data = HotelDetailPage().action()
    data_dict = {hotelNow: data}
    with open(filename, mode='a', encoding='UTF-8') as f:
        f.write(str(data_dict))
    print('success')


while True:
    timestamp = time.strftime('%Y-%m-%d %H%M%S')
    fileDir = os.path.join(os.path.dirname(__file__), '../data')
    file = os.path.abspath(fileDir + '/' + '携程App数据' + timestamp + '.txt')

    FirstPage().action()
    time.sleep(3)
    HotelSearchPage().action()
    time.sleep(3)

    loop1(hotelName=hotel[0],filename=file)
    for i in range(1, len(hotel)):
        loop2(hotel[i - 1], hotel[i], filename=file)
