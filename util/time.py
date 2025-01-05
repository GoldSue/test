#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 11:37
# @Author  : libaojin
# @File    : time.py
from datetime import datetime, timedelta

# 获取当前时间的字符串格式
def now_data_time(format='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(format)

def now_data(format='%Y-%m-%d'):
    return datetime.now().strftime(format)

def now_time(format='%H:%M:%S'):
    return datetime.now().strftime(format)

# 将字符串解析为日期对象
def date_time_paras(time_str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.strptime(time_str, format)

def date_paras(time_str, format='%Y-%m-%d'):
    return datetime.strptime(time_str, format)

def time_paras(time_str, format='%H:%M:%S'):
    return datetime.strptime(time_str, format)

# 计算两个时间的差值
def calculate_time_difference(start, end):
    return (end - start).total_seconds()


def adjust_time(base_time=None, days=0, hours=0, minutes=0, seconds=0):

    if base_time is None:
        base_time = datetime.now()  # 如果没有提供基准时间，使用当前时间

    adjustment = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return base_time + adjustment

