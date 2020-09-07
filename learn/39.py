"""
将一个数组逆序输出。
程序分析：用第一个与最后一个交换
"""
# 粗暴
a = [1, 2, 3, 4, 5, 6]
# print(a[::-1])


# 简单
b = []
c = len(a)
for i in range(1, c + 1):
    b.append(a[c-i])
print(b)