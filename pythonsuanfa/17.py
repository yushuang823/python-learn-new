"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
> 关键是计算出每一项的值。
"""
n = int(input('输入n:\n'))
a = input('输入a:\n')
s = []
x = 0
for i in range(1, n+1):
    s.append(int(a*i))
print(s)
print(sum(s))


for i in range(n):
    x += a*(10*i)
    s.append(x)

s = [2]
tn = 2
for i in range(1,5):
    tn = tn*10 + s[0]
    s.append(tn)
print(s)
print(sum(s))


