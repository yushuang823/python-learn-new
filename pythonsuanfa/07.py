"""
将一个列表的数据复制到另一个列表中。
> 使用列表[:]。
"""
c = ["m", "n", "g"]
b = []
for i in c:
    b.append(i)
print(b)

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = a[:]
    print(b)
