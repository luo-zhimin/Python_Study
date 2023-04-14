"""
    递归
"""
# recurrence => re current ce
import os

directory = '/Users/luozhimin/Desktop/File/package/learningMaterials/Python_HM'


def testFile():
    # all directory
    print(os.listdir(directory))
    # 是否是directory
    print(os.path.isdir(directory))
    # 是否存在
    print(os.path.exists(directory))


def get_files_recurrence_form_dir(path) -> list:
    """
    从指定文件夹里面获取全部文件 使用递归
    :param path: 要获取(recurrence)的路径
    :return: list 包含全部文件 stackOverFlow
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            # or re.match(r'(\w*-[\u4e00-\u9fa5]*)\.zip$', f) != ''
            if f == '.DS_Store':
                continue
            # 判断 文件收集 文件夹继续递归
            current_path = path + "/" + f
            if os.path.isdir(current_path):
                # 是文件夹
                file_list += get_files_recurrence_form_dir(current_path)
            else:
                file_list.append(current_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []
    return file_list


if __name__ == '__main__':
    file_lists = get_files_recurrence_form_dir(directory)
    # empty
    for fi in file_lists:
        print(fi)
