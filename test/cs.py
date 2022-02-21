# -*- coding: utf-8 -*-
# File : cs.py
# Author: Off
# Date : 2022/2/18
# Desc :


import xml.dom.minidom

import re

line = "this hdr-biz model server"
pattern = "hdrq-biz"
m = re.search(pattern, line)
print(m)