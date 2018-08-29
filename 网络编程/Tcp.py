# Tcp编程测试
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'),html.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)
'''
# 输出结果如下：
# ==============================
D:\GitHub\PythonLearnProject\网络编程>python Tcp.py
HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Tue, 14 Aug 2018 02:34:31 GMT
Content-Type: text/html
Content-Length: 154
Connection: close
Location: https://www.sina.com.cn/
X-Via-CDN: f=edge,s=ctc.ningbo.ha2ts4.104.nb.sinaedge.com,c=182.138.101.45;
X-Via-Edge: 15342140710462d658ab6eebeee7305077e44
<html>
<head><title>302 Found</title></head>
<body bgcolor="white">
<center><h1>302 Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
# ==============================
'''