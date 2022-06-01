# -*- coding: utf-8 -*-
# File : autorun.py
# Author: Off
# Date : 2022/5/24
# Desc : 定时任务

import os
import random
import time

import schedule
from appium import webdriver

from comm.basepage import BasePage
from comm.config import getConfigData, Excel
from comm.linuxCon import LinuxBase
from run.step import Step

workbook = getConfigData('Excel').get('workbook')
configData = getConfigData('trip')
bigdata = getConfigData('bigdata')


def job(*, hotel, driver, file):
    """

    :param hotel:
    :param driver:
    :param file:
    :return:
    """

    step = Step(driver, workbook)
    if len(hotel) == 0:
        return []
    elif len(hotel) > 0:
        try:
            step.loop0()
            step.loop1(hotelName=hotel[0], filename=file)
            if len(hotel) > 1:
                for i in range(1, len(hotel)):
                    a = random.randint(3, 5)
                    time.sleep(a)
                    try:
                        step.loop2(hotel[i - 1], hotel[i], filename=file)
                    except IndexError:
                        continue
                    except Exception as e:
                        for n in range(i, len(hotel)):
                            Excel(workbook_path=workbook, sheet='Sheet1').ExcelW("F", hotel[n][2])
                            step.faiList.append(hotel[n])
                        pass
        except Exception:
            for n in range(0, len(hotel)):
                Excel(workbook_path=workbook, sheet='Sheet1').ExcelW("F", hotel[n][2])
                step.faiList.append(hotel[n])
            pass
        finally:
            BasePage(webDriver=driver).driver.quit()
            return step.faiList


def run():
    """
    第一家酒店数据准确并能执行完整，才会失败酒店再次获取数据
    :return:
    """

    hotel = Excel(workbook_path=workbook, sheet='Sheet1').numR(3)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', configData)
    timestamp = time.strftime('%Y%m%d%H%M%S')
    fileDir = os.path.join(os.path.dirname(__file__), '../data')
    file = os.path.abspath(fileDir + '/' + 'ctrip' + timestamp + '.txt')
    filename = 'ctrip' + timestamp + '.txt'

    print(hotel)
    print('\n')
    faiList = job(driver=driver, hotel=hotel, file=file)

    if len(faiList) > 0:
        driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', configData)
        print(faiList)
        job(driver=driver1, hotel=faiList, file=file)

    # LinuxBase(bigdata).upload(file, f'/home/bigdata/{filename}')


if __name__ == '__main__':

    run()

    # schedule.every().day.at('11:19:00').do(run)
    #
    # while True:
    #     schedule.run_pending()
