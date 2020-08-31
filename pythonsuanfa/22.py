"""
利用循环打印菱形
> 先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
"""
n = 7
for i in range(int(n/2) + 1):
    print(' '*(int(n/2) - i), end='')
    print('*'*(2*i + 1))
for j in range(int(n/2)):
    print(' '*(j + 1), end='')
    print('*'*(5 - 2*j))
