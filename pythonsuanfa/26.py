'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
> 递归实际上是一种函数堆栈。
'''
s = input('输入字符串：\n')


def fn(str):
    if str == '':
        return str
    print(str[-1])
    return fn(str[:-1])


print(fn(s))
