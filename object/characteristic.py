"""
    封装
    继承
    类型注解
    多态
"""


# 封装
# 定义私有成员的方式非常简单，只需要：
# 私有成员变量：变量名以__开头（2个下划线）
# 私有成员方法：方法名以__开头（2个下划线）

class Phone:
    name = None
    producer = None
    # producer = 'MAC'

    # 电压
    __current_voltage = None
    # 是否开启5g
    __is_5g_enable = None

    def __check_5g(self):
        if self.__is_5g_enable and not self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def __keep_single_core(self):
        print("让Cpu以单核形式运行")

    def call_by_5g(self):
        # need judgement none
        # if self.__current_voltage and not self.__current_voltage >= 1:
        #     print("5g通话开启")
        # else:
        #     self.__keep_single_core()
        #     print("通话失败，电量不足")
        self.__check_5g()
        print("正在通话中")


# any extends
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_nfc(self):
        print("nfc读卡")

    def write_nfc(self):
        print("nfc写卡")


# extends
class Phone2022(Phone):
    face_id = "10010"

    def face(self):
        print("2022脸部识别～")


iphone = Phone()
# iphone.__current_voltage=33
# AttributeError
# print(iphone.__current_voltage)
# private Phone' object has no attribute '__keep_single_core'
# print(iphone.__keep_single_core)
iphone.call_by_5g()

# only extends phone2022 extends phone
print(f"-------only extends---------")
phone = Phone2022()
phone.face()
phone.call_by_5g()


# any extends (class1,class2...,classN)
class MyPhone(Phone, NFCReader):
    # 补全语法
    # pass
    # producer override
    producer = 'IMAC'

    def call_by_5g(self):
        print("开始CPU单核模式，确保通话时候省电")
        # print("使用5g网络进行通话")
        # 方式一
        # print(f"父类的厂商是{NFCReader.producer}")
        # Phone.call_by_5g(self)

        # 方式二
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()
        print("关闭cpu单核模式，确保性能")


print("----any extends---")
phone = MyPhone()
# override
phone.call_by_5g()
print(f"myPhone producer override is {phone.producer}")
phone.read_nfc()
phone.write_nfc()


# 多态
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪叫～")


class Cat(Animal):
    def speak(self):
        print("喵喵叫～")


def make_notices(animal: Animal):
    animal.speak()


print("------")
make_notices(Dog())
make_notices(Cat())
