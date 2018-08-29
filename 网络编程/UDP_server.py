import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s...' % addr)
    s.sendto(b'Hello,%s!' % data,addr)
'''
# 2018年8月14日 13:50:16
# 测试 UDP 协议 服务端  输出结果：
# ============================
d:\GitHub\PythonLearnProject\网络编程>python UDP_server.py
Bind UDP on 9999...
Received from 127.0.0.1:56027...
Received from 127.0.0.1:56027...
Received from 127.0.0.1:56027...
# ============================
'''