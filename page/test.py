# -*- coding: utf-8 -*-
# File : test.py
# Author: Off
# Date : 2022/2/14
# Desc :
import time

from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

FirstPage().action()
time.sleep(3)

HotelSearchPage().action()
time.sleep(3)

def loop1(*, hotelname=None):
    HotelListPage().action1()
    time.sleep(3)

    # HotelListSearchPage().action('杭州浙勤开元名都大酒店')
    HotelListSearchPage().action(hotelname)

    time.sleep(3)

    HotelListPage(hotelname).action2()
    time.sleep(3)

    a = HotelDetailPage().action()
    print(a)


def loop2(history_hotelname, hotelname):
    HotelListPage(name=history_hotelname).action3()
    time.sleep(3)

    # HotelListSearchPage().action('杭州浙勤开元名都大酒店')
    HotelListSearchPage().action(hotelname)

    time.sleep(3)

    HotelListPage(hotelname).action2()
    time.sleep(3)

    a = HotelDetailPage().action()
    print(a)


loop1(hotelname='杭州浙勤开元名都大酒店')

loop2('杭州浙勤开元名都大酒店', '南京固城湾开元度假酒店')