"""
输出 9*9 乘法口诀表。
> 分行与列考虑，共9行9列，i控制行，j控制列。
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}\t'.format(j, i, i * j), end=' ')  # end的默认值是\n  end= '' 表示不换行
    print()  # end默认值是\n 自动换行
