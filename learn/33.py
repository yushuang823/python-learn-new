"""
按逗号分隔列表。
"""
# 将 字符串、元组、列表、字典中的元素（字符串形式）以指定的字符(分隔符)连接生成一个新的字符串
# 'sep'.join(seq)


a = [1, 2, 3, 4, 5, 6]
b = []
for i in a:
    b.append(str(i))
s1 = ','.join(b)        # 注意：不论是元组，列表，字典或者其他，join()连接的元素都应该是以字符串的形式出
print(s1)

a = ['1', '2', ' 3', '4', ' 5', ' 6']
# s2 = '*'.join(a)
# print(s2)

