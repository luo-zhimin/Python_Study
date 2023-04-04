"""
    util
"""

from my_utils.file_util import *
from my_utils.str_util import *

# reserve
print(str_reverse("我是综合练习字符串反转"))
# sub
# 从下标1开始到下标5
print(substr("1234567", 1, 5))

directory = "/Users/luozhimin/Desktop/File/picture/daily"
# read
print_file_info(directory + "/Python.text")
# append
append_to_file(directory + "/Python.text", "\nexercise package file util append data in the file")
