"""
    字符串包
"""


def str_reverse(s):
    """
    :param s: 要反转的字符
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("我是字符串"))
