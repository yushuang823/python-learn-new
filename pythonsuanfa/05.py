'''
输入三个整数x,y,z，请把这三个数由小到大输出。
> 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''
# x,y,z进行两两比较


if __name__ == '__main__':
    x = input('first number:')
    y = input('second number:')
    z = input('third number:')
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    print(x, y, z)
