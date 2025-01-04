#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File    :   os.02.创建文件夹.py
Time    :   2025/01/04 13:31:37
Author  :   afei 
Version :   python 3.11
'''

import os
import datetime

current_date = datetime.datetime.now()
current_datetime = current_date.strftime(f'%Y-%m-%d')

os.mkdir('./backup_%s' %(current_datetime))

back_config = open('./backup_%s/'%(current_datetime) + 'ip' + '_backupconfig.txt','a')
back_config.close()