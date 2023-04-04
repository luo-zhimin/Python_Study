"""
    从物理上看，包就是一个文件夹，在该文件夹下包含了一个 __init__.py 文件，该文件夹可用于包含多个模块文件
从逻辑上看，包的本质依然是模块
    作用
        当我们的模块文件越来越多时,包可以帮助我们管理这些模块, 包的作用就是包含多个模块，但包的本质依然是模块
    新建包后，包内部会自动创建`__init__.py`文件，这个文件控制着包的导入行为

    安装第三方包

"""
# 导入包里面的模块
# import my_package.my_module
# import my_package.my_module2

# my_package.my_module.info()
# my_package.my_module2.info2()

# from my_package import my_module
# from my_package import my_module2
#
# # 不在需要使用包名了
# my_module.info()
# my_module2.info2()

# from my_package.my_module import info
# from my_package.my_module2 import info2
#
# info()
# info2()

# package __all__
from my_package import *

my_module.info()
# because __init__ __all__
# my_module2.info2()
