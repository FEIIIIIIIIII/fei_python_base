#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File    :   time.02.记录程序运行总用时.py
Time    :   2025/01/04 13:31:55
Author  :   afei 
Version :   python 3.11
'''

import datetime
import time
 
 
start_time = datetime.datetime.now()
print('备份任务开始时间：'+start_time.strftime("%Y年%m月%d日%H时%M分%S秒"))
 
time.sleep(3)#模拟执行任务
 
end_time = datetime.datetime.now()
print('备份任务结束时间：'+end_time.strftime("%Y年%m月%d日%H时%M分%S秒"))
run_time=end_time-start_time
 
hours, remainder = divmod(run_time.total_seconds(), 3600)
minutes, seconds = divmod(remainder, 60)
print(f"本次备份任务运行时间：{int(hours)}小时{int(minutes)}分钟{int(seconds)}秒")