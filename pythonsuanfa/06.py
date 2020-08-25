"""
斐波那契数列。
> 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""
arr = [0,1]


def fib(n):
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
        arr.append(b)
    return a, arr


if __name__ == '__main__':
    print(fib(15))

