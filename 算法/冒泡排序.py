"""
冒泡排序算法的流程如下：

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubblesort(array):
    length = len(array)
    # 控制第几次循环
    for i in range(length-1, 0, -1):
        # 控制每次循环的次数
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == '__main__':
    array = [5, 1, 4, 9, 6, 8]
    print(bubblesort(array))
