# -*- coding: utf-8 -*-
# File : ip.py
# Author: Off
# Date : 2022/2/18
# Desc :
import requests
r = requests.get(url='http://httpbin.org/get')
print(r.text)
