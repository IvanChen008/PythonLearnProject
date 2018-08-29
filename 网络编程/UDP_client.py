import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
'''
# 2018年8月14日 13:51:29
# 测试 UDP 协议 客户端  输出结果：
# ============================
d:\GitHub\PythonLearnProject\网络编程>python UDP_client.py
Hello,Michael!
Hello,Tracy!
Hello,Sarah!
# ============================
'''