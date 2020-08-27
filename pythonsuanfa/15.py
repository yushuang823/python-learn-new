'''
输出指定格式的日期。
> 使用 datetime 模块。
'''


import datetime, time
form = '%Y-%m-%d'


# 日期对象
date1 = datetime.date(2020, 8, 27)
print('今日日期是：{}'.format(date1.strftime(form)))

# 日期运算
date2 = date1 + datetime.timedelta(20)
print('20天之后的日期是：', date2.strftime(form))

# 日期替换
date3 = date2.replace(year=2002, month=10, day=1)
print(date3.strftime(form))

# 当前日期
date4 = datetime.date.today()
print('今天日期是：', date4.strftime(form))

# 当地时间
date5 = time.localtime(time.time())
print(time.strftime(form, date5))
