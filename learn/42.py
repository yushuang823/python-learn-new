"""
求输入数字的平方，如果平方运算后小于 50 则退出。
"""

Flag = True
while Flag:
    n = int(input('输入数字:\n'))
    if pow(n, 2) < 50:
        Flag = False
    else:
        Flag = True

