# 和文件相关
import json

from data_define import Order


# __all__ = ['TextFileReader', 'JsonFileReader']


# 定义抽象类
class FileReader:
    def __init__(self, directory):
        self.path = directory

    def read_data(self) -> list[Order]:
        # 读到的数据转换为Order对象 列表
        pass


class TextFileReader(FileReader):

    def read_data(self) -> list[Order]:
        order_list: list[Order] = []
        f = open(self.path, 'r', encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            line_data = line.strip().split(",")
            order_list.append(Order(line_data[0], line_data[1], int(line_data[2]), line_data[3]))
        f.close()
        return order_list


class JsonFileReader(FileReader):
    def read_data(self) -> list[Order]:
        order_list: list[Order] = []
        f = open(self.path, 'r', encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            json_dict = json.loads(line)
            order_list.append(
                Order(json_dict['date'], json_dict['order_id'], int(json_dict['money']), json_dict['province']))
        f.close()
        return order_list


if __name__ == '__main__':
    reader = TextFileReader("/Users/luozhimin/Desktop/Project/Python_Study/data/面向对象/2011年1月销售数据.txt")
    texts = reader.read_data()
    json_reader = JsonFileReader(
        '/Users/luozhimin/Desktop/Project/Python_Study/data/面向对象/2011年2月销售数据JSON.txt')
    jsons = json_reader.read_data()

    for text in texts:
        print(text)

    print("-----")

    for j in jsons:
        print(j)
