# -*- coding: utf-8 -*-
# File : test.py
# Author: Off
# Date : 2022/2/14
# Desc :
import time

from comm.config import Excel
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

FirstPage().action()
time.sleep(3)

HotelSearchPage().action()
time.sleep(3)


def loop1(*, hotelname=None, row):
    HotelListPage().action1()

    # HotelListSearchPage().action('杭州浙勤开元名都大酒店')
    HotelListSearchPage().action(hotelname)

    HotelListPage(hotelname).action2()

    a = HotelDetailPage().action()
    Excel(workbook_path='/config\ctrip.xlsx', sheet='Sheet1').ExcelW(str(a), row)


def loop2(history_hotelname, hotelname, row):
    HotelListPage(name=history_hotelname).action3()

    # HotelListSearchPage().action('杭州浙勤开元名都大酒店')
    HotelListSearchPage().action(hotelname)

    HotelListPage(hotelname).action2()

    a = HotelDetailPage().action()
    Excel(workbook_path='/config\ctrip.xlsx', sheet='Sheet1').ExcelW(str(a), row)

    print(a)


a = next(Excel(workbook_path='/config\ctrip.xlsx', sheet='Sheet1').ExcelR())
print(a)
loop1(hotelname='杭州浙勤开元名都大酒店', row=a.get('row'))

# a =next(Excel(workbook_path='D:\github\ctripApp\config\ctrip.xlsx', sheet='Sheet1').ExcelR())

loop2('杭州浙勤开元名都大酒店', '南京固城湾开元度假酒店', a.get('row'))
