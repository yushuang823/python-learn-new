"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
"""
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
res = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(x)):   # 行
    for j in range(len(x[0])):  # 列
        res[i][j] = x[i][j] + y[i][j]
for i in res:
    print(i)
print(res)