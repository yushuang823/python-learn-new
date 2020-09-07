"""
求100之内的素数.
"""

L =[]
flag = True

for i in range(1, 100):
    # flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        L.append(i)
print(L)



