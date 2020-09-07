"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
"""
letter = input('请输入第一个字母：')
if letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input('请输入第二个字母：')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')
elif letter == 'W':
    print('Wednesday')
elif letter == 'F':
    print('Friday')
elif letter == 'S':
    letter = input('输入第二个字母：')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data error')