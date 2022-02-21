# -*- coding: utf-8 -*-
# File : css.py
# Author: Off
# Date : 2022/2/21
# Desc :
import re

a = 'IWG5H5\n猜您喜欢\n无早餐\n2张1.3米单人床\n2人入住\n32㎡\n部分禁烟\n免费取消\n立即确认\n免费升房\n延迟退房\n欢迎水果\n预约发票\n免费取消超值价'
b = ['IWG5H5', '猜您喜欢', '无早餐', '2张1.3米单人床', '2人入住', '32㎡', '部分禁烟', '免费取消', '立即确认', '免费升房', '延迟退房', '欢迎水果', '预约发票',
     '免费取消超值价']
print(b)


def getData(*, list2: list):
    list1 = [("早餐", "早餐"), ("人床", "床型"), ("入住", "人数"), ("㎡", "平方")]
    dict_ = {"早餐": None, "床型": None, "人数": None, "平方": None}
    for i in list1:
        for d in list2:
            if re.search(i[0], d) is not None:
                dict_[i[1]] = d
                break
            else:
                continue
    return dict_


c = getData(list2=b)
print(c)
