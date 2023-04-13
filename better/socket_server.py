import socket

socket_server = socket.socket()
# bing localhost 8888
socket_server.bind(("localhost", 8888))
# __backlog int 表示接受的连接数量
socket_server.listen(1)
# 等待客户端连接
# return 二元元祖
# result: tuple = socket_server.accept()
# conn = result[0]  # 连接对象
# address = result[0]  # 地址信息
# accept 阻塞
conn, address = socket_server.accept()
print(f"接收到了客户端的连接，客户端的信息是：{address}")
# 接收信息 连接的本次对象
# 循环使用 实现了聊天功能
# recv 缓冲区大小 一般1024 receiver
while True:
    data: str = conn.recv(1024).decode("utf-8")
    print(f"客户端发来的消息是:{data}")
    # 发送回复消息
    # encode 进行编码
    msg = input("请输入你要和客户端回复的消息：")
    # send
    if msg == 'exit':
        break
    conn.send(msg.encode("utf-8"))
# 关闭服务
conn.close()
socket_server.close()
