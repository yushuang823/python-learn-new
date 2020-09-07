"""
使用lambda来创建匿名函数
lambda arg1, arg2 : expression(表达式)
lambda函数也叫匿名函数
ambda与def的区别：
1）def创建的方法是有名称的，而lambda没有。
2）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。
3）lambda只是一个表达式，而def则是一个语句。
4）lambda表达式” : “后面，只能有一个表达式，def则可以有多个。
5）像if或for或print等语句不能用于lambda中，def可以。
6）lambda一般用来定义简单的函数，而def可以定义复杂的函数。
6）lambda函数不能共享给别的程序调用，def可以。
lambda语法格式：
lambda 变量 : 要执行的语句
"""
# 单个参数
g = lambda x: x ** 2
print(g(4))

# 多个参数
s = lambda x, y: x ** y
print(s(2, 3))

# 使用 lambda 来创建匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4])))
