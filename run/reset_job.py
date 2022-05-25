# -*- coding: utf-8 -*-
# File : reset_job.py
# Author: Off
# Date : 2022/5/25
# Desc : 定时任务--没周一重置酒店数据

import schedule

from comm.config import Excel, log
from run.autorun import workbook


def resetJob():
    """
    清空excel数据
    :return:
    """

    excel = Excel(workbook_path=workbook, sheet='Sheet1')
    for i in range(1, excel.r_max):
        excel.ExcelW(args=None, row=i)
    log.info("数据重置成功")



if __name__ == '__main__':
    schedule.every().monday.do(resetJob)

    while True:
        schedule.run_pending()



