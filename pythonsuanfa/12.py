"""
判断101-200之间有多少个素数，并输出所有素数。
> 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
from math import sqrt

min = 101
max = 200
prim = []

for i in range(min, max + 1):
    tem = int(sqrt(i))
    flag = True
    for j in range(2, tem + 1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        prim.append(i)


print('{}和{}之间共有{}个素数'.format(min, max, len(prim)), prim)
