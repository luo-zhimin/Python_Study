"""
    文件处理工具
"""


# f = None


def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError as e:
        print(e)
    else:
        # read all bytes
        print(f.read())
    finally:
        f.close()


def append_to_file(file_name, data):
    f = None
    try:
        f = open(file_name, 'a')
    except FileNotFoundError as e:
        print(e)
    else:
        # read all bytes
        f.write(data)
    finally:
        f.close()
