# -*- coding: utf-8 -*-
# File : ip.py
# Author: Off
# Date : 2022/2/18
# Desc :
import time

import schedule

a = 1


class Test(object):
    a = 1

    def run1(self):
        print(time.localtime())
        print(self.a)
        print(Test.a)
        Test.a = Test.a + 8
        # print(a)

    # def run2(self):
    #     print(time.localtime())
    #     print(self.a)


if __name__ == '__main__':
    # instance = Test()
    # schedule.every().day.at('10:32:00').do(instance.run1)
    # schedule.every().day.at('10:28:00').do(instance.run1)
    #
    # while True:
    #     schedule.run_pending()
    Test().run1()
    Test().run1()
    Test().run1()
