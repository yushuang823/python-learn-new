"""
一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

> 在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。

"""


import math


if __name__ == '__main__':
    for i in range(10000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if x ** 2 == i + 100 and y ** 2 == i + 268:
            print(i)