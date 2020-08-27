"""
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
> 兔子的规律为数列1,1,2,3,5,8,13,21....
"""
month = input('请输入月份：\n')
a = 0
b = 1
if month.isdigit():
    month = int(month)
    for i in range(1, month):
        a, b = b, a + b
    print('第{}个月有{}对兔子'.format(month, b))
else:
    print('输入错误请重新输入')
