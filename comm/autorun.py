# -*- coding: utf-8 -*-
# File : autorun.py
# Author: Off
# Date : 2022/3/17
# Desc : 定时任务

import os
import random
import time

import schedule
from appium import webdriver

from comm.basepage import BasePage
from comm.config import Excel, getConfigData
from comm.linuxCon import LinuxBase
from page.first_page import FirstPage
from page.hotelDetail_page import HotelDetailPage
from page.hotelListSearch_page import HotelListSearchPage
from page.hotelList_page import HotelListPage
from page.hotelSearch_page import HotelSearchPage

excel = getConfigData('Excel').get('workbook')
hotel = Excel(workbook_path=excel, sheet='Sheet1').ExcelR()
configData = getConfigData('trip')
bigdata = getConfigData('bigdata')

def loop1(hotelName: tuple, *, filename, driver, row=0):
    HotelListPage(driver=driver).action1()
    HotelListSearchPage(hotelName[0], driver=driver).action()
    HotelListPage(hotelName[0], driver=driver).action2()
    data = HotelDetailPage(webDriver=driver).action()

    data_dict = {hotelName: data}
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(str(data_dict) + '\n')
    print('success')


def loop2(pastHotel: tuple, hotelNow: tuple, *, filename, driver):
    HotelListPage(name=pastHotel[0], driver=driver).action3()
    HotelListSearchPage(hotelNow[0], driver=driver).action()

    b = random.randint(3, 6)
    time.sleep(b)

    HotelListPage(hotelNow[0], driver=driver).action2()
    data = HotelDetailPage(webDriver=driver).action()
    data_dict = {hotelNow: data}
    with open(filename, mode='a', encoding='UTF-8') as f:
        f.write(str(data_dict) + '\n')
    print('success')

class Gob(object):
    start_data = 1

    def running1(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', configData)

        timestamp = time.strftime('%Y%m%d%H%M%S')
        fileDir = os.path.join(os.path.dirname(__file__), '../data')
        file = os.path.abspath(fileDir + '/' + 'ctrip' + timestamp + '.txt')
        filename = 'ctrip' + timestamp + '.txt'

        FirstPage(webDriver=driver).action()
        time.sleep(3)
        HotelSearchPage(webDriver=driver).action()
        time.sleep(3)

        loop1(hotelName=hotel[Gob.start_data-1], filename=file, driver=driver)
        for i in range(Gob.start_data, Gob.start_data+1):
            a = random.randint(3, 6)
            time.sleep(a)
            try:
                loop2(hotel[i - 1], hotel[i], filename=file, driver=driver)
            except Exception:
                break

        BasePage(webDriver=driver).driver.quit()

        LinuxBase(bigdata).upload(file, f'/home/bigdata/{filename}')

        Gob.start_data = self.start_data + 2


if __name__ == '__main__':
    schedule.every().day.at('11:19:00').do(Gob().running1)
    schedule.every().day.at('11:28:00').do(Gob().running1)

    while True:
        schedule.run_pending()




