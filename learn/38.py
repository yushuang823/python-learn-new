'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''
n = int(input('输入一个数：\n'))
a = [2, 5, 7, 9, 11]
h = len(a)
# for i in range(h):
#     if a[-1] < n:
#         a.append(n)
#         break
#     elif n < a[i]:
#         a.insert(i, n)
#         break
# print(a)


if a[-1] < n:
    a.append(n)
else:
    for i in range(h):
        if n < a[i]:
            a.insert(i, n)
            break


print(a)


