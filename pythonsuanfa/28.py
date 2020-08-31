"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
> 学会分解出每一位数。
"""


n = int(input('请输入不超过5位的数字：\n'))
a = n // 10000   # 万
b = n % 10000 // 1000   # 千
c = n % 1000 // 100   # 百
d = n % 100 // 10  # 十
e = n % 10    # 个


if a != 0:
    print('这是一个五位数：', e, d, b, c, a)
elif b != 0:
    print('四位数：', e, d, c, b)
elif c != 0:
    print('三位数：', e, d, c)
elif d != 0:
    print('两位数：',e, d)
else:
    print('一位数：', e)