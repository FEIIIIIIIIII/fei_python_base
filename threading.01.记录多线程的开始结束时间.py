#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File    :   threading.01.记录多线程的开始结束时间.py
Time    :   2025/01/04 13:31:43
Author  :   afei 
Version :   python 3.11
'''

import threading
import time

#定义一个要使用多线程的函数，函数名为say_hello，传递2个参数，分别是what和delay
def say_hello(what,delay):
    print(what)
    time.sleep(delay)
    print(what)

t = threading.Thread(target=say_hello,args=('hello',3))

print(f'程序开始执行时间 {time.strftime('%X')}')

t.start()

#用join()方法，捕捉用多线程运行的函数say_hello的开始和结束时间
t.join()
print(f'程序结束执行时间 {time.strftime('%X')}')
