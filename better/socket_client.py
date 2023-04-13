import socket

# 创建客户端
socket_client = socket.socket()
# 连接到服务端
socket_client.connect(("localhost", 8888))
while True:
    msg = input("请输入你要发送的消息：")
    if msg == 'exit':
        break
    # 发送消息
    socket_client.send(msg.encode("utf-8"))
    # buff size
    recv_data = socket_client.recv(1024)
    print(f"服务端回复的消息是：{recv_data.decode('utf-8')}")
socket_client.close()
