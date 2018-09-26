"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

示例 1:

输入: [2,2,1]
输出: 1

示例 2:

输入: [4,1,2,1,2]
输出: 4
"""


# 时间复杂度是 O(N^2), 在查找数字时还需要遍历一次
def singleNumber(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
        else:
            arr.remove(i)

    return arr.pop()


# 使用 字典 的方式查找某个索引， 时间复杂度是 O(N)
def singleNumber1(nums):
    dic = {}
    for i in nums:
        try:
            dic.pop(i)
        except:
            dic[i] = 1

    return dic.popitem()[0]


# 9 x 9 乘法口诀表
def multiplication():
    # 控制第几次循环
    arr = []
    for i in range(1, 10):
        # 控制每次循环的次数
        for j in range(1, i + 1):
            s = '{}*{} = {}'.format(i, j, i * j)
            arr.append(s)
    return arr


if __name__ == '__main__':
    # nums = [9, 2, 2, 9, 5, 6, 5, ]
    # print(singleNumber1(nums))
    print(multiplication())
