#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File    :   time.01.记录程序运行的开始和结束时间.py
Time    :   2025/01/04 13:31:49
Author  :   afei 
Version :   python 3.11
'''

import time
print(f'程序开始执行时间 {time.strftime('%X')}')
time.sleep(3)
print(f'程序结束执行时间 {time.strftime('%X')}')