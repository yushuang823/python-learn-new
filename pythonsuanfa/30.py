if __name__ == '__main__':
    s = ['1', '2', 3, 4, 5, 6, 7]
    # l = s[::]
    # print(l)
    print(s[:4:-2])  # [60]4是从左到右索引为4的位置
    print(s[-2:2:-2])  # [50]2是索引 -2是倒数第二个位置
