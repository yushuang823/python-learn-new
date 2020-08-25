"""
输入某年某月某日，判断这一天是这一年的第几天？

> 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。
"""

if __name__ == '__main__':
    day = input('请输入日期：如2020-01-01')
    year = int(day[:4])  # 取年份
    month = int(day[5:7])  # 取月份
    sun = int(day[8:])  # 取日子
    run = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    tal_day = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # 判断是否是闰年
        for i in range(month - 1):
            tal_day += run[i]
    else:
        for i in range(month - 1):
            tal_day += p[i]
    print('该日期是{}年的{}天'.format(year, tal_day + sun))  # 本月份之前的天数加上本月天数
