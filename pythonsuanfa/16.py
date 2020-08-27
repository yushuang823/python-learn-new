"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
> 利用while语句,条件为输入的字符不为'\n'。
"""
import string

letters = 0  # 字母个数
space = 0  # 空格数
digit = 0  # 数字个数
others = 0  # 其它字符
s = input('请输入字符：\n')

for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        others += 1

print('该字符中有{}个字母{}个空格{}个数字{}个字符'.format(letters, digit, space, others))



