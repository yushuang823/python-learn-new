"""
一个5位数，判断它是不是回文数。
> 回文数，个位与万位相同，十位与千位相同。
"""


n = input('输入一个五位数：\n')
a = len(n)
# b = a // 2
# flag = True


# for i in range(b):
#     if n[i] != n[- 1 - i]:
#         flag = False
#         break
# if flag == True:
#     print('该数是回文')
# else:
#     print('不是回文')


# 双指针法
left, right = 0, a - 1
flag = True
while left < right:
    if n[left] != n[right]:
         flag = False
    left += 1
    right -= 1
if flag == True:
    print('是回文')
else:
    print('不是回文')












