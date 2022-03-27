# -*- coding: utf-8 -*-
# File : run.py
# Author: Off
# Date : 2022/2/11
# Desc : 立即运行
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

excel = getConfigData('Excel').get('workbook')
hotel = Excel(workbook_path=excel, sheet='Sheet1').ExcelR()
configData = getConfigData('trip')
bigdata = getConfigData('bigdata')

def loop1(hotelName: tuple, *, filename, driver, row=0):
    """
    打开应用到获取第一家酒店数据
    :param hotelName: 酒店名
    :param filename: 数据写入文件路径
    :param driver: driver对象
    :param row:
    :return:
    """
    HotelListPage(driver=driver).action1()
    HotelListSearchPage(hotelName[0], driver=driver).action()
    HotelListPage(hotelName[0], driver=driver).action2()
    data = HotelDetailPage(webDriver=driver).action()

    data_dict = {hotelName: data}
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(str(data_dict) + '\n')
    print('success')


def loop2(pastHotel: tuple, hotelNow: tuple, *, filename, driver):
    """
    第二家开始的酒店
    :param pastHotel: 上此搜索的酒店
    :param hotelNow: 本次搜索酒店
    :param filename:
    :param driver:
    :return:
    """
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


def running1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', configData)

    timestamp = time.strftime('%Y%m%d%H%M%S')
    fileDir = os.path.join(os.path.dirname(__file__), '../data')
    file = os.path.abspath(fileDir + '/' + 'ctrip' + timestamp + '.txt')
    filename = 'ctrip' + timestamp + '.txt'

    FirstPage(webDriver=driver).action()
    time.sleep(3)
    HotelSearchPage(webDriver=driver).action()
    time.sleep(3)

    loop1(hotelName=hotel[0], filename=file, driver=driver)
    for i in range(1, int(len(hotel) / 2)):
        a = random.randint(3, 6)
        time.sleep(a)

        loop2(hotel[i - 1], hotel[i], filename=file, driver=driver)

    BasePage(webDriver=driver).driver.quit()

    LinuxBase(bigdata).upload(file, f'/home/bigdata/{filename}')

    # time.sleep(60 * 60 * 10)


if __name__ == '__main__':
    running1()
    time.sleep(3)

