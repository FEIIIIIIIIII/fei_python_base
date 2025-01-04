#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File    :   os.01.用os模块的ping.py
Time    :   2025/01/04 13:31:31
Author  :   afei 
Version :   python 3.11
'''

import os

iplist = open('ip_list.txt')

for ip in iplist:
    result = os.system('ping -n 3 ' + ip)
    if result == 0:    #或者使用'Reply from ' in str(result)进行判断
        print(ip + ' 网络可达')
    else:
        print(ip + ' 网络不可达')

iplist.close()