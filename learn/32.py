"""
按相反的顺序输出列表的值。
"""
# a = [1, 2, 3, 4, 5, 6]
# l1 = len(a)
# l2 = []
# for i in range(1, l1 + 1):
#     l2.append(a[l1 - i])
# print(l2)

# 第二种方法
a = [1, 2, 3, 4, 5, 6]
b = []
for i in a[::-1]:
    b.append(i)
print(b)
