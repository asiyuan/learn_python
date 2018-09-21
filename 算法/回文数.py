"""
*** 回文数
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    输入: 121
    输出: true

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


def isPalindrome(self, x):
    if x < 0:
        return False
    else:
        if x == int(str(x)[::-1]):
            return True
        else:
            return False
