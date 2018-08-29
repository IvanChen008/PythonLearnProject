import socket,threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(1)
print('Waiting for connection...')

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(5)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

'''
# 2018年8月14日 11:24:06
# 测试 tcp 服务端
由于之前编写的时候，tcplink函数写在了无限监听函数后面，导致无法跳出无限循环
编译tcplink函数出现各种连接不上的错误。需要提前写好tcplink函数先编译好。最后调用。
# 运行结果：
# =============================
D:\GitHub\PythonLearnProject\网络编程>python TcpServer.py
Waiting for connection...
Accept new connection from 127.0.0.1:4808...
Connection from 127.0.0.1:4808 closed.
# =============================
'''

