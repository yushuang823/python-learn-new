"""
利用递归方法求5!。
> 递归公式：fn=fn_1*4!
"""


def fn(n):
    if n == 0:
        return 1
    return n * fn(n-1)


print(fn(5))
