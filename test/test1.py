# -*- coding: utf-8 -*-
# File : test1.py
# Author: Off
# Date : 2022/5/17
# Desc :
import json

import jsonpath

l = [
    '{"房型": "开元双床房- 商祺星卡会员", "早餐": "1份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥570"}',
    '{"房型": "开元双床房- 商祺星卡会员", "早餐": "1份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥570"}',

    '{"房型": "开元双床房￼", "早餐": "无早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥540"}'
]
l2 = list(map(json.loads, l))
l4 = sorted(set(list(map(str, l2))), key=list(map(str, l2)).index)

l3 = jsonpath.jsonpath(l2, '$..房型')
# print(l4)

a = {"a": 11}
b = a.copy()

# print(id(a))
# print(id(b))

l5 = []


def mySum(L):
    if len(L) <= 0:
        return 0
    else:
        l5.append(L)
        k = l5
        print(k)
        return mySum(L[1:])  # 递归呼叫


print(mySum([1, 2, 3, 4, 5, 6]))
print(l5)
