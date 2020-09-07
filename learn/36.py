"""
对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
"""


# 冒泡法
# a = []
# for i in range(10):
#     b = int(input('请输入要对比的数字：\n'))
#     a.append(b)
#
#
# for i in range(9):         # 9次对比循环
#     for j in range(9 - i):    # 每次对比的个数
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)


# 选择法排序法
# a = []
# for i in range(10):
#     b = int(input('输入对比数字：\n'))
#     a.append(b)
#
#
# for i in range(9):
#     for j in range(i + 1, 10):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)


# 插入法
# a = []
# b = int(input('输入第一个数字：\n'))
# a.append(b)
# for i in range(9):
#     c = int(input('输入数字：\n'))
#     for j in range(i + 1):
#         if c >= a[i - j]:
#             a.insert(i - j + 1, c)
#             break
#         if i - j == 0 and c < a[i - j]:
#             a.insert(i - j, c)
# print(a)


# 快排方法
# 哨兵互走交换的过程就是不断排序的过程。若右边的哨兵先走，不管走多少次，最后相遇时的那个数是小于基准数的。
# 这时与基准数交换，正好分为两个序列。可若是左边的先走，相遇在大于基准数上就不好办了。
# 终止条件 len(n) < 2  列表长度大于1
# 内部While循环的作用是使得左右游标相互靠近
# 外部While循环的作用是不断通过exchange使得“逆序”元素的互相交换， 不断向左子数组小于右子数组的趋势靠近，
def quick_sort(list, left, right):
    if left >= right:  # 递归终止条件
        return list
    i = left
    j = right
    pivot = i
    while i < j:
        while i < j and list[j] > list[pivot]:
            j -= 1
        while i < j and list[i] <= list[pivot]:
            i += 1
        list[i], list[j] = list[j], list[i]
    list[pivot], list[j] = list[j], list[pivot]
    quick_sort(list, left, j - 1)
    quick_sort(list, j + 1, right)
    return list


if __name__ == '__main__':
    n = [6, 1, 2, 7, 9, 18, 4, 5, 10, 8]
    h = len(n)
    print(quick_sort(n, 0, h - 1))
