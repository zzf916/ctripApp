# -*- coding: utf-8 -*-
# File : test1.py
# Author: Off
# Date : 2022/5/17
# Desc :
import json

import jsonpath

l = ['{"房型": "开元双床房- 商祺星卡会员", "早餐": "1份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥570"}', '{"房型": "开元双床房￼", "早餐": "无早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥540"}', '{"房型": "开元双床房￼", "早餐": "2份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥590"}', '{"房型": "豪华大床房￼", "早餐": "无早餐", "床型": "1张2米特大床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥600"}', '{"房型": "豪华大床房￼", "早餐": "1份早餐", "床型": "1张2米特大床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥630"}', '{"房型": "豪华双床房￼", "早餐": "无早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥600"}', '{"房型": "豪华双床房￼", "早餐": "2份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥650"}', '{"房型": "亲子双床房- 商祺星卡会员", "早餐": "3份早餐", "床型": "2张1.2米单人床", "人数": "2人入住", "平方": "35㎡", "isOrder": false, "价格": "¥690"}', '{"房型": "亲子大床房- 商祺星卡会员", "早餐": "3份早餐", "床型": "1张特大床或2张单人床随机安排", "人数": "2人入住", "平方": "35㎡", "isOrder": true, "价格": "¥790"}', '{"房型": "高级双卧家庭房- 商祺星卡会员", "早餐": "4份早餐", "床型": "2张单人床和1张特大床", "人数": "4人入住", "平方": "70㎡", "isOrder": true, "价格": null}', '{"房型": "豪华双卧亲子房- 商祺星卡会员", "早餐": "4份早餐", "床型": "2张2米特大床", "人数": "4人入住", "平方": "70㎡", "isOrder": true, "价格": "¥1320"}', '{"房型": "豪华套房￼", "早餐": "2份早餐", "床型": "1张2米特大床", "人数": "2人入住", "平方": "70㎡", "isOrder": true, "价格": "¥1320"}']
l2 = list(map(json.loads, l))

l3 = jsonpath.jsonpath(l2, '$..房型')
print(l3)