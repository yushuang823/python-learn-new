'''
求1+2!+3!+...+20!的和。
> 此程序只是把累加变成了累乘。
'''
h = 20
l = []
n = 1
for i in range(1, h + 1):
    n = i * n
    l.append(n)
print(sum(l))