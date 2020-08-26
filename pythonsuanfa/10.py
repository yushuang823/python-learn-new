"""
格式化输出当前时间。
> 使用 time 模块，格式为 yyyy-mm-dd HH:mm:ss。
"""
import time

local = time.localtime(time.time())
format = '%Y-%m-%d %H:%M:%S'
print(time.strftime(format, local))
