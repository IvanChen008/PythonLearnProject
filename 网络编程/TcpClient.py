import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Micheal',b'Tracy',b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
'''
# 2018年8月14日 11:24:06
# 测试 tcp 客户端
# 运行结果：
# =============================
d:\GitHub\PythonLearnProject\网络编程>python TcpClient.py
Welcome!
Hello,Micheal!
Hello,Tracy!
Hello,Sarah!
# =============================
'''