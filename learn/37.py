'''
求一个3*3矩阵主对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''
a = []
for i in range(3):
    for j in range(3):
        n = float(input('输入一个数字：\n'))
        if i == j:
            a.append(n)
print(sum(a))