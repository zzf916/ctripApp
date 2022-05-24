# -*- coding: utf-8 -*-
# File : autorun.py
# Author: Off
# Date : 2022/5/24
# Desc :

import os
import random
import time
from appium import webdriver

from comm.basepage import BasePage
from comm.config import getConfigData, Excel
from comm.linuxCon import LinuxBase
from run.step import Step

workbook = getConfigData('Excel').get('workbook')
configData = getConfigData('trip')
bigdata = getConfigData('bigdata')


def job(*, hotel, driver, file, filename):
    if len(hotel) == 0:
        return None
    elif len(hotel) > 0:
        Step(driver, workbook).loop0()
        Step(driver, workbook).loop1(hotelName=hotel[0], filename=file)
        if len(hotel) > 1:
            for i in range(1, len(hotel)):
                a = random.randint(3, 6)
                time.sleep(a)

                Step(driver, workbook).loop2(hotel[i - 1], hotel[i], filename=file)

        BasePage(webDriver=driver).driver.quit()
        # LinuxBase(bigdata).upload(file, f'/home/bigdata/{filename}')


def run():
    """

    :return:
    """

    hotel = Excel(workbook_path=workbook, sheet='Sheet1').numR(8)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', configData)
    timestamp = time.strftime('%Y%m%d%H%M%S')
    fileDir = os.path.join(os.path.dirname(__file__), '../data')
    file = os.path.abspath(fileDir + '/' + 'ctrip' + timestamp + '.txt')
    filename = 'ctrip' + timestamp + '.txt'

    job(driver=driver, hotel=hotel, file=file, filename=filename)


if __name__ == '__main__':
    run()