"""
    file operation
    编码
        UTF-8是目前全球通用的编码格式
        除非有特殊需求，否则，一律以UTF-8格式进行文件编码即可
    读取
        read(byte)
        readlines()
        readline()
        close()
    写入
        write
        flush

        直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
        当调用flush的时候，内容会真正写入文件
        这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）
    追加

"""

# file path daily directory
dailyDirectory = "/Users/luozhimin/Desktop/File/picture/daily"
# file read
# 文件可分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别
"""
    语法 
        open(name, mode, encoding)
            name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
            mode：设置打开文件的模式(访问模式)：只读、写入、追加等。
            encoding:编码格式（推荐使用UTF-8）
        mode ->r w a [read,write,append]
        
        read(num)
            num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
        readlines()
            readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
"""
# file = open(dailyDirectory + "/Python.text", "r", encoding="UFT-8")
# need user role
f = open(dailyDirectory + "/Ctest.text", "r", encoding="UTF-8")
print(f"file type = {type(f)}")
# read
# 多次调用 下一次从上一次的尾巴读取
# print(f"read 10 byte result \n{f.read(10)}\n")
# print(f"read any bytes result \n{f.read()}\n")
# 读取文件的全部行 封装到列表中
print("-------")
lines = f.readlines()
print(f"读取的对象类型是{type(lines)},内容是{lines}")

# 读取一行数据
firstLine = f.readline()
print(f"first line -> {firstLine}")
secondLine = f.readline()
print(f"second line -> {secondLine}")

# for read
for line in f:
    print(f"每一行数据为->{line}")

# close
# 最后通过close，关闭文件对象，也就是关闭对文件的占用
# 如果不调用close,同时程序没有停止运行，那么这个文件将一直被Python程序占用
f.close()

# 通过在with open的语句块中对文件进行操作
# 可以在操作完成后自动关闭close文件，避免遗忘掉close方法
# with..open
with open(dailyDirectory + "/Ctest.text", "r") as f:
    for line in f:
        print(f"with .. open .. readLine {line}")

print("------")

count = 0
with open(dailyDirectory + "/word.txt", encoding="UTF-8") as file:
    for line in file:
        lines = line.strip().split(" ")
        for l in lines:
            if l == 'itheima':
                count += 1
print(f"this txt contains word count {count}")

# write
# operation -> open('directory','w',encoding='you encoding') mode 'w' -> write \n
# really write file saving this operation delete source content write new content
# really write file not find this operation create new file and write new content
f = open(dailyDirectory + "/Python.text", "w")
# buffer
f.write("Python write buffer")
# flush write
f.flush()

# append
f = open(dailyDirectory + "/Python.text", "a")
f.write("\n这次是追加到该文件里面")
f.close()

print("-----")
# exercise
f = open(dailyDirectory + "/bill.txt", "r")
fileBak = open(dailyDirectory + "/bill.txt.bak", "w")
for bf in f:
    bfs = bf.strip().split(",")
    if bfs[-1] == '测试':
        continue
    fileBak.write(bf + "\n")
f.close()
fileBak.close()
